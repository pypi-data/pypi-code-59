import requests
bilibiliVideoApi="https://api.bilibili.com/x/web-interface/view?bvid="
class Spider(object):
    def __init__(self,bv:str):
        self.bv=bv.replace("bv","").replace("BV","").replace("Bv","").replace("bV","")
        self.url=(bilibiliVideoApi+bv)
        self.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Referer": "https://www.bilibili.com",
            }
    def get(self,flag:int=0,url:str=None):
        if flag==0:
            reponse=requests.get(self.url,headers=self.headers)
        elif flag==1:
            reponse=requests.get(url,headers=self.headers)
        else:
            raise ValueError("The flag is wrong.")
        return reponse
class Parser(object):
    def __init__(self,spider:Spider):
        self.spider=spider
        self.reponse=self.spider.get()
        self.content=self.reponse.json()
    def jsonParser(self):
        Title=self.content["data"]["title"]#标题
        aid=self.content["data"]["aid"]#AV号
        bvid=self.content["data"]["bvid"]#BV号
        View=self.content["data"]["stat"]["view"]#观看量
        Favourite=self.content["data"]["stat"]["favorite"]#收藏
        Coin=self.content["data"]["stat"]["coin"]#硬币
        Share=self.content["data"]["stat"]["share"]#分享
        Like=self.content["data"]["stat"]["like"]#赞
        return {
            "title":Title,
            "aid":aid,
            "bvid":bvid,
            "view":View,
            "favourite":Favourite,
            "coin":Coin,
            "share":Share,
            "like":Like
            }
class Video(object):
    def __init__(self,bv:str):
        self.bv=bv
        self.url=(bilibiliVideoApi+bv)
        self.spider=Spider(self.bv)
        self.parser=Parser(self.spider)
        self.data=self.parser.jsonParser()
        self.title=self.data["title"]
        self.aid=self.data["aid"]
        self.bvid=self.data["bvid"]
        self.view=self.data["view"]
        self.favourite=self.data["favourite"]
        self.coin=self.data["coin"]
        self.share=self.data["share"]
        self.like=self.data["like"]
        self.linkBv=self.urlget()["Bvid_Version"]
        self.linkAv=self.urlget()["Aid_Version"]
        self.line=8
        self.gc()
    def gc(self):
        del self.bv,self.url,self.spider,self.parser,self.data
    def avidGet(self):
        return self.aid
    def urlget(self):
        return {
            "Aid_Version":"https://www.bilibili.com/video/av"+str(self.aid),
            "Bvid_Version":"https://www.bilibili.com/video/"+self.bvid
        }
    def __str__(self):
        return "标题:\n%s;\nav:av%d;\nbv:%s;\n观看人数:%d;\n收藏人数:%d;\n硬币数量:%d;\n分享数量:%d;\n点赞数量:%d\n%s分界线君%s\n"\
              %(self.title,self.aid,self.bvid,self.view,self.favourite,self.coin,self.share,self.like,"-"*self.line,"-"*self.line)
    def str(self):
        return "av:av%d;\nbv:%s;\n观看人数:%d;\n收藏人数:%d;\n硬币数量:%d;\n分享数量:%d;\n点赞数量:%d\n%s分界线君%s\n"\
              %(self.aid,self.bvid,self.view,self.favourite,self.coin,self.share,self.like,"-"*self.line,"-"*self.line)
