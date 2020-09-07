from bs4 import BeautifulSoup
import re
import time
import csv
import sys

from SpiderComponent.PageHandler import PageHandler
from DbComponent.sqlite3Mgr import g_sqlite_mgr


class RentInfo(object):
    def __init__(self):
        self.downtown = ''
        self.street = ''
        self.community = ''
        self.area = 0
        self.rent = 0
    

    def __repr__(self):
        return '%s, %s, %s, %d, %d' % (self.downtown, self.street, self.community, self.rent, self.area)


class LianjiaHandler(PageHandler):
    def __init__(self):
        PageHandler.__init__(self)


    def InitDB(self):
        db = g_sqlite_mgr.GenerateDB('rent.db')
        db.Execute('CREATE TABLE RENT (downtown TEXT, street TEXT, community TEXT,rent INTEGER,area INTEGER);')

    def SaveData(self, rentInfoList):
        if len(rentInfoList) == 0:
            return
        """
        with open('data.csv', 'a+', encoding='utf8') as csvfile:
            csv_writer = csv.writer(csvfile, lineterminator='\n')
            #csv_writer.writerow(['downtown', 'street', 'community', 'rent', 'area'])
            for rentInfo in rentInfoList:
                csv_writer.writerow([rentInfo.downtown, rentInfo.street, rentInfo.community, str(rentInfo.rent), str(rentInfo.area)])
        """
        db = g_sqlite_mgr.GetDB('rent.db')
        for rentInfo in rentInfoList:
            sql = 'INSERT INTO RENT (downtown, street, community, rent, area) VALUES(\'%s\', \'%s\', \'%s\', %d, %d)' % (rentInfo.downtown, rentInfo.street, rentInfo.community, rentInfo.rent, rentInfo.area)
            db.Execute(sql)
        db.Commit()


    def ParseInfo(self, houseInfo):
        res = houseInfo.find(class_='content__list--item--des').find_all('a')
        if res and len(res) == 3:
            rentInfo = RentInfo()
            rentInfo.downtown = res[0].text
            rentInfo.street = res[1].text
            rentInfo.community = res[2].text
            rentStr = houseInfo.find(class_ = 'content__list--item-price').find('em').text
            rentInfo.rent = int(rentStr)
            detail = houseInfo.find(class_='content__list--item--des').text 
            text = re.findall('(\d{1,}㎡)', detail)
            areaStr = text[0][0:-1]
            rentInfo.area = int(areaStr)
            return rentInfo
        return None


    def HandlePage(self, page):
        soup = BeautifulSoup(page, features='html.parser')
        houseList = soup.find(class_ = 'content__list').find_all(class_ = 'content__list--item--main')
        rentInfoList = list()
        for houseInfo in houseList:
            rentInfo = self.ParseInfo(houseInfo)
            if rentInfo:
                rentInfoList.append(rentInfo)
        self.SaveData(rentInfoList)
        return True

        