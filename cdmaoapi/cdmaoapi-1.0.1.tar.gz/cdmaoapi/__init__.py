'''
文件名称：cdmaoapi库
用处：获取/提交编程猫官方数据
优点：集合大量接口，简化大量requests步骤，只需要一行函数，就可获取资料！
不仅是获取，还可以与官方后台交互，如：回复评论，作品收藏，作品点赞等。
你可以用本库来开发更多有趣的功能哦！
开发者：冷鱼花茶
更新日期：2020.7.18
官方文档：http://doc.viyrs.com/cdmaoapi.html
'''



import requests
import json
from lxml import etree

print('''
***************************
本程序成功调用cdmaoapi库
此版本号：V1.0.0
官方文档：http://doc.viyrs.com/cdmaoapi.html
***************************
''')


def submit(url,data,cookie,ID):
    '''
    函数说明：使用提交数据
    参数ID：srt形式：
    '''
    headers = {'cookie':str(cookie),'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    if ID==1:
        return requests.post(url, headers=headers, json=data)
    elif ID==2:
        return requests.put(url, headers=headers)
    elif ID==3:
        return requests.patch(url, headers=headers)

def submitcomment(zpid, content, cookie):
    '''
    函数说明：使用POST方法提交作品/工作室评论数据
    参数ID：srt形式：
    '''
    data = {'content': str(content), 'rich_content': str(content), 'source':'WORK'}
    url = 'https://api.codemao.cn/web/discussions/'+str(zpid)+'/comment'
    return submit(url, data, cookie,1)


def forumcomments(ltid, content, cookie):
    '''
    函数说明：使用POST方法提交论坛评论数据
    参数ID：srt形式：
    '''
    data = {'content': str(content)}
    url = 'https://api.codemao.cn/web/forums/posts/'+str(ltid)+'/replies'
    return submit(url, data, cookie, 1)


def forumcommentshf(plid, parent_id,content, cookie):
    '''
    函数说明：使用POST方法提交论坛回复评论数据
    参数ID：srt形式：
    '''
    data = {'content': str(content), 'parent_id':str(parent_id)}
    url = 'https://api.codemao.cn/web/forums/replies/'+str(plid)+'/comments'
    return submit(url, data, cookie, 1)



def submitcommenthf(zpid, zhfid, chfid, content, cookie):
    '''
    函数说明：使用POST方法提交作品评论/工作室回复数据
    参数ID：srt形式：
    '''
    data = {'content': str(content), 'parent_id': str(chfid), 'source': 'WORK'}
    url = 'https://api.codemao.cn/web/discussions/'+str(zpid)+'/comments/'+str(zhfid)+'/reply'
    return submit(url, data, cookie, 1)


def forumposting(title,content,ID,cookie):
    '''
    函数说明：使用POST方法提交论坛帖子数据
    参数ID：srt形式：
    '''
    data = {'content': str(content), 'title': str(title)}
    url = 'https://api.codemao.cn/web/forums/boards/'+str(ID)+'/posts'
    return submit(url, data, cookie, 1)


def stmanagement(shop_id, name, preview_url, description, cookie):
    '''
    函数说明：使用POST方法提交工作室资料编辑数据
    参数ID：srt形式：
    '''
    data = {'id': str(shop_id), 'name': str(name), 'preview_url': str(preview_url),'description':str(description)}
    url = 'https://api.codemao.cn/web/work_shops/update'
    return submit(url, data, cookie, 1)


def stdeletesworks(shop_id,zpid,ID,cookie):
    '''
    函数说明：使用POST方法提交工作室作品投稿/删除作品
    参数ID：srt形式：
    '''
    data = {}
    if ID==2:
        url='https://api.codemao.cn/web/work_shops/works/contribute?id='+str(shop_id)+'&work_id='+str(zpid)
    elif ID==1:
        url = 'https://api.codemao.cn/web/work_shops/works/remove?id='+str(shop_id)+'&work_id='+str(zpid)

    return submit(url, data, cookie, 1)


def submitcommentzan(plid,cookie):
    '''
    函数说明：使用PUT方法提交作品/工作室评论点赞
    参数ID：srt形式：
    '''
    data=''
    url = 'https://api.codemao.cn/web/discussions/comments/'+str(plid)+'/liked'
    return submit(url, data, cookie, 2)

def workslike(zpid,cookie):
    '''
    函数说明：使用patch方法提交作品点赞
    参数ID：srt形式：
    '''
    data=''
    url = 'https://api.codemao.cn/web/works/'+str(zpid)+'/like'
    return submit(url, data, cookie, 3)
def workscollection(zpid,cookie):
    '''
    函数说明：使用patch方法提交作收藏
    参数ID：srt形式：
    '''
    data=''
    url = 'https://api.codemao.cn/web/works/'+str(zpid)+'/collection'
    return submit(url, data, cookie, 3)




def get(url):
    # 设置响应头，防止被拦截！
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}

    # 获取JSON
    rr = requests.get(url, headers=headers)
    rr.encoding = 'utf-8'
    rrr = rr.text
    return json.loads(rrr)


