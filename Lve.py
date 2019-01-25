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
        # 摄影师上传提交的参数
        SubmitData = {'name': p['A_Name'], 'phone': p['A_Phone'],
                      'note': p['note'], 'areye': 1, 'arface': 1,
                      'ardot': 1, 'isToday': 1, 'ptype': 1, 'haimatiAid': aid,
                      'productArr[]': 1,
                      'photoData[0][path]': 'a47a41e745b4df402f6033061911d5d6.jpg',
                      'photoData[0][count]': 1, 'photoData[0][productId]': 1, 'photoData[0][group]': '',
                      'photoData[1][path]': 'e69c2b30ae2282c8a479fe1986be662e.jpg',
                      'photoData[1][count]': 2, 'photoData[1][productId]': 1 , 'photoData[1][group]': '',
                      'photoData[2][path]': '901c7d40870697c82873c2fc26a669be.jpg',
                      'photoData[2][count]': 4, 'photoData[2][productId]': 1, 'photoData[2][group]': '',
                      'photoData[3][path]': '59ede256cbb1caf9f83fd4a2a9dad48b.jpg',
                      'photoData[3][count]': 5, 'photoData[3][productId]': 1, 'photoData[3][group]': '',
                      }
        for i in range ( time ) :
            # 摄影师上传提交接口地址
            PsersubmitAccount = '/Pser/submitAccount'
            #self.test()
            #sys上传调 post请求
            self.PostRequests ( header = self.header , url = PsersubmitAccount , data = SubmitData , cookie = self.cookie )



    def XpsUpload ( self , time = 1 ) :
        SearchAccountCount = '/Cser/getPhotoQueue' #查看能接多少单
        XpsSubmit = '/Cser/submitAccount' #修片师上传接口
        RequestsAccountUrl = '/Cser/requestAccount' # 接单接口
        GetHandAccount = '/Cser/getHandleAccount'   #接单后查询接口
        XpsSubmitUrl = '/Cser/submitAccount'
        RequestsAccountData = { 'isMainto' : 0 } #接单 参数
        for i in  range ( time ) :
            self.PostRequests(url = SearchAccountCount , cookie = self.cookie )
            #接单
            self.PostRequests( url = RequestsAccountUrl , data = RequestsAccountData , cookie = self.cookie , header = self.header )
            #查单
            #self.r.json()
            self.PostRequests ( url = GetHandAccount , cookie = self.cookie , header = '' , data = '' )
            print(self.r.json()['msg'])
            aid = self.r.json()["msg"]["CA_Id"]
            v = self.r.json()["msg"]["oriPhoto"]
            mvp = []
            for i in range(len(v)):
                dict = {"id":list(v.keys())[i],"path":list(v.values())[i]}
                if dict["path"] == "a47a41e745b4df402f6033061911d5d6.jpg":
                    dict["path"] = "a897e4f1167262fd1cc93cde4e80f97e.jpg"
                if dict["path"] == "e69c2b30ae2282c8a479fe1986be662e.jpg":
                    dict["path"] = "7bdb7a8520f828ee08909664573a8430.jpg"
                if dict["path"] == "901c7d40870697c82873c2fc26a669be.jpg":
                    dict["path"] = "f830476258b50ebd1577ab40320b582c.jpg"
                if dict["path"] == "59ede256cbb1caf9f83fd4a2a9dad48b.jpg":
                    dict["path"] = "6493b8cb228838205b6758f56c43637d.jpg"
                # if dict['path'] == 'a47a41e745b4df402f6033061911d5d6.jpg':
                #     dict['path'] = 'a897e4f1167262fd1cc93cde4e80f97e.jpg'
                # if dict['path'] == 'a47a41e745b4df402f6033061911d5d6.jpg':
                #     dict['path'] = 'a897e4f1167262fd1cc93cde4e80f97e.jpg'
                list(dict.values())
                mvp.append(dict)
            mvp = str(demjson.encode(mvp))
            XpsSubmitdata = str('aid=%s&photo=%s'%(aid,mvp))
           #XpsSubmitdata = demjson.encode(XpsSubmitdata)
            self.PostRequests( url = XpsSubmitUrl , data = XpsSubmitdata  ,header= self.header,cookie = self.cookie )

    def Review(self , time = 1 , caid = '' ):
        #返回审核页面订单信息的接口 name ''   page   leader -1
        RCaidInforUrl = '/Cker/getCheckList'
        #审核详情界面的接口 aid
        AccountInforUrl = '/Cker/getCheckAccount'
        changestate = '/Cker/changePhotoState'
        changestatedata = { "plant" : "" , "weed" : "" }
        #通过审核的接口
        RPassUrl = '/Cker/passAccount'
        if caid == '' :
            for x in range(1,time+1):
                RCaidInforData = {'name': '', 'page': x , 'leader': -1}
                self.PostRequests(url=RCaidInforUrl, header=self.header, cookie=self.cookie, data=RCaidInforData)
                caid = self.r.json()["msg"]["list"]
                for i in range(10):
                    Caid = caid[i]['CA_Id']
                    AccountInforData = {'aid': Caid}
                    self.PostRequests(url=AccountInforUrl, header=self.header, cookie=self.cookie,data=AccountInforData)
                    RPassData = {'aid': Caid, 'goodNote': '', 'badNote': '', 'isVisa': 0, 'splPrty': 0}
                    self.PostRequests(url=RPassUrl, data=RPassData, header=self.header, cookie=self.cookie)
                    if self.r.json()['msg'] == '操作成功':
                        print('%s该流水号修片师组长已审核'%Caid)
                    else:
                        print('审核失败')
        else:
            AccountInforData = { 'aid' : caid }
            self.PostRequests(url=AccountInforUrl, header=self.header, cookie=self.cookie,data=AccountInforData)
            data = {'aid': caid, 'goodNote': '', 'badNote': '', 'isVisa': 0, 'splPrty': 0}
            self.PostRequests(url = RPassUrl, data=data, header=self.header, cookie=self.cookie)
            if self.r.json()['msg'] == '操作成功':
                print('%s该流水号修片师组长已审核' % caid)
            else:
                print('审核失败')
    def kpsReview(self , cnum = '' , time = 1 ):
        RCaidInforurl = '/Cker/getCheckAccountList'
        AccountInforUrl = '/Account/doCheckAccount'
        pj = '/Cker/appraiseCserAccount'
        if cnum == '' :
            for x in range(1,time+1):
                RCaidInforData = {'type': 3, 'key': '' , 'state': 'all' , 'page':x}
                self.PostRequests(url=RCaidInforurl, header=self.header, cookie=self.cookie, data=RCaidInforData)
                caid = self.r.json()["msg"]["list"]
                print(caid[0]['aid'])
                for i in range(10):
                    Caid = caid[i]['aid']
                    RPassData = 'score=5&comment=456&aid=%s'%Caid
                    self.PostRequests(url=pj, data=RPassData,  header=self.header, cookie=self.cookie)
                    AccountInforData = {'aid': Caid , 'isAgreeShare' : 1 }
                    self.PostRequests(url=AccountInforUrl, header=self.header, cookie=self.cookie,data=AccountInforData)
                    m = self.r.json()['msg']
                    self.PostRequests(url=pj, data=RPassData, header=self.header, cookie=self.cookie)
                    if m == '微信通知未发送,该用户未关注微信公众号或已取消关注':
                        print(Caid+'该流水号看片师已审核')
                    else:
                        print(Caid+'看片师审核失败')
        else:

            Caid = cnum
            RPassData = 'score=5&comment=456&aid=%s' % Caid
            self.PostRequests(url=pj, data=RPassData, header=self.header, cookie=self.cookie)
            AccountInforData = {'aid': Caid, 'isAgreeShare': 1}
            self.PostRequests(url=AccountInforUrl, header=self.header, cookie=self.cookie, data=AccountInforData)
            m = self.r.json()['msg']
            self.PostRequests(url=pj, data=RPassData, header=self.header, cookie=self.cookie)
            if m == '微信通知未发送,该用户未关注微信公众号或已取消关注':
                print(Caid + '该流水号看片师已审核')
            else:
                print(Caid + '看片师审核失败')
