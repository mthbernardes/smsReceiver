import json
import time
import random
import requests
from lxml import html

class util:
    def getCC(self,country):
        with open('numberGen/countryCode.json') as jsonFile:
            data = json.load(jsonFile)
        return data[country]

class generator:
    def __init__(self,):
        self.url = 'http://hs3x.com/'

    def getNumber(self,):
        r = requests.get(self.url)
        tree = html.fromstring(r.content)
        countries = tree.xpath('//*[@class="plistn"][1]/text()')
        numbers = tree.xpath('//*[@class="plistn"][2]/text()')
        paths = tree.xpath('//*[@class="plistn"]/a/@href')
        selected = random.randint(0,len(paths))
        number = numbers[selected]
        self.path = paths[selected]
        countryCode = '+'+util().getCC(countries[selected].strip().lower())
        #util().getCC(country)
        return number.replace(countryCode,''),countryCode

    def checkSMS(self,pattern):
        while 1:
            r = requests.get(self.url+self.path)
            tree = html.fromstring(r.content)
            message = tree.xpath('//*[@class="plistn"][2]/text()')
            for x in range(5):
                if pattern in message[x]:
                    return message[x]
                    break
            time.sleep(5)