def user(bcmid, ID):
    '''
    函数说明：获取用户资料
    参数ID：srt形式：
    '''
    rr = get('https://api.codemao.cn/api/user/info/detail/'+str(bcmid))

    if ID == "name":
        return rr['data']['userInfo']['user']['nickname']
    elif ID == "code":
        return rr['code']
    elif ID == "description":
        return rr['data']['userInfo']['user']['description']
    elif ID == "ID":
        return rr['data']['userInfo']['user']['id']
    elif ID == "doing":
        return rr['data']['userInfo']['user']['doing']
    elif ID == "zpid":
        return rr['data']['userInfo']['work']['id']
    elif ID == "zpname":
        return rr['data']['userInfo']['work']['name']
    elif ID == "avatar":
        return rr['data']['userInfo']['user']['avatar']
    elif ID == "preview":
        return rr['data']['userInfo']['work']['avatar']
    elif ID == "viewTimes":
        return rr['data']['userInfo']['viewTimes']
    elif ID == "praiseTimes":
        return rr['data']['userInfo']['praiseTimes']
    elif ID == "forkedTimes":
        return rr['data']['userInfo']['forkedTimes']
    elif ID == "collectionTimes":
        return rr['data']['userInfo']['collectionTimes']


def userstudio(bcmid, ID):
    '''
    函数说明：获取用户工作室资料
    参数ID：srt形式：
    '''
    rr = get('https://api.codemao.cn/web/work-shops/'+str(bcmid)+'/participators')
    if ID == "subject_id":
        return rr['subject_id']
    elif ID == "name":
        return rr['name']
    elif ID == "level":
        return rr['level']


def userbenoticed(bcmid,ID):
    '''
    函数说明：获取用户被关注资料
    参数ID：srt形式：
    '''
    rr = get('https://api.codemao.cn/api/user/attention/me?user_id='+str(bcmid))
    yhid = []
    name=[]
    avatar=[]

    for i in range(int(rr['data']['total_page'])):
        yhid.append(rr['data']['attentionList'][i]['id'])
        name.append(rr['data']['attentionList'][i]['nickname'])
        avatar.append(rr['data']['attentionList'][i]['avatar'])

    if ID == "yhid":
        return yhid
    elif ID == "name":
        return name
    elif ID == "avatar":
        return avatar
    elif ID == "total_page":
        return rr['data']['total_page']


def userattention(bcmid, ID):
    '''
    函数说明：获取用户关注资料
    参数ID：srt形式：
    '''

    rr = get('https://api.codemao.cn/api/user/me/attention?user_id='+str(bcmid))
    yhid = []
    name = []
    avatar = []

    for i in range(int(rr['data']['total_num'])):
        yhid.append(rr['data']['attentionList'][i]['id'])
        name.append(rr['data']['attentionList'][i]['nickname'])
        avatar.append(rr['data']['attentionList'][i]['avatar'])
        

    if ID == "yhid":
        return yhid
    elif ID == "name":
        return name
    elif ID == "avatar":
        return avatar
    elif ID == "total_num":
        return rr['data']['total_num']











def shops(bcmid, ID):
    '''
    函数说明：获取工作室介绍
    参数ID：srt形式：
    '''
    
    rr = get('https://api.codemao.cn/web/shops/'+str(bcmid))
    
    if ID == "id":
        return rr['id']
    elif ID == "name":
        return rr['name']
    elif ID == "total_score":
        return rr['total_score']
    elif ID == "preview_url":
        return rr['preview_url']
    elif ID == "description":
        return rr['descriptio']
    elif ID == "level":
        return rr['level']


def stmembers(bcmid, ID):
    '''
    函数说明：获取工作室成员
    参数ID：srt形式：
    '''

    rr = get('https://api.codemao.cn/web/shops/'+str(bcmid)+'/users?limit=80&offset=0')
    idd=[]
    name=[]
    avatar_url=[]
    position=[]
    qq=[]
    for i in range(int(rr['total'])):
        if ID == "id":
            idd.append(rr['items'][i]['user_id'])
        elif ID == "name":
            name.append(rr['items'][i]['name'])
        elif ID == "avatar_url":
            avatar_url.append(rr['items'][i]['avatar_url'])
        elif ID == "position":
            position.append(rr['items'][i]['position'])
        elif ID == "qq":
            qq.append(rr['items'][i]['qq'])


        
    if ID == "id":
        return idd
    elif ID == "name":
        return name
    elif ID == "avatar_url":
        return avatar_url
    elif ID == "position":
        return position
    elif ID == "qq":
        return qq
    elif ID == "total":
        return rr['total']


def stsearch(name, ID):
    '''
    函数说明：获取搜索工作室资料
    参数name：srt形式：
    '''

    rr = get('https://api.codemao.cn/web/work-shops/search?name='+str(name)+'&limit=100')
    idd=[]
    name=[]
    avatar_url=[]
    position=[]
    level=[]
    for i in range(int(rr['total'])):
        if ID == "id":
            idd.append(rr['items'][i]['id'])
        elif ID == "name":
            name.append(rr['items'][i]['name'])
        elif ID == "preview_url":
            avatar_url.append(rr['items'][i]['preview_url'])
        elif ID == "position":
            position.append(rr['items'][i]['position'])
        elif ID == "level":
            level.append(rr['items'][i]['level'])


        
    if ID == "id":
        return idd
    elif ID == "name":
        return name
    elif ID == "preview_url":
        return avatar_url
    elif ID == "position":
        return position
    elif ID == "level":
        return qq
    elif ID == "total":
        return rr['total']



def stcomment(gzsid, ID):
    '''
    函数说明：获取工作室评论
    参数gzsid：int形式：
    '''

    rr = get('https://api.codemao.cn/web/discussions/'+str(gzsid)+'/comments?source=WORK_SHOP&sort=-created_at&limit=20&offset=0')
    idd=[]
    nickname=[]
    avatar_url=[]
    position=[]
    level=[]
    work_shop_name=[]
    work_shop_level=[]
    content=[]
    for i in range(20):
        if ID == "id":
            idd.append(rr['items'][i]['id'])
        elif ID == "nickname":
            nickname.append(rr['items'][i]['user']['nickname'])
        elif ID == "avatar_url":
            avatar_url.append(rr['items'][i]['user']['avatar_url'])
        elif ID == "userid":
            position.append(rr['items'][i]['user']['id'])
        elif ID == "subject_id":
            level.append(rr['items'][i]['user']['subject_id'])
        elif ID == "work_shop_name":
            work_shop_name.append(rr['items'][i]['user']['work_shop_name'])
        elif ID == "work_shop_level":
            work_shop_level.append(rr['items'][i]['user']['work_shop_level'])
        elif ID == "content":
            content.append(rr['items'][i]['content'])
        
    if ID == "id":
        return idd
    elif ID == "nickname":
        return nickname
    elif ID == "avatar_url":
        return avatar_url
    elif ID == "userid":
        return position
    elif ID == "subject_id":
        return level
    elif ID == "work_shop_name":
        return work_shop_name
    elif ID == "work_shop_level":
        return work_shop_level
    elif ID == "content":
        return content





