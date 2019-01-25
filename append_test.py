import requests
import json
import pymysql
# def test2():
#     url = 'http://cloud.hzmantu.com/Admin/staffRecover'
#     header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
#     cookie = {
#         'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221674df289f6d-0f47a4d5c96de9-4313362-2073600-1674df289f7187%22%2C%22%24device_id%22%3A%221674df289f6d-0f47a4d5c96de9-4313362-2073600-1674df289f7187%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; MTSESSID=p7o64am14lgdgkslnv2neqehe2'}
#     data = {'staffId':'2829'}
#     r = requests.post(data = data ,url=url, headers=header, cookies=cookie)
#     print(r.json())
# def testGetCookie():
#     url = 'http://sso.dev.hzmantu.com/staff/checkQrLogin'
#     header = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
#     data = {'authCode':'56686c30b01b346b3f90bde4576f737f','appId':'103'}
#     r = requests.post(data = data , url = url , headers = header)
#     v = r.cookies
#     print(r.json(),v)
# testGetCookie()
def test3():
    data = {"aid":"C2018122186419868","photo":[{"id":"6336233","path":"f830476258b50ebd1577ab40320b582c.jpg"},{"id":"6336234","path":"6493b8cb228838205b6758f56c43637d.jpg"},{"id":"6336231","path":"a897e4f1167262fd1cc93cde4e80f97e.jpg"},{"id":"6336232","path":"7bdb7a8520f828ee08909664573a8430.jpg"}]}
    v = json.dumps(data)
    e = json.load()
    print(v,e)
    ll = "aid=C2018122550320247&photo=[{'id':'6363246','path':'a897e4f1167262fd1cc93cde4e80f97e.jpg'},{'id':'6363247','path':'7bdb7a8520f828ee08909664573a8430.jpg'},{'id':'6363248','path':'f830476258b50ebd1577ab40320b582c.jpg'},{'id':'6363249','path':'6493b8cb228838205b6758f56c43637d.jpg'}]"
def test4():
    import turtle
    t = turtle.Pen()
    for x in range(360):
        t.forward(x)
        t.left(100)
def test5():
    da = {'sad':'sad','sad':123}
    mn = list(da)
    #print(mn[1])
    s = '/song?id=1330348068'
    m = s[9:]
    f = open('f.txt', 'a')
    f.write('\n123')

    print(m)

def test6():
    device = pymysql.connect(host='localhost',
                                      db='reping',
                                      user='root',
                                      password='root')

    devices = device.cursor()
    insert = "INSERT INTO song (Sname,Spath)values ('%sdsas','asdasdasd')"
    devices.execute(insert)
    #fin = devices.fetchmany()

    #print(fin)
    device.commit()
sql = 'select Sid from song where  Sname = "天份"'

test6()