import  requests

import demjson
import random
import json
class test ( object ) :
    def __init__ ( self , url , data ) :
        #登陆
        self.url = url
        LoginUrl = '/User/checkLogin'
        self.PostRequests ( url = LoginUrl ,data =data )
        #获取cookie 、 header
        self.cookie = { 'PHPSESSID' : self.r.cookies [ 'PHPSESSID' ] }
        self.header = self.r.request.headers

    #get 请求
    def GetRequests ( self , url , header = '' , cookie  = '' ) :
        url = self.url + url
        self.Get_r = requests.get ( url = url , headers = header , cookies = cookie )
        return self.Get_r
    # post 请求
    def PostRequests ( self , url , header = '' , cookie = '' , data = '' ) :
        url = self.url + url
        self.r = requests.post ( url = url , headers = header , cookies = cookie , data = data )
        #print ( self.r.status_code , self.r.reason , self.r.json () )
        return self.r
    # 随机生成一个浮点数
    def Random(selfa , a ,b ):
        num = random.randint( a , b )
        return num
    def SysUpload ( self ,  aid , time=1 ) :
        # 查找订单接口
        searchAccountUrl = '/Remote/searchAccount'
        searchAccountData = {'aidKey': aid}
        v = self.PostRequests(url=searchAccountUrl, data=searchAccountData, header=self.header, cookie=self.cookie)
        print('*' * 50)
        p = v.json()['msg'][0]
        pid = p['productIdArr'][0]['AI_Pid']
        print(pid)
        # 摄影师上传提交的参数
        SubmitData = {'name': p['A_Name'], 'phone': p['A_Phone'],
                      'note': p['note'], 'areye': 1, 'arface': 1,
                      'ardot': 1, 'isToday': 1, 'ptype': 1, 'haimatiAid': aid,
                      'productArr[]': pid,
                      'photoData[0][path]': 'a47a41e745b4df402f6033061911d5d6.jpg',
                      'photoData[0][count]': 1, 'photoData[0][productId]': pid, 'photoData[0][group]': '',
                      'photoData[1][path]': 'e69c2b30ae2282c8a479fe1986be662e.jpg',
                      'photoData[1][count]': 2, 'photoData[1][productId]': pid , 'photoData[1][group]': '',
                      'photoData[2][path]': '901c7d40870697c82873c2fc26a669be.jpg',
                      'photoData[2][count]': 4, 'photoData[2][productId]': pid, 'photoData[2][group]': '',
                      'photoData[3][path]': '59ede256cbb1caf9f83fd4a2a9dad48b.jpg',
                      'photoData[3][count]': 5, 'photoData[3][productId]': pid, 'photoData[3][group]': '',

                      }
        for i in range ( time ) :
            # 摄影师上传提交接口地址
            PsersubmitAccount = '/Pser/submitAccount'
            #self.test()
            #sys上传调 post请求
            self.PostRequests ( header = self.header , url = PsersubmitAccount , data = SubmitData , cookie = self.cookie )

Url = 'http://qyfh.ops.hzmantu.com'
# sys登陆参数
LoginDataSys1 = {'user' : 'sysl1' ,
                'pass' : '123'}
LoginDataSys2 = {'user' : 'sysl2' ,
                'pass' : '123'}
LoginDataSys3 = {'user' : 'sysl3' ,
                'pass' : '123'}
LoginDataSys4 = {'user' : 'sysl4' ,
                'pass' : '123'}
LoginDataSys5 = {'user' : 'sysj1' ,
                'pass' : '123'}
LoginDataSys6 = {'user' : 'sysj2' ,
                'pass' : '123'}
LoginDataSys7 = {'user' : 'sysj3' ,
                'pass' : '123'}
LoginDataSys8 = {'user' : 'sysj4' ,
                'pass' : '123'}
