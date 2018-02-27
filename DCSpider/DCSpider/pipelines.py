# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DCSpiderPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect("localhost", "duadua", "980608asdf", "spider")
        cursor = db.cursor()
        db.set_character_set('utf8')
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        sql = "INSERT INTO " \
              "antpool(activeWorkerNumber,blockNumber,currentRound,estimateTime,networkDiff,poolHashrate,shareNumber,identity_url,model_url,real_name,total_fan_num,total_favor_num,view_flag,weight)\
              VALUES('%s','%s','%s','%s','%s','%s','%s')"\
              %(item['activeWorkerNumber'], item['blockNumber'], item['currentRound'],item['estimateTime'], item['estimateTime'], item['poolHashrate'], item['shareNumber'])
        try:
            print(sql)
            cursor.execute(sql)
            db.commit()
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        db.close()
        return item
