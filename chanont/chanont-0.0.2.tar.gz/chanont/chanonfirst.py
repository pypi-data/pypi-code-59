class Chanon:
    #function initial run everytime
    #self variable :ทำด้วยตัวเอง แทนที่ตัวเเปลที่มีการเรียกใช้
    #set default
    
    def __init__(self):
        self.name = 'Chanon'
        self.lastname = 'Tungngeon'
        self.nickname = 'Golf'
        
    def __str__(self):
        return 'This is the Coolest person!!!'
    
    def WhoIAm(self):
        ''' นี่คือ function สำหรับใช้การเเสดงชื่อ '''
        
        print('My name is {}'.format(self.name))
        print('My lastname is {}'.format(self.lastname))
        print('My nickname is {}'.format(self.nickname))

    def thainame(self):
        print('ชานน ถุงเงิน')
        return 'ชานน ถุงเงิน'
    @property    
    def email(self): #property ไม่ต้องใส่()chanon.email()
        return 'Email :{}.{}@gmail.com'.format(self.lastname.lower(),self.name.lower())

#test run    
if __name__ == '__main__':

    #come when print classname

    #ประกาศคลาสเบื้องต้น สร้าง object:chanon
    chanon = Chanon()

    print(help(chanon.WhoIAm))

    print(chanon.name)
    print(chanon.lastname)
    print(chanon.nickname)
    print('--------------')

    chanon.WhoIAm()
    print('-------------------')

    mypaa = Chanon()
    mypaa.name = 'Somjit'
    mypaa.lastname = 'Tungngeon'
    mypaa.nickname = 'Yo'

    mypaa.WhoIAm()
    print('--------------')
    # x=chanon.email()
    # print(x)
    print(chanon.email)
    print(chanon)


