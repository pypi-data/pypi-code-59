import fetchSubImages.core


def returnUrls(subReddit, maxNumberImgs):
    """
    Return the URLs from the last 'maxNumberImgs' images in the 'subReddit' sub

    :param subReddit: Subreddit for fetching
    :param maxNumberImgs: Maximum number of posts fetched
    :return: List of image URLs

    :type subReddit: str
    :type maxNumberImgs: int
    :rtype: list
    """
    return fetchSubImages.core.returnUrls(subReddit, maxNumberImgs)


def returnTitles(subReddit, maxNumberImgs):
    """
    Return the title of the the last 'maxNumberImgs' images in the 'subReddit' sub

    :param subReddit: Subreddit for fetching
    :param maxNumberImgs: Maximum number of posts fetched
    :return: List of post titles

    :type subReddit: str
    :type maxNumberImgs: int
    :rtype: list
    """
    return fetchSubImages.core.returnTitles(subReddit, maxNumberImgs)


def returnObjs(subReddit, maxNumberImgs):
    """
        Return the last 'maxNumberImgs' images in the 'subReddit' sub as objects containing [title] and [url]

        :param subReddit: Subreddit for fetching
        :param maxNumberImgs: Maximum number of posts fetched
        :return: List of objects containing "title" and "url"

        :type subReddit: str
        :type maxNumberImgs: int
        :rtype: list
    """
    return fetchSubImages.core.returnObjs(subReddit, maxNumberImgs)


def downloadImgs(subReddit, maxNumberImgs, folder):
    """
        Download the last 'maxNumberImgs' images in the 'subReddit' sub to 'folder'

        :param subReddit: Subreddit for downloading
        :param maxNumberImgs: Maximum number of posts to fetch (< 0 to fetch all)
        :param folder: Destination folder

        :type subReddit: str
        :type maxNumberImgs: int
        :type folder: str
    """
    fetchSubImages.core.downloadImgs(subReddit, maxNumberImgs, folder)
