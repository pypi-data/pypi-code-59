def show(article):
    """Show one article"""
    print(article)

def show_list(site, titles):
    """Show list of articles"""
    print("The latest tutorials from {}".format(site))
    for article_id, title in enumerate(titles):
        print("{} {}".format(article_id,title))