import pymysql
class User(object):
    def kl(self):

        # 打开数据库连接
        self.db = pymysql.connect(host = "rds11gs3kjhq3aeyr736o.mysql.rds.aliyuncs.com", user = "cloud_dev", password = "u4-vsQxQLv_R15Nf", db = "photo_cloud_dev")
        self.cursor = self.db.cursor()

sql = User()
sql.kl()
