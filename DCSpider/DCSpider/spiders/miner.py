import scrapy
import json
from DCSpider.items import DCItems
import datetime


class DCSpider(scrapy.Spider):
    name = "miner"
    allowed_domains = ['antpool.com']
    start_urls = ['https://www.antpool.com/webService.htm']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS":{
            'host': 'www.antpool.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'cookie': '_ga=GA1.2.1672356070.1519308418; acw_tc=AQAAAKKyT191UAYAt0qmdf2kNPa8cNl5; _gid=GA1.2.132665962.1519562145; JSESSIONID=01E4C42EA2856E5F14417AB2787374E6'
        },
        "ITEM_PIPELINES":{
            'MySpider.pipelines.DCSpiderPipeline': 300,
        }
    }

    def parse(self, response):
        jsonBody = json.loads(response.body)
        models = jsonBody['Data']['homeForm']
        modelItems = []

        for dict in models:
            modelItem = DCItems()
            try:
                create_date = datetime.datetime.strptime(create_date, "%Y/%m/%d").date()
            except Exception as e:
                create_date = datetime.datetime.now.date()
            modelItem['create_date'] = create_date
            # ZEC
            modelItem['zecActiveWorkerNumber'] = dict['zecActiveWorkerNumber']
            modelItem['zecBlockNumber'] = dict['zecBlockNumber']
            modelItem['zecCurrentRound'] = dict['zecCurrentRound']
            modelItem['zecEstimateTime'] = dict['zecEstimateTime']
            modelItem['zecNetworkDiff'] = dict['zecNetworkDiff']
            modelItem['zecPoolHashrate'] = dict['zecPoolHashrate']
            modelItem['zecShareNumber'] = dict['zecShareNumber']
            # SC
            modelItem['scActiveWorkerNumber'] = dict['scActiveWorkerNumber']
            modelItem['scBlockNumber'] = dict['scBlockNumber']
            modelItem['scCurrentRound'] = dict['scCurrentRound']
            modelItem['scEstimateTime'] = dict['scEstimateTime']
            modelItem['scNetworkDiff'] = dict['scNetworkDiff']
            modelItem['scPoolHashrate'] = dict['scPoolHashrate']
            modelItem['scShareNumber'] = dict['scShareNumber']
            # LTC
            modelItem['ltcActiveWorkerNumber'] = dict['ltcActiveWorkerNumber']
            modelItem['ltcBlockNumber'] = dict['ltcBlockNumber']
            modelItem['ltcCurrentRound'] = dict['ltcCurrentRound']
            modelItem['ltcEstimateTime'] = dict['ltcEstimateTime']
            modelItem['ltcNetworkDiff'] = dict['ltcNetworkDiff']
            modelItem['ltcPoolHashrate'] = dict['ltcPoolHashrate']
            modelItem['ltcShareNumber'] = dict['ltcShareNumber']
            # ETH
            modelItem['ethActiveWorkerNumber'] = dict['ethActiveWorkerNumber']
            modelItem['ethBlockNumber'] = dict['ethBlockNumber']
            modelItem['ethCurrentRound'] = dict['ethCurrentRound']
            modelItem['ethEstimateTime'] = dict['ethEstimateTime']
            modelItem['ethNetworkDiff'] = dict['ethNetworkDiff']
            modelItem['ethPoolHashrate'] = dict['ethPoolHashrate']
            modelItem['ethShareNumber'] = dict['ethShareNumber']
            # ETC
            modelItem['etcActiveWorkerNumber'] = dict['etcActiveWorkerNumber']
            modelItem['etcBlockNumber'] = dict['etcBlockNumber']
            modelItem['etcCurrentRound'] = dict['etcCurrentRound']
            modelItem['etcEstimateTime'] = dict['etcEstimateTime']
            modelItem['etcNetworkDiff'] = dict['etcNetworkDiff']
            modelItem['etcPoolHashrate'] = dict['etcPoolHashrate']
            modelItem['etcShareNumber'] = dict['etcShareNumber']
            # DASH
            modelItem['dashActiveWorkerNumber'] = dict['dashActiveWorkerNumber']
            modelItem['dashBlockNumber'] = dict['dashBlockNumber']
            modelItem['dashCurrentRound'] = dict['dashCurrentRound']
            modelItem['dashEstimateTime'] = dict['dashEstimateTime']
            modelItem['dashNetworkDiff'] = dict['dashNetworkDiff']
            modelItem['dashPoolHashrate'] = dict['dashPoolHashrate']
            modelItem['dashShareNumber'] = dict['dashShareNumber']
            # BCH
            modelItem['bccActiveWorkerNumber'] = dict['bccActiveWorkerNumber']
            modelItem['bccBlockNumber'] = dict['bccBlockNumber']
            modelItem['bccCurrentRound'] = dict['bccCurrentRound']
            modelItem['bccEstimateTime'] = dict['bccEstimateTime']
            modelItem['bccNetworkDiff'] = dict['bccNetworkDiff']
            modelItem['bccPoolHashrate'] = dict['bccPoolHashrate']
            modelItem['bccShareNumber'] = dict['bccShareNumber']
            # BTC
            modelItem['activeWorkerNumber'] = dict['activeWorkerNumber']
            modelItem['blockNumber'] = dict['blockNumber']
            modelItem['currentRound'] = dict['currentRound']
            modelItem['estimateTime'] = dict['estimateTime']
            modelItem['networkDiff'] = dict['networkDiff']
            modelItem['poolHashrate'] = dict['poolHashrate']
            modelItem['shareNumber'] = dict['shareNumber']

            modelItems.append(modelItem)
        return modelItems
