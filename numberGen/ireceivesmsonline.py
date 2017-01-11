import json
import time
import random
import requests
from lxml import html

class util:
    def getCC(self,country):
        country = 'usa' if country == 'united states' else country
        with open('numberGen/countryCode.json') as jsonFile:
            data = json.load(jsonFile)
        return data[country]

class generator:
    def __init__(self,):
        self.url = 'https://ireceivesmsonline.com'

    def getNumber(self,):
        r = requests.get(self.url)
        tree = html.fromstring(r.content)
        countries = tree.xpath('//*[@class="nostyle"]/text()[2]')
        numbers = tree.xpath('//*[@class="nostyle"]/text()[3]')
        path = tree.xpath('//*[@class="nostyle"]/a/@href')
        selected = random.randint(0,len(numbers))
        number = numbers[selected].strip()
        countryCode = '+'+util().getCC(countries[selected].strip().lower())
        self.path = path[selected]
        return number.replace(countryCode,''),countryCode

    def checkSMS(self,pattern):
        while 1:
            r = requests.get(self.url+self.path)
            tree = html.fromstring(r.content)
            messages = tree.xpath('//*[@id="wrap"]/div/div/table/tbody/tr/td[2]/text()')
            messages.pop(0)
            for x in range(5):
                if pattern in messages[x]:
                    return messages[x]
                    break
            time.sleep(5)