def userattention(bcmid, ID):
    '''
    函数说明：获取用户关注资料
    参数ID：srt形式：
    '''

    rr = get('https://api.codemao.cn/api/user/me/attention?user_id='+str(bcmid))
    yhid = []
    name = []
    avatar = []

    for i in range(int(rr['data']['total_num'])):
        yhid.append(rr['data']['attentionList'][i]['id'])
        name.append(rr['data']['attentionList'][i]['nickname'])
        avatar.append(rr['data']['attentionList'][i]['avatar'])
        

    if ID == "yhid":
        return yhid
    elif ID == "name":
        return name
    elif ID == "avatar":
        return avatar
    elif ID == "total_num":
        return rr['data']['total_num']


def homepage(page, ID):
    '''
    函数说明：获取首页作品
    参数ID：srt形式：
    '''

    rr = get(
        'https://api.codemao.cn/web/works/channels/'+str(page)+'/works?type=KITTEN&page=1&limit=10')
    zpid = []
    name = []
    description = []
    view_times = []
    praise_times = []
    preview = []
    userid = []
    nickname = []
    avatar_url = []
    description=[]
    for i in range(9):
        if ID == "zpid":
            zpid.append(rr['items'][i]['id'])
        elif ID == "name":
            name.append(rr['items'][i]['name'])
        elif ID == "description":
            description.append(rr['items'][i]['description'])
        elif ID == "view_times":
            view_times.append(rr['items'][i]['view_times'])
        elif ID == "praise_times":
            praise_times.append(rr['items'][i]['praise_times'])
        elif ID == "preview":
            preview.append(rr['items'][i]['preview'])
        elif ID == "userid":
            userid.append(rr['items'][i]['user']['id'])
        elif ID == "nickname":
            nickname.append(rr['items'][i]['user']['nickname'])
        elif ID == "avatar_url":
            avatar_url.append(rr['items'][i]['user']['avatar_url'])


        
    if ID == "zpid":
        return zpid
    elif ID == "name":
        return name
    elif ID == "description":
        return description
    elif ID == "view_times":
        return view_times
    elif ID == "praise_times":
        return praise_times
    elif ID == "preview":
        return preview
    elif ID == "userid":
        return userid
    elif ID == "nickname":
        return nickname
    elif ID == "avatar_url":
        return avatar_url

    
def stworks(page, sort, ID):
    '''
    函数说明：获取工作室作品
    参数ID：srt形式：
    '''

    rr = get(
        'https://api.codemao.cn/web/works/subjects/'+str(page)+'/works?&offset=0&limit=200&sort='+sort)
    zpid = []
    name = []
    view_time = []
    praise_times = []
    preview = []
    userid = []
    nickname = []
    avatar_url = []
    for i in range(int(rr['total'])):
        if ID == "zpid":
            zpid.append(rr['items'][i]['id'])
        elif ID == "name":
            name.append(rr['items'][i]['name'])
        elif ID == "view_times":
            view_time.append(rr['items'][i]['view_times'])
        elif ID == "praise_times":
            praise_times.append(rr['items'][i]['praise_times'])
        elif ID == "preview":
            preview.append(rr['items'][i]['preview'])
        elif ID == "userid":
            userid.append(rr['items'][i]['user']['id'])
        elif ID == "nickname":
            nickname.append(rr['items'][i]['user']['nickname'])
        elif ID == "avatar_url":
            avatar_url.append(rr['items'][i]['user']['avatar_url'])

        
    if ID == "zpid":
        return zpid
    elif ID == "name":
        return name
    elif ID == "view_times":
        return view_time
    elif ID == "praise_times":
        return praise_times
    elif ID == "preview":
        return preview
    elif ID == "userid":
        return userid
    elif ID == "nickname":
        return nickname
    elif ID == "avatar_url":
        return avatar_url



