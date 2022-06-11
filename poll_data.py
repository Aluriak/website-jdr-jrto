"""Access to the poll data"""

import csv
import datetime
import requests
from collections import defaultdict


import secrets
URL = secrets.poll_private_url


def get(url=URL, *, ignore_past_sessions=False) -> dict:
    r = requests.get(URL)
    reader = csv.reader(map(lambda s: s.strip(','), r.text.splitlines(False)), delimiter=',')
    header_date = next(reader)
    header_time = next(reader)

    # "in the past" detection
    today = datetime.datetime.today()#.strftime('%Y-%m-%d')
    is_in_the_past = lambda date: (datetime.datetime.strptime(date, '%d/%m/%Y') < today)

    assert len(header_date) == len(header_time)
    datetimes = tuple(zip(header_date, header_time))

    VOTE_VALUE = {'Oui': 2, 'Si nécessaire': 1, 'Non': 0}

    votes = []
    sessions = defaultdict(dict)

    # collect votes per human
    for idx, (human, *human_votes) in enumerate(reader, start=1):
        if human in secrets.ignored_humans: continue
        votes.append((human, [VOTE_VALUE[v] for v in human_votes]))

    # build output: session datetime -> human -> vote
    for vote, dttime in zip(votes, datetimes):
        if ignore_past_sessions and is_in_the_past(dttime[0]): continue
        if vote:
            sessions[dttime][human] = vote
    return datetimes, sessions

def comments_from_sessions(url=URL, *, ignore_past_sessions=False) -> dict:
    datetimes, sessions = get(url, ignore_past_sessions=ignore_past_sessions)
    out = {
        'populated': len(sessions),
        'full': sum(1 for datetime, humans in sessions.items() if len(humans) == 4),
        'overpopulated': sum(1 for datetime, humans in sessions.items() if len(humans) > 4),
        'empty': len(datetimes) - len(sessions),
        'total': len(datetimes),
        'stats': {d: {} for d in sessions},
    }
    for datetime, humans in sessions.items():
        assert len(humans) > 0
        nb_yes = sum(1 for v in humans.values() if v == 2)
        nb_myb = sum(1 for v in humans.values() if v == 1)
        nb_ttl = len(humans)
        names = ', '.join(h if v == 2 else (f'({h})') for h, v in humans.items())
        assert nb_yes + nb_myb == nb_ttl
        out['stats'][datetime]['yes'] = nb_yes
        out['stats'][datetime]['maybe'] = nb_myb
        out['stats'][datetime]['total'] = nb_ttl
        out['stats'][datetime]['names'] = names
        if nb_myb > 0:
            out['stats'][datetime]['comment'] = f"Session {datetime} a entre {nb_yes} et {nb_ttl} personnes prêtes: {names}"
        else:
            out['stats'][datetime]['comment'] = f"Session {datetime} a {nb_yes} personnes prêtes: {names}"
    return out


if __name__ == '__main__':
    sessions = comments_from_sessions()
    print('stats:', sessions['stats'])
    print(f"{sessions['populated']} sessions have at least 1 player registered.")
    print(f"{sessions['empty']} sessions have no player yet.")

