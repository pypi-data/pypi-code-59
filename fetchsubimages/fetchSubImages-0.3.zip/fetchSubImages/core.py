from urllib.request import urlopen
import json
import os.path


class Post:
    """ Post object """
    def __init__(self, title, url):
        """
        :param title: Post's title
        :param url: Post's URL

        :type title: str
        :type url: str
        """
        self.title = title
        self.url = url


def returnUrls(subReddit, maxNumberImgs):
    imgUrls = []
    cont = 0

    jsonUrl = "https://www.reddit.com/r/{}.json?limit=100&raw_json=1".format(subReddit)

    resp = urlopen(jsonUrl).read().decode('utf-8')

    jsonf = json.loads(resp)

    for post in jsonf['data']['children']:
        if post['data']['post_hint'] == "image":
            imgUrls.append(post['data']['preview']['images'][0]['source']['url'])
            cont += 1
            if 0 < maxNumberImgs == cont:
                return imgUrls

    return imgUrls


def returnTitles(subReddit, maxNumberImgs):
    imgTitles = []
    cont = 0

    jsonUrl = "https://www.reddit.com/r/{}.json?limit=100&raw_json=1".format(subReddit)

    resp = urlopen(jsonUrl).read().decode('utf-8')

    jsonf = json.loads(resp)

    for post in jsonf['data']['children']:
        if post['data']['post_hint'] == "image":
            imgTitles.append(post['data']['title'])
            cont += 1
            if 0 < maxNumberImgs == cont:
                return imgTitles

    return imgTitles


def returnObjs(subReddit, maxNumberImgs):
    imgObjs = []

    imgUrls = returnUrls(subReddit, maxNumberImgs)
    imgTitles = returnTitles(subReddit, maxNumberImgs)

    for i in range(0, len(imgUrls)):
        imgObjs.append(Post(imgTitles[i], imgUrls[i]))

    return imgObjs


def downloadImgs(subReddit, maxNumberImgs, Dest):
    imgs = returnObjs(subReddit, maxNumberImgs)

    if not os.path.exists(Dest):
        os.mkdir(Dest)

    for img in imgs:
        title = ''.join(c for c in img.title if (c.isalnum() or c.isspace()))
        content = urlopen(img.url).read()
        open(os.path.join(Dest, "[{}].png".format(title)), "wb").write(content)
