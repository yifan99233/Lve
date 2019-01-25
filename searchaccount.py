import  requests
import json
import demjson
from time import sleep

class test ( object ) :
    def __init__ ( self , url , data ) :
        #登陆
        self.url = url
        LoginUrl = '/User/checkLogin'
        self.PostRequests ( url = LoginUrl ,data =data )
        #获取cookie 、 header
        self.cookie = { 'PHPSESSID' : self.r.cookies [ 'PHPSESSID' ] }
        self.header = self.r.request.headers
        print(self.cookie,'\n',self.header)

    #get 请求
    def GetRequests ( self , url , header = '' , cookie  = '' ) :
        url = self.url + url
        self.Get_r = requests.get ( url = url , headers = header , cookies = cookie )

        return self.Get_r
    # post 请求
    def PostRequests ( self , url , header = '' , cookie = '' , data = '' ) :
        url = self.url + url
        self.r = requests.post ( url = url , headers = header , cookies = cookie , data = data )
        #print(url, data ,header,cookie)
        #print ( self.r.status_code , self.r.reason , self.r.json () )
        return self.r
    def test(self , page = 2):
        url = '/Account/uploadedAccount/p/' + str(page)
        v = self.GetRequests( url = url  )
        print(v.status_code, v.reason ,v.text)
        self.r.json()
        #print(self.r.text)
    def XpsUpload ( self , time = 1 ) :
        SearchAccountCount = '/Cser/getPhotoQueue' #查看能接多少单
        XpsSubmit = '/Cser/submitAccount' #修片师上传接口
        RequestsAccountUrl = '/Cser/requestAccount' # 接单接口
        GetHandAccount = '/Cser/getHandleAccount'   #接单后查询接口
        XpsSubmitUrl = '/Cser/submitAccount'
        RequestsAccountData = { 'isMainto' : 0 } #接单 参数
        for i in  range ( time ) :
            #self.PostRequests(url = SearchAccountCount , cookie = self.cookie )
            #接单
            self.PostRequests( url = RequestsAccountUrl , data = RequestsAccountData , cookie = self.cookie , header = self.header )
            #查单
            #self.r.json()
            self.PostRequests ( url = GetHandAccount , cookie = self.cookie , header = '' , data = '' )
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
    #修片师组长审核
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
                        print('%s该流水号修片师组长审核失败'%Caid)
        else:
            AccountInforData = { 'aid' : caid }
            self.PostRequests(url=AccountInforUrl, header=self.header, cookie=self.cookie,data=AccountInforData)
            data = {'aid': caid, 'goodNote': '', 'badNote': '', 'isVisa': 0, 'splPrty': 0}
            self.PostRequests(url = RPassUrl, data=data, header=self.header, cookie=self.cookie)
            if self.r.json()['msg'] == '操作成功':
                print('%s该流水号修片师组长已审核' % caid)
            else:
                print('%s该流水号修片师组长审核失败'% caid)
    def kpsReview(self):
        pass
    def testv(self):
        url = 'Task/autoConfirmSample'
        self.PostRequests(url =url )
        #print(self.r.json())
Url = 'http://qyfh.ops.hzmantu.com'
LoginDataSys = {'user' : 'xpszz' ,
                'pass' : '123'
               }
c = test( url = Url , data = LoginDataSys)
#c.XpsUpload(time = 1)
#c.Review()
#c.testv()