def personalwork(bcmid, ID):
    '''
    函数说明：获取个人作品
    参数ID：srt形式：
    '''

    rr = get(
        'https://api.codemao.cn/api/user/works/published?user_id='+str(bcmid)+'&limit=100&types=1,3,5')
    zpid = []
    name = []
    preview=[]
    description=[]
    for i in range(int(rr['data']['total_num'])):
        if ID == "id":
            zpid.append(rr['data']['works'][i]['work_id'])
        elif ID == "name":
            name.append(rr['data']['works'][i]['name'])
        elif ID == "description":
            description.append(rr['data']['works'][i]['description'])
        elif ID == "preview":
            preview.append(rr['data']['works'][i]['preview'])
    if ID == "id":
        return zpid
    elif ID == "name":
        return name
    elif ID == "description":
        return description
    elif ID == "preview":
        return preview
    elif ID == "total_num":
        return rr['data']['total_num']


def detailedworks(zpid, ID):
    '''
    函数说明：获取详细作品
    参数ID：srt形式：
    '''

    rr = get(
        'https://api.codemao.cn/web/works/'+str(zpid))
    if ID == "work_name":
        return rr['work_name']
    elif ID == "work_introduction":
        return rr['work_introduction']
    elif ID == "operation_description":
        return rr['operation_description']
    elif ID == "view_times":
        return rr['view_times']
    elif ID == "praise_times":
        return rr['praise_times']
    elif ID == "collect_times":
        return rr['collect_times']
    elif ID == "comment_times":
        return rr['comment_times']
    elif ID == "preview":
        return rr['preview']
    elif ID == "id":
        return rr['user_info']['id']
    elif ID == "avatar":
        return rr['user_info']['avatar']
    elif ID == "nickname":
        return rr['user_info']['nickname']
    elif ID == "signature":
        return rr['user_info']['signature']













def forumac(page,ID):
    '''
    函数说明：获取论坛前20条信息
    参数page：int形式：
    '''
    zpid=[]
    title=[]
    content=[]
    userid=[]
    nickname=[]
    avatar_url=[]
    subject_id=[]
    work_shop_name=[]
    work_shop_level=[]
    if page == 1:
        rr = get('https://api.codemao.cn/web/forums/posts/hots/all')
        rr = rr['items'][:21]
        idd=','.join(rr)
        rr = get("https://api.codemao.cn/web/forums/posts/all?ids="+idd)
    else:
        rr = get('https://api.codemao.cn/web/forums/boards/'+str(page)+'/posts')
    for i in range(20):
        if ID == "id":
            zpid.append(rr['items'][i]['id'])
        if ID == "title":
            title.append(rr['items'][i]['title'])
        if ID == "content":
            content.append(rr['items'][i]['content'])
        if ID == "userid":
            userid.append(rr['items'][i]['user']['id'])
        if ID == "nickname":
            nickname.append(rr['items'][i]['user']['nickname'])
        if ID == "avatar_url":
            avatar_url.append(rr['items'][i]['user']['avatar_url'])
        if ID == "subject_id":
            subject_id.append(rr['items'][i]['user']['subject_id'])
        if ID == "work_shop_name":
            work_shop_name.append(rr['items'][i]['user']['work_shop_name'])
        if ID == "work_shop_level":
            work_shop_level.append(rr['items'][i]['user']['work_shop_level'])
    if ID == "id":
        return zpid
    elif ID == "title":
        return title
    elif ID == "content":
        return content
    elif ID == "userid":
        return userid
    elif ID == "nickname":
        return nickname
    elif ID == "avatar_url":
        return avatar_url
    elif ID == "subject_id":
        return subject_id
    elif ID == "work_shop_name":
        return work_shop_name
    elif ID == "work_shop_level":
        return work_shop_level


def forumsi(ltid, ID):
    '''
    函数说明：获取论坛详细信息
    参数page：int形式：
    '''
    zpid = []
    title = []
    rr = get('https://api.codemao.cn/web/forums/posts/'+str(ltid)+'/details')
    if ID == "userid":
        return rr['user']['id']
    elif ID == "nickname":
        return rr['user']['nickname']
    elif ID == "avatar_url":
        return rr['user']['avatar_url']
    elif ID == "subject_id":
        return rr['user']['subject_id']
    elif ID == "work_shop_name":
        return rr['user']['work_shop_name']
    elif ID == "work_shop_level":
        return rr['user']['work_shop_level']
    elif ID == "title":
        return rr['title']
    elif ID == "content":
        return rr['content']
    elif ID == "board_name":
        return rr['board_name']
    elif ID == "board_id":
        return rr['board_id']
    elif ID == "n_views":
        return rr['n_views']


