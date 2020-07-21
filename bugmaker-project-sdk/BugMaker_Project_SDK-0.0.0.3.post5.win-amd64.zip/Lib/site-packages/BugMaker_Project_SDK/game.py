import pygame,time
class surface(object):
    """The base class of sth in game."""
    def __init__(self,canvas:pygame.Surface,img:pygame.Surface,x:int,y:int,width:int,height:int,life:int):
        self.canvas=canvas
        self.img=img
        self.initX=x
        self.inirY=y
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.life=life
    def draw(self):
        self.canvas.bilt(self.img,(self.x,self.y))
    def left(self,speed:int):
        self.x-=speed
    def right(self,speed:int):
        self.x+=speed
    def up(self,speed:int):
        self.y-=speed
    def down(self,speed:int):
        self.y+=speed
    def isOnClick(self,mouseX:int,mouseY:int)->bool:
        return self.x<mouseX<self.x+self.width and self.y<mouseY<self.y+self.height
    def die(self,injureLife:int):
        self.life-=injureLife
        self.x=self.initX
        self.y=self.initY
class tools(object):
    lastTime=0
    @classmethod
    def isActionTime(cls,interval):
        if cls.lastTime==0:
            cls.lastTime=time.time()
            return True
        NowTime=time.time()
        if NowTime-cls.lastTime>=interval:
            cls.lastTime=time.time()
            return True
        else:
            return False
