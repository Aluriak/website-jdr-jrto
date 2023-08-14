AUTHOR = 'lucas'
SITENAME = 'JRTO'
SITEURL = 'https://blog.jdr.bourneuf.net'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
DEFAULT_DATE = 'fs'  # use filesystem value if none given
DEFAULT_DATE_FORMAT = '%d %B %Y'


THEME = 'themes/myhtml5-dopetrope'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_LINKS_ON_MENU = True
DISPLAY_RECENT_POSTS = False
PAGE_ORDER_BY = 'date'
SUMMARY_MAX_LENGTH = 10


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


PATH = 'content'
ARTICLE_PATHS = ['news', 'scenarii', 'faq']

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
# PAGE_URL = ('{slug}.html')
# PAGE_SAVE_AS = ('{slug}.html')
# AUTHOR_URL = ('author/{name}.html')
TAG_URL = '/tag/{name}.html'
TAG_SAVE_AS = '/tag/{name}.html'


# Blogroll
LINKS = (
    ('Inscriptions', 'https://framadate.org/7YyZuwjkESfrPanJ'),
    ('Discord', 'https://discord.com/invite/WkrKQGxZvQ'),
)
OUTLINKS = (
    ('xkcd', 'https://xkcd.com/244/'),
    ('PTGPTB', 'http://ptgptb.fr/'),
    ('Game of Rôles', 'https://www.youtube.com/watch?v=uLOWzZI1vV0'),
)

DEFAULT_PAGINATION = False