#aid = 2019010234714385
#aid = 'K2019010275355410'#sysc3
#aid = 2018122572584418#(金标---1)
#aid = 2019010282934570 #syse结婚
#aid = 2019010253822579 #syse证件---1005
# aid = 2019010221457140 #sysa1结婚dengji---1067
#aid = 2019010234714385 #sysa1证件照---1067
#aid = 2019010243380113 #签证照---1067
aid = 2019010253822579 #证件---1067
#aid = 2019010269657142 #签证照---1001
#aid = 2019010269750081 #证件照---1001

Url = 'http://npwz.ops.hzmantu.com'
# sys登陆参数
LoginDataSys = {'user' : 'sysj1' ,
                'pass' : '123'
               }
# xps登陆参数
LoginDataXps = {'user' : 'mxps500' ,
                'pass' : '123'
               }
def Sys () :
    c = test(url = Url , data = {'user' : 'mmsys' ,
                'pass' : '123'
               })
    c.SysUpload(   aid = 2018103086060133 , time = 1 )

#Sys()
def Xps():
    c = test(url = Url , data = {'user' : 'xps' ,
                'pass' : '123'
               })
    c.XpsUpload(time=1)
#Xps()
def Review():
    c = test(url = Url,data = {'user':'xpszz','pass':123})
    c.Review(time=500)
#Review()
def kpsReview():
    c = test(url = Url,data = {'user':'kps','pass':123})
    c.kpsReview(time=1)
kpsReview()
# c = test(url = Url , data = LoginDataSys)
#
# # for x in range(10):
#     print(c.Random(7,15))