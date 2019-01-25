# utf-8
import requests
import pymysql
from bs4 import BeautifulSoup
class WyMusic(object):
    def __init__(self,id):
        self.id = id


    def bdevice(self,sql):
        device = pymysql.connect(host='localhost',
                                      db='reping',
                                      user='root',
                                      password='root')

        with device.cursor() as devices:
            insert = sql
            devices.execute(insert)
            device.commit()

    def GetId(self):
        url = 'https://music.163.com/playlist?id=' + str(self.id)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'nts_mail_user=13259038769@163.com:-1:1; mail_psc_fingerprint=07de614a52232be93d7fee2b89541180; _ntes_nnid=e7d8c964b471fea946c74feb1b41a9dd,1542248946866; _ntes_nuid=e7d8c964b471fea946c74feb1b41a9dd; usertrack=CrHti1vs2fKYy6xcAwR/Ag==; __f_=1542637517216; WM_TID=cz7%2FBhxmWSRFEABURQY5fw%2BChrspCFda; P_INFO=m13259038769@163.com|1544411745|0|other|00&99|null&null&null#zhj&330100#10#0#0|132769&1||13259038769@163.com; _iuqxldmzr_=32; __utmc=94650624; __utmz=94650624.1545988384.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); WM_NI=lnc60uiOSdl2s%2BQFg9MV00MmR%2BMna5T8Aw4vDfnnYkdU9S0T6mM7Mf8WK3XoEDvCKVBkZgKUFlujBuIy0S%2B7d0xJ1dhiJzErca2MqmR9dOJIBVL0EQwFQN5MusahiHlkN1A%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaed25b86ec8fd1e521b29e8fa6c54f978b8abbee41b2b0a8a7ec668f8fa29af32af0fea7c3b92ab0b2add7b37fab919d85ef3ab1f59fa7e6338f8a00d1d06792f5838fe43f98e88f98b77e88baa28fdc61a88bf7b4b360f6b383d8d06efc8985d4db65879cbaa4ca5e82b59688ca5f86b4bb8bc17f8ba700b4aa3da8f0b8abb470acb7869bc87aa1bffeaef46792e7acb0c943828a84d1c85bb59a9fafb847b7adaf89ec44b0b582d2c437e2a3; JSESSIONID-WYYY=PjYarMMVwXMe%5CaRx1HE%2FqlAUGlmbfMKuT9ZU4e7VXU70Mw1FiwxUHuG431zEaxWqNGay%5Cb9VqMzDhRk9g%2FtosYxSmdfa9PQcdX7cEIxSs6iWhRIdK90cFdYOnc7HDIkw7Kbcv%5CpKpf8tw7Sidgn%2FJ7DDwYg%2FZItEEhQGfBg%2FDBkRlkAO%3A1546015910253; __utma=94650624.1831317185.1544953644.1545988384.1546014110.4; __utmb=94650624.8.10.1546014110',
            'Host': 'music.163.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        r = BeautifulSoup(requests.session().get(url=url, headers=headers).content)
        op = r.find('ul', {'class': 'f-hide'}).find_all('a')
        SongList = []
        for i in op:
            songdict = {}
            path = ('{}'.format(i['href']))
            user = ('{}'.format(i.text))
            songdict['user'] = user
            songdict['path'] = path
            SongList.append(songdict)
        return SongList
    def GetHotComments(self):
        device = pymysql.connect(host='localhost',
                                      db='reping',
                                      user='root',
                                      password='root')
        data = 'params=amde0UQqaeMkmuXgycoJffxL1hu1mViDg1qSY6BJ2llkteFvmNnw44kYSfnFJG8wofkr8N1X0QzeyC3zFBw40tgtTc1%2BOfc4uilw1b6tfsM3LgnY90Rf9d5DPNJQ8CcH5fAaEJGVQkClTFFnOgrF5nuD%2BI41VKifmj5nVFZncVwLjfpKFrKGozJISS8CDExp&encSecKey=00d4768b205721dd536828bb1abb2a4e48a1cdf73cfe982b7fa91be20512ca1933f10efacc04300fbed76e73ad717575cd23efde98357ed206fe150d700ac0c9a0bf491313b64afa3f2cbb85a852a23994e016e30bf7c8d31c712e105458b244c15a627136f571d93d2783101c98065f5d25bc395f0dc110613efa8aa76ea27d'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie':'nts_mail_user=13259038769@163.com:-1:1; mail_psc_fingerprint=07de614a52232be93d7fee2b89541180; _ntes_nnid=e7d8c964b471fea946c74feb1b41a9dd,1542248946866; _ntes_nuid=e7d8c964b471fea946c74feb1b41a9dd; usertrack=CrHti1vs2fKYy6xcAwR/Ag==; __f_=1542637517216; WM_TID=cz7%2FBhxmWSRFEABURQY5fw%2BChrspCFda; P_INFO=m13259038769@163.com|1544411745|0|other|00&99|null&null&null#zhj&330100#10#0#0|132769&1||13259038769@163.com; _iuqxldmzr_=32; __utmz=94650624.1545988384.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=94650624; WM_NI=WlmcU9M3vJZrD33A7XFFbiWnP7SJvu2fqkN%2BaXDgxW4GHK21d2vtqBPgw1h%2BW0Ody96EMAlzZS7b1XAsY6nOFUFzHQolR6b%2BKB2dD%2BwOJ%2BBg0pcYRyeAsaAf0CkX98yuQ2o%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeabf673ed9786b6e45aa2b48ab6c55e978a8f85bc6eb3e9a196f36ee9efa99bb12af0fea7c3b92a95b4a384d8338fedbaabd97a88edfda2b654869aae8ad66694e99dabf57ff2babf8ccd21a3888c88fb5df89988acb13ba8eeba95f44a94b9b9d2eb2195f08185fc33f69b83a2ef729a8df983b45483ad97d7ed45868b8a9bcb5badb49ed7e121899efe85c721b59186ccc16df4b0adbad173a79fbd82c46ef49da5b9bc34bbab9fd3ee37e2a3; JSESSIONID-WYYY=JCCNRQqObs5Oq3VsUnbKTDtUE%5CJC137j8dAzri41xgYgO7cdyzZssdo9bqtFhiRnuQydlphO459FoONrFlhqo8TD3NbYMapzoVQRWHjo0d4RQFWuIgO5WG9khZixVH%2F1t4vGqgm7y8VOODckaF9jb5qTCV8fiK3Bqfv7v2NC0j70eoG2%3A1546183295484; __utma=94650624.1831317185.1544953644.1546171054.1546181693.6; __utmb=94650624.7.10.1546181693',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        f = open('gp4.txt', 'a+',encoding='utf-8')
        SongList = self.GetId()
        devices = device.cursor()
        for x in range(int(len(SongList))):
            url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token='%SongList[x]['path'][9:]
            sad = ('*'*5+SongList[x]['user']+'*'*5+'\n')
            Spath = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token='%SongList[x]['path'][9:]
            Sname = SongList[x]['user']
            Sidvn = x + 100
            print(Sidvn,Sname,Spath)
            f.write(sad)
            #sql1 = "INSERT INTO song (Sname,Spath)values ('%s','%s')"%(pymysql.escape_string(Sname),pymysql.escape_string(Spath))
            #devices.execute(sql1)
            IdSql = 'select Sid from song where Sname = "%s"'%Sname
            #devices.execute(IdSql)
            #Id = devices.fetchall()[0][0]
            #device.commit()

            print(sad)
            r = requests.post(url, headers=headers, data=data)
            vm = len(r.json()['hotComments'])
            for i in range(vm):
                ve = r.json()['hotComments'][i]['content']
                veuser = r.json()['hotComments'][i]['user']['nickname']
                user = veuser
                commitw = ve
                f.write('*'*8)
                f.write(user+':\n')
                f.write(commitw+'\n')
                #sql2 = "INSERT INTO commits (Side,Cnick,Ccommit)values ('%d','%s','%s')"%(Id,pymysql.escape_string(user),pymysql.escape_string(commitw))
                print(Sidvn,user,commitw)
                #devices.execute(sql2)
        device.commit()




c = WyMusic(1978921795)
c.GetId()
c.GetHotComments()