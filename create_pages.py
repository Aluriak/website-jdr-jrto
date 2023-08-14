"""Automatic writing of pages based on external resources"""

import secrets
import datetime
import poll_data


DATE_PAGE_TEMPLATE= """title: Dates
slug: dates

{content}

"""


def create_page_date(poll_private_url: str, poll_public_url: str, ignore_past_sessions: bool = True):
    sessions = poll_data.comments_from_sessions(url=poll_private_url, ignore_past_sessions=ignore_past_sessions)
    lines = [
        f"{sessions['total']} sessions sont disponibles." if sessions['total'] else "Aucune session prévues… C'est curieux !",
        '',
    ]

    if sessions['empty']:
        lines.append(f"{sessions['empty']} sessions n'ont aucun joueur d'inscrit.\n")
    if sessions['populated']:
        lines.append(f"{sessions['populated']} sessions manquent de joueurs.\n")
    if sessions['full']:
        lines.append(f"{sessions['full']} sessions sont complètes.\n")

    lines.append('')

    for session_date, values in sessions['stats'].items():
        lines.append(values['comment'])

    button_poll_link = f'<center><b><a target="_blank" href="{poll_public_url}" style="background-color: #04AA6D; border-radius: 5px; font-size: 17px; font-family: \'Source Sans Pro\', sans-serif; padding: 6px 18px; color: white;">Cliquer ici pour s\'inscrire à une table</a></b></center>'

    return DATE_PAGE_TEMPLATE.format(content='\n'.join(lines) + '\n\n\n' + button_poll_link)


PAGES = {
    "content/pages/dates.mkd": create_page_date,
}


if __name__ == '__main__':
    for page, genfunc in PAGES.items():
        with open(page, 'w') as fd:
            fd.write(genfunc(secrets.poll_private_url, secrets.poll_public_url))