'''
935c1dfd324c478426864ff44c47e289
c2ed403b52a0fb9fadca854a61094602
b897733b8cfea0146a4d044902dee478
8bb0e813fc28469908d4852f64f84c35
'photoData[4][path]': '695cd67a3c938cc07c0aae465f93976f.jpg',
                      'photoData[4][count]': 6, 'photoData[4][productId]': pid, 'photoData[4][group]': '',
                      'photoData[5][path]': '9212717289d33ab7c6421e7bc99be1ce.jpg',
                      'photoData[5][count]': 7, 'photoData[5][productId]': pid, 'photoData[5][group]': '',
                      'photoData[6][path]': '632b56d2726567491845eaa4294d4406.jpg',
                      'photoData[6][count]': 8, 'photoData[6][productId]': pid, 'photoData[6][group]': '',
                      'photoData[7][path]': '5c1d9188340af0d14c6b3bfe2f0fd0dc.jpg',
                      'photoData[7][count]': 9, 'photoData[7][productId]': pid, 'photoData[7][group]': '',
                      'photoData[8][path]': '8e48cd98173eb8fb044ad49330332809.jpg',
                      'photoData[8][count]': 10, 'photoData[8][productId]': pid, 'photoData[8][group]': '',
                      'photoData[9][path]': '536357262aede0850025da7c690468dc.jpg',
                      'photoData[9][count]': 11, 'photoData[9][productId]': pid, 'photoData[9][group]': '',
                      'photoData[10][path]': '4900cfb5c253a3ec018a3c29728474a9.jpg',
                      'photoData[10][count]': 12, 'photoData[10][productId]': pid, 'photoData[10][group]': '',
                      'photoData[11][path]': '77d5ac1da1ae63d57c1dc73b26fa8cd2.jpg',
                      'photoData[11][count]': 13, 'photoData[11][productId]': pid, 'photoData[11][group]': '',
                      'photoData[12][path]': '7e99f42e9e66d750d2935801c9c23b51.jpg',
                      'photoData[12][count]': 14, 'photoData[12][productId]': pid, 'photoData[12][group]': '',
                      'photoData[13][path]': 'c5f8c235df9dded053100585b9e6f0f6.jpg',
                      'photoData[13][count]': 15, 'photoData[13][productId]': pid, 'photoData[13][group]': '',
                      'photoData[14][path]': '67f1f54e7e00cd1e90e1870b248791ff.jpg',
                      'photoData[14][count]': 16, 'photoData[14][productId]': pid, 'photoData[14][group]': '',
                      'photoData[15][path]': '1695bcb96dbb9ab928f56de09a710842.jpg',
                      'photoData[15][count]': 17, 'photoData[15][productId]': pid, 'photoData[15][group]': '',
                      'photoData[16][path]': 'f638df462ec7793884a206683fea8a45.jpg',
                      'photoData[16][count]': 18, 'photoData[16][productId]': pid, 'photoData[16][group]': '',
                      'photoData[17][path]': '93a10a644e22bbf2c491a16d2bde7439.jpg',
                      'photoData[17][count]': 19, 'photoData[17][productId]': pid, 'photoData[17][group]': '',
                      'photoData[18][path]': 'c3011d2162a7074b9dd32f3c3cea7994.jpg',
                      'photoData[18][count]': 20, 'photoData[18][productId]': pid, 'photoData[18][group]': '',
                      'photoData[19][path]': 'de518872ed1748866bf675723a8c3d6d.jpg',
                      'photoData[19][count]': 3, 'photoData[19][productId]': pid, 'photoData[19][group]': '',
'''
aid1 = 2019010269750081 #证件照---1001
aid2 = 2019010269657142 #签证照---1001
aid3 = 2019010253822579 #证件---1067
aid4 = 2019010243380113 #签证照---1067
#LoginData = {'user' : 'sysl1' , 'pass' : '123'}
LoginData = {'user' : 'sysl1' , 'pass' : '123'}
# def saddas():
#     aid = 2019010269657142#化妆师多人
#     #aid = 'K2018010271015510'#kids
#     #aid = 2019010327554860 #化妆老人
#     #aid = 2019010381234728 #化妆师新人
#     c = test(url=Url, data=LoginData)
#     c.SysUpload(   aid = aid , time = 1 )
# saddas()

'''
化妆技术专家A：
            化妆区域督导A：
                        杭州和达城店---1001
            化妆区域督导B：
                        杭州湖滨银泰in77店---1002
                        义乌之心店---1003
化妆技术专家B:
            化妆区域督导C:
                        义乌之心店---1003
                        杭州城西银泰店---1004
'''

# hz1 = 2019010474957110 #杭州城西银泰店
# hz2 = 2019010494378920 #义乌之心店
# hz3 = 2019010477214195 #杭州湖滨银泰in77店
# hz4 = 2019010327554860 #杭州和达城店
def hz1():
    c = test(url = Url , data = {'user':'ytsys','pass':'123'})
    c.SysUpload(   aid = 2019010474957110 , time = 5 )
def hz2():
    c = test(url = Url , data = {'user':'ywsys','pass':123})
    c.SysUpload(   aid = 2019010494378920 , time = 5 )
def hz3():
    c = test(url = Url , data = {'user':'hbsys','pass':123})
    c.SysUpload(   aid = 2019010477214195 , time = 5 )
def hz4():
    c = test(url = Url , data = {'user':'sys','pass':123})
    c.SysUpload(   aid = 2019010327554860 , time = 5 )
hz1()
hz2()
hz3()
hz4()
# 2019011295910094
# def hz1():
#     c = test(url = Url , data = {'user':'sa','pass':'123'})
#     c.SysUpload(   aid = 2019011363188137 , time = 1 )
# hz1()

# def jhg():
#     c = test(url = Url , data = {'user':'hksys','pass':123})
#     c.SysUpload(   aid = 2019010685024112 , time = 2 )
# jhg()

#
# def Sys1 () :
#     c = test(url = Url , data = LoginDataSys1)
#     c.SysUpload(   aid = aid1 , time = 6 )
# Sys1()
# def Sys2 () :
#     c = test(url = Url , data = LoginDataSys2)
#     c.SysUpload(   aid = aid2 , time = 6 )
# Sys2()
# def Sys3 () :
#     c = test(url = Url , data = LoginDataSys3)
#     c.SysUpload(   aid = aid1 , time = 6 )
# Sys3()
# def Sys4 () :
#     c = test(url = Url , data = LoginDataSys4)
#     c.SysUpload(   aid = aid2 , time = 6 )
# Sys4()
# def Sys5 () :
#     c = test(url = Url , data = LoginDataSys5)
#     c.SysUpload(   aid = aid3 , time = 6 )
# Sys5()
# def Sys6 () :
#     c = test(url = Url , data = LoginDataSys6)
#     c.SysUpload(   aid = aid4 , time = 6 )
# Sys6()
# def Sys7 () :
#     c = test(url = Url , data = LoginDataSys7)
#     c.SysUpload(   aid = aid3 , time = 6 )
# Sys7()
# def Sys8 () :
#     c = test(url = Url , data = LoginDataSys8)
#     c.SysUpload(   aid = aid4 , time = 6 )
# Sys8()
#
# 'K2019010665341021'#拜年照
# 'K2019010631024948'#新年亲子照
# 'K2019010625649957'#新年迷你照
# 'K2019010669755498'#新年纯真照
# def cnm():
#     c = test(url=Url, data={'user':'kdsys','pass':123})
#     c.SysUpload(   aid = 'K2019010669755498' , time = 1 )
# cnm()