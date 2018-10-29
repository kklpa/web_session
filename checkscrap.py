import requests
from bs4 import BeautifulSoup as bs

url = 'http://domain.com'
url2 = 'http://domain.com./zakup/last/'
url3 = 'http://domain.com/accounts/login/?next=/'

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0' }

s = requests.Session()

res = s.get(url, verify=False, headers=headers)
print(res.text)
'''if 'csrftoken' in res.cookies:
    csrftoken = res.cookies['csrftoken']
    print('csrftoken', csrftoken)
elif 'csrf' in res.cookies:
    csrftoken = res.cookies['csrf']
    print('csrftoken', csrftoken)
elif 'csrfmiddlewaretoken' in res.cookies:
    csrftoken = res.cookies['csrfmiddlewaretoken']
    print('csrftoken', csrftoken)
'''
middle_search_string = 'csrfmiddlewaretoken\' value=\''
middle_poz = res.text.find(middle_search_string)
middle_val_str = res.text[middle_poz+len(middle_search_string):middle_poz+100]
csrfmiddlewaretoken = middle_val_str[:middle_val_str.rfind('\'')]
print('csrfmiddlewaretoken: ',csrfmiddlewaretoken)

login_data = dict(csrfmiddlewaretoken=csrfmiddlewaretoken, username='', password='',  next='/')
#headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0', 'Cookie' : csrfmiddlewaretoken  }
res = s.post(url3, data=login_data, headers={
'Referer': url3, 
#'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
#'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
#'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
#'DNT': '1',
#'Upgrade-Insecure-Requests': '1'

 })

print('res: ', res.text)

res2 = s.get(url2, cookies=s.cookies)
print('res2: ', res2.text)
