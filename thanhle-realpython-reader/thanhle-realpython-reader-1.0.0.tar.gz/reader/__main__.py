from configparser import ConfigParser
from pkg_resources import resource_string
import sys

from reader import feed
from reader import viewer

def main():
    """Read the Real Python article feed"""
    # Read URL of the Real Python feed from config file
    cfg = ConfigParser()
    cfg.read_string(resource_string(__name__, "config.txt").decode('utf-8'))
    url = cfg.get("feed", "url")

    # If an article ID is given, show the article
    if len(sys.argv) > 1:
        article = feed.get_article(url, sys.argv[1])
        viewer.show(article)
    # If no ID is given, show a list of all articles
    else:
        site = feed.get_site(url)
        titles = feed.get_titles(url)
        viewer.show_list(site, titles)


if __name__ == '__main__':
    main()