def forumsea(name, ID):
    '''
    函数说明：获取论坛搜索信息
    参数name：Str形式：
    '''
    zpid = []
    title = []
    userid = []
    nickname = []
    avatar_url = []
    subject_id = []
    work_shop_name = []
    work_shop_level = []

    rr = get(
        'https://api.codemao.cn/web/forums/posts/search?title='+str(name)+'&limit=100')
    for i in range(rr['total']):
        if ID == "id":
            zpid.append(rr['items'][i]['id'])
        if ID == "title":
            title.append(rr['items'][i]['title'])
        if ID == "userid":
            userid.append(rr['items'][i]['user']['id'])
        if ID == "nickname":
            nickname.append(rr['items'][i]['user']['nickname'])
        if ID == "avatar_url":
            avatar_url.append(rr['items'][i]['user']['avatar_url'])
        if ID == "subject_id":
            subject_id.append(rr['items'][i]['user']['subject_id'])
        if ID == "work_shop_name":
            work_shop_name.append(rr['items'][i]['user']['work_shop_name'])
        if ID == "work_shop_level":
            work_shop_level.append(rr['items'][i]['user']['work_shop_level'])
    if ID == "id":
        return zpid
    elif ID == "title":
        return title
    elif ID == "userid":
        return userid
    elif ID == "nickname":
        return nickname
    elif ID == "avatar_url":
        return avatar_url
    elif ID == "subject_id":
        return subject_id
    elif ID == "work_shop_name":
        return work_shop_name
    elif ID == "work_shop_level":
        return work_shop_level

def worksearch(name, ID):
    '''
    函数说明：获取作品搜索信息
    参数name：Str形式：
    '''
    zpid = []
    title = []
    userid = []
    nickname = []
    avatar_url = []
    subject_id = []
    work_shop_name = []
    work_shop_level = []

    rr = get(
        'https://api.codemao.cn/web/works/search?query='+str(name)+'&offset=0&limit=20')
    for i in range(20):
        if ID == "id":
            zpid.append(rr['items'][i]['id'])
        if ID == "name":
            title.append(rr['items'][i]['name'])
        if ID == "userid":
            userid.append(rr['items'][i]['user']['id'])
        if ID == "nickname":
            nickname.append(rr['items'][i]['user']['nickname'])
        if ID == "avatar_url":
            avatar_url.append(rr['items'][i]['user']['avatar_url'])
        if ID == "view_times":
            subject_id.append(rr['items'][i]['view_times'])
        if ID == "praise_times":
            work_shop_name.append(rr['items'][i]['praise_times'])
        if ID == "preview":
            work_shop_level.append(rr['items'][i]['preview'])
    if ID == "id":
        return zpid
    elif ID == "name":
        return title
    elif ID == "userid":
        return userid
    elif ID == "nickname":
        return nickname
    elif ID == "avatar_url":
        return avatar_url
    elif ID == "view_times":
        return subject_id
    elif ID == "praise_times":
        return work_shop_name
    elif ID == "preview":
        return work_shop_level


def carouselfigure(ID):
    '''
    函数说明：获取轮播图
    参数ID：srt形式：
    '''

    rr = get(
        'https://api.codemao.cn/web/banners/all?type=OFFICIAL')
    name = []
    preview = []
    description = []
    subject_id = []
    content = []
    rrr = requests.get("https://api.codemao.cn/web/banners/all?type=OFFICIAL")
    rrr.encoding = 'utf-8'
    rrr = rrr.text
    for i in range(int(rrr.count('title'))):
        if ID == "title":
            name.append(rr['items'][i]['title'])
        elif ID == "target_url":
            description.append(rr['items'][i]['target_url'])
        elif ID == "background_url":
            preview.append(rr['items'][i]['background_url'])
        elif ID == "small_background_url":
            subject_id.append(rr['items'][i]['small_background_url'])

    if ID == "title":
        return name
    elif ID == "target_url":
        return description
    elif ID == "background_url":
        return preview
    elif ID == "small_background_url":
        return subject_id


