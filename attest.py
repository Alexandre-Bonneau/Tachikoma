import unittest
import time
import re
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import xml.etree.ElementTree as ET

import glob

# list_perso = ["Alexandre","Bonneau","27/04/1995","Poitiers","234 avenue st exupery", "Toulouse", "31400"]
# checkbox_value = ["travail","achats","sante","famille","handicap","sport_animaux","convocation","missions","enfants"]

class attest(object):
    def __init__(self, xml ='att_info.xml' ):
        self.xml = xml
        self.tree = ET.parse(xml)
        self.root = self.tree.getroot()
        self.people_list = self.root.findall('people')
        self.downloadPath = "/home/abonneau/Private/test"

    def get_people(self,str):
        for i in self.people_list:
            if eval(str) in eval (i.get('idlist')):
                return i
        return None

    def get_info(self,people):
        list_va=["prenom", "nom","dnaiss", "lnaiss"  ,"addr", "ville","cp"]
        l= [people.find('info').get(i) for i in list_va]
        print(l)
        return l

    def generate_att(self,list_perso,type = "achats"):
        options=Options()
        downloadPath=self.downloadPath
        prefs = {}
        prefs["profile.default_content_settings.popups"]=0
        prefs["download.default_directory"]=downloadPath
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=options)
        driver.get("https://media.interieur.gouv.fr/deplacement-covid-19/")
        value = ["firstname",
        "lastname",
        "birthday",
        "placeofbirth",
        "address",
        "city",
        "zipcode",
        "datesortie",
        "heuresortie"]
        year, month, day, hour, min = map(str, time.strftime("%Y %m %d %H %M").split())

        date=day+"/"+month+"/"+year
        heure=hour+"h"+min
        print(type)
        checkbox = "checkbox-"+type
        list_total = list_perso+[date, heure]
        for i in range(9):
            form = driver.find_element_by_name(value[i])
            form.send_keys(list_total[i])

        form = driver.find_element_by_id(checkbox)
        form.click()
        form = driver.find_element_by_id("generate-btn")
        form.click()
        while len(os.listdir(downloadPath))==0:
            None
        link = (glob.glob(self.downloadPath+"/*")[0])
        while (link[-4:])!=".pdf":
            link = (glob.glob(self.downloadPath+"/*")[0])
            
    def send(self,id):
        pp = self.get_people(str(id))
        files = glob.glob(self.downloadPath+"/*")
        for f in files:
            os.remove(f)
        i=self.get_info(pp)
        self.generate_att(i)
        link=glob.glob(self.downloadPath+"/*")[0]
        return link









# a=attest()
# #
# # alex=a.get_people("482938921416654849")
# # i=a.get_info(alex)
# # a.generate_att(i)
# a.send("482938921416654849")
