from bs4 import BeautifulSoup
import requests
import re
import os
import json
import csv
import unittest
import sqlite3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
import datetime
import pprint
import pandas as pd
import regex

def get_grammy_winners():
    page = requests.get('https://en.wikipedia.org/wiki/Grammy_Award_for_Best_New_Artist#2010s')
    soup = BeautifulSoup(page.content, 'html.parser')
    tags = soup.find_all('tr')

    links = []

    for tag in tags:
        if tag == None:
            continue
        if tag.find('a'):
            links.append(tag.text.strip())
    
    # print(links)

    expression = '201\d'

    dates = []

    for link in links:
        if '2010s' in link:
            dates.append(link)

    matches = re.findall(expression, dates[0])

    dates2 = []

    dates2.extend(matches)
    
    print(dates)

    expression2 = "\n(.+) \("

    matches2 = re.findall(expression2, dates[0])

    names = []

    names.extend(matches2)

    print(names)

    


    # links = []

    # expression = '201\d'

    # for tag in tags:
    #     links.append(tag.find('td'))

    # print(links)

    # dates = []

    # for link in links:
    #     if link == None:
    #         continue
    #     yo = str(link)
    #     matches = re.findall(expression, yo)
    #     dates.extend(matches)

    # print(dates)

    # date = []
    # for tag in tags:
    #     if '201' in tag.find('a').get('title'):
    #         date.append(tag.text.strip())
    
    # print(date)

    # for tag in tags:
    #     if '' in tag.find('a').get('href'):

    # wiki_url = 'https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year'
    # table_id = 'mw-redirect'

    # response =  requests.get(wiki_url)
    # soup = BeautifulSoup(response.text, 'html.parser')

    # tags = soup.find_all('table', attrs={'class': 'wikitable sortable jquery-tablesorter'})


    



def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


def main():
    url = 'https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year'

    get_grammy_winners()

if __name__ == "__main__":
    main()
    unittest.main(verbosity=2)
