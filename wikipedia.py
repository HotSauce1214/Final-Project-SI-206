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

# def get_grammy_winners(filename):
#     with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), filename), 'r') as f:
#         r = f.read()
#     soup = BeautifulSoup(r, 'html.parser')
#     r = requests.get('https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year')
#     soup = BeautifulSoup(r, 'html.parser')

#     #this isn't right, it should be something more specific I think
#     tags = soup.find_all("table", class_ = "wikitable sortable jquery-tablesorter")


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


def main():
    def get_grammy_winners(filename):
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), filename), 'r') as f:
            r = f.read()
        soup = BeautifulSoup(r, 'html.parser')
        r = requests.get('https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year')
        soup = BeautifulSoup(r, 'html.parser')

        #this isn't right, it should be something more specific I think
        tags = soup.find_all("table", class_ = "wikitable sortable jquery-tablesorter")