def streview(gzsid, ID):
    '''
    函数说明：获取工作室评论前20条
    参数ID：srt形式：
    '''

    rr = get(
        'https://api.codemao.cn/web/discussions/'+str(gzsid)+'/comments?source=WORK_SHOP&sort=-created_at&limit=20&offset=0')
    zpid = []
    name = []
    preview = []
    description = []
    subject_id=[]
    content=[]
    for i in range(int(rr['limit'])):
        if ID == "id":
            zpid.append(rr['items'][i]['id'])
        elif ID == "userid":
            name.append(rr['items'][i]['user']['id'])
        elif ID == "nickname":
            description.append(rr['items'][i]['user']['nickname'])
        elif ID == "avatar_url":
            preview.append(rr['items'][i]['user']['avatar_url'])
        elif ID == "subject_id":
            subject_id.append(rr['items'][i]['user']['subject_id'])
        elif ID == "content":
            content.append(rr['items'][i]['content'])
    if ID == "id":
        return zpid
    elif ID == "userid":
        return name
    elif ID == "nickname":
        return description
    elif ID == "avatar_url":
        return preview
    elif ID == "subject_id":
        return subject_id
    elif ID == "content":
        return content


def workreview(zpid, ID):
    '''
    函数说明：获取作品评论前20条
    参数ID：srt形式：
    '''

    rr = get(
        'https://api.codemao.cn/web/discussions/'+str(zpid)+'/comments?source=WORK&sort=-created_at&limit=20&offset=0')
    zpid = []
    name = []
    preview = []
    description = []
    subject_id = []
    content = []
    for i in range(int(rr['limit'])):
        if ID == "id":
            zpid.append(rr['items'][i]['id'])
        elif ID == "userid":
            name.append(rr['items'][i]['user']['id'])
        elif ID == "nickname":
            description.append(rr['items'][i]['user']['nickname'])
        elif ID == "avatar_url":
            preview.append(rr['items'][i]['user']['avatar_url'])
        elif ID == "subject_id":
            subject_id.append(rr['items'][i]['user']['subject_id'])
        elif ID == "content":
            content.append(rr['items'][i]['content'])
    if ID == "id":
        return zpid
    elif ID == "userid":
        return name
    elif ID == "nickname":
        return description
    elif ID == "avatar_url":
        return preview
    elif ID == "subject_id":
        return subject_id
    elif ID == "content":
        return content


def worksub(zpid, plid,ID):
    '''
    函数说明：获取作品子评论
    参数ID：srt形式：
    '''

    rr = get(
        'https://api.codemao.cn/web/discussions/'+str(zpid)+'/comments?source=WORK&sort=-created_at&limit=20&offset=0')
    zpid = []
    name = []
    preview = []
    description = []
    subject_id = []
    content = []
    j=0
    
    for i in range(20):
        if rr['items'][i]['id']==str(plid):
            j=i
            break
    try:
        rr['items'][j]['replies']['total']
    except:
        i="no"

    if i != 'no':
        for i in range(rr['items'][j]['replies']['total']):
            if ID == "id":
                zpid.append(rr['items'][j]['replies']['items'][i]['id'])
            elif ID == "userid":
                name.append(rr['items'][j]['replies']['items'][i]['reply_user']['id'])
            elif ID == "nickname":
                description.append(rr['items'][j]['replies']['items'][i]['reply_user']['nickname'])
            elif ID == "avatar_url":
                preview.append(rr['items'][j]['replies']['items'] [i]['reply_user']['avatar_url'])
            elif ID == "subject_id":
                subject_id.append(rr['items'][j]['replies']['items'][i]['reply_user']['subject_id'])
            elif ID == "content":
                content.append(rr['items'][j]['replies']['items'][i]['content'])
        if ID == "id":
            return zpid
        elif ID == "userid":
            return name
        elif ID == "nickname":
            return description
        elif ID == "avatar_url":
            return preview
        elif ID == "subject_id":
            return subject_id
        elif ID == "content":
            return content
    else:
        return '找不到子评论'



