
import pymysql
import xlrd
class User(object):
    def __init__(self):

        # 打开数据库连接
        self.db = pymysql.connect(host = "rds11gs3kjhq3aeyr736o.mysql.rds.aliyuncs.com", user = "cloud_dev", password = "u4-vsQxQLv_R15Nf", db = "photo_cloud_dev")
        print(self.db)
        self.cursor = self.db.cursor()

    def Update(self,nick,user= "user",store = 1001,pwd ="202cb962ac59075b964b07152d234b70"):
        #不传name则默认用nick
        if user == "user":
            user = nick
        # 使用cursor()方法获取操作游标
        sql = "UPDATE cloud_staff SET CS_Name = '%s',CS_Pass = '%s',CS_Store = %d WHERE CS_Nick = '%s'"%(user,pwd,store,nick)
        # SQL 更新语句
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            print("更新成功")
        except:
            # 发生错误时回滚
            self.db.rollback()
            print("更新失败")

        # 关闭数据库连接
        self.db.close()
    def AddUser(self,id,nick,type,Num,user = "user",Atype = 0,store = 1001):
        if user == "user":
            user = nick
        SQL = "INSERT INTO cloud_staff (CS_id,CS_Glid,CS_Deputy,CS_Name,CS_Pass,CS_Store,CS_Num, \
              CS_Nick,CS_Phone,CS_Type,CS_AType,CS_StaffId,CS_Level,CS_Exp,CS_Multiple,CS_Score, \
              CS_AccountCount,CS_Money,CS_GiftWrack,CS_PriorityCount,CS_PriorityUsed,CS_IsCserLock, \
              CS_IsCkerTrain,CS_IsBPO,CS_IsShow,CS_PromoteAt,CS_CreateAt)VALUES  \
              (%d, -1, 0, '%s','202cb962ac59075b964b07152d234b70', \
              %d,%d,'%s',13259038769,%d,%d,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1525747185)"%\
              (id,user,store,Num,nick,type,Atype)
        # SQL 插入语句
        try:
            # 执行SQL语句
            self.cursor.execute(SQL)
            # 提交到数据库执行
            self.db.commit()
            print("添加成功")
        except:
            # 发生错误时回滚
            self.db.rollback()
            print("添加失败")
        # 关闭数据库连接
        self.db.close()
    def dell(self):
            SQL = "DELETE FROM cloud_account WHERE  CA_Id = '%s' "
# 更新  --- 必填nick              选填name,pwd,store
# 添加  --- 必填id,nick,type      选填name,Atype,store
# type   --- 1-修片师，2-摄影师，3-看片师，4-修片看片师，77-特殊职位
# Atype  ---  3修片组长 4摄影组长 5摄影督导 6化妆督导 7看片督导 10外包组长
# Atype  ---  75化妆高层 76化妆组长77区域经理 78看片组长 79看片高层 80云学院培训师
# Atype  ---  81区域摄影组长 82摄影高层 83云学院高层 84区域化妆组长
list = [
    {'nick':'摄影师',   'user':'qesys','type':2,'Atype':0},
    {'nick':'修片师',   'user':'qexps','type':1,'Atype':	0},
    {'nick':'修片组长' ,  'user':'qexpszz','type':4,'Atype':3},
    {'nick':'修片副组长', 'user':'qexpsfzz','type':	4,'Atype':8},
    {'nick':'看片师',    'user':'qekps','type':	3,'Atype':0},
    {'nick':'摄影导师',  'user':'qesyds','type':77,'Atype':5},
    {'nick':'化妆导师',  'user':'qehzds','type':77,'Atype':6},
    {'nick':'看片导师',  'user':'qekpds','type':77,'Atype':7},
    {'nick':'摄影专家',  'user':'qesyzj','type':77,'Atype':71},
    {'nick':'化妆专家',  'user':'qehzzj','type':77,'Atype':72},
    {'nick':'摄影督导',  'user':'qesydd','type':77,'Atype':73},
    {'nick':'化妆督导',  'user':'qehzdd','type':77,'Atype':74},
    {'nick':'高层',      'user':'qegc','type':88,'Atype':3},
        {'nick':'管理员',    'user':'qegly','type':	88,'Atype':2},
    {'nick':'云学院高层', 'user':'qeyxygc','type':77,'Atype':83},
    {'nick':'区域化妆组长', 'user':'qeqyhzzz','type':77	,'Atype':84},
    {'nick':'化妆高层',    'user':'qehzgc','type':77,'Atype':75},
    {'nick':'区域摄影组长', 'user':'qeqysyzz','type':77,'Atype':81},
    {'nick':'摄影高层',    'user':'qesygc','type':2,'Atype':82},
    {'nick':'云学院培训师', 'user':'qeyxypxs','type':77,'Atype':80},
    {'nick':'看片高层',    'user':'qekpgc','type':77,'Atype':79},
    {'nick':'看片组长','user':'qekpzz','type':77,'Atype':78},
    {'nick':'区域经理','user':'qeqyjl','type':77,'Atype':77},
    {'nick':'化妆组长','user':'qehzzz','type':77,'Atype':76},
    {'nick':'区域督导','user':'qeqydd','type':77,'Atype':74},
    {'nick':'小海马',  'user':'qexhm','type':77,'Atype':85},
    {'nick':'修片看片师',  'user':'qexpkps','type':4,'Atype':0},

]

def mb(list):

    list = list
#c.dell()
#c.Update(nick = 'gkpsdd' , user = 'gkpsdd'  , store = 1001 )
    m = 500

    for i in list:
        c = User()
        print("*-*"*100)
        c.AddUser(id = m , Num = m , nick = i['nick'] , user = i['user'] , type = i['type'] , Atype = i['Atype'] ,  store = 1001)
        print(i)
        m += 1
mb(list)

