from markupsafe import re
import mosspy
import requests
import urllib3
from bs4 import BeautifulSoup
from .models import Files
# from .matches import display_matched
from django.shortcuts import redirect


userid = #########

m = mosspy.Moss(userid, "cc")

def check(file):
    # _path = "/Users/karthik/Projects/MADD/backend/madd/"
    m.addFilesByWildcard("files/*")
    print("fetching moss")
    url = m.send(lambda file_path, display_name: print('*', end='', flush=True))
    print ("Report Url: " + url)

    links_to_parse = []
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    print("match links")
    for link in soup.find_all('a'):
        if link.get('href').startswith(url):
            if link.get('href') not in links_to_parse:
                links_to_parse.append(link.get('href'))
                # print(link.get('href'))

    for link in links_to_parse:
        new_soup = BeautifulSoup(urllib3.PoolManager().request('GET', link).data, 'html.parser')
        users_for_file = []
        holding_text = new_soup.find('title').text.split()
        users_for_file.append(holding_text[2].split('/')[-1])
        users_for_file.append(holding_text[4].split('/')[-1])
        matched = []

        if file in users_for_file:
            user = 1 if users_for_file[0] == file else 2
            code1 = url + '/' + new_soup.findAll('frame')[user].get('src') 
            soup1 = BeautifulSoup(urllib3.PoolManager().request('GET', code1).data, 'html.parser')

            code1match = soup1.find_all('font')
            for i in code1match:
                if i.text not in matched:
                    matched.append(i.text)
