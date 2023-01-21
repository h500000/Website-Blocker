import time
from datetime import datetime as dt
path_hosts_file=r"/etc/hosts"
redirect_ip="127.0.0.1"
list_websites=["www.facebook.com", "facebook.com", "youtube.com", "www.youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        with open(path_hosts_file,"r+") as hosts_file:
            content=hosts_file.read()
            for website in list_websites:
                if website in content:
                    pass
                else:
                    hosts_file.write(redirect_ip+" "+website+"\n")
            print(content)
    else:
        with open(path_hosts_file,"r+") as hosts_file:
            content=hosts_file.readlines()
            hosts_file.seek(0)
            for line in content:
                if not any(website in line for website in list_websites):
                    hosts_file.write(line)
            hosts_file.truncate()
            print(content)
    time.sleep(5)  #5 seconds
