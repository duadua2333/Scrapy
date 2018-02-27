# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DCItems(scrapy.Item):
    # antpool相关数据
    # BTC
    activeWorkerNumber: scrapy.Field()
    blockNumber: scrapy.Field()
    currentRound: scrapy.Field()
    estimateTime: scrapy.Field()
    networkDiff: scrapy.Field()
    poolHashrate: scrapy.Field()
    shareNumber: scrapy.Field()

    # BCH
    bccActiveWorkerNumber: scrapy.Field()
    bccBlockNumber: scrapy.Field()
    bccCurrentRound: scrapy.Field()
    bccEstimateTime: scrapy.Field()
    bccNetworkDiff: scrapy.Field()
    bccPoolHashrate: scrapy.Field()
    bccShareNumber: scrapy.Field()

    # DASH
    dashActiveWorkerNumber: scrapy.Field()
    dashBlockNumber: scrapy.Field()
    dashCurrentRound: scrapy.Field()
    dashEstimateTime: scrapy.Field()
    dashNetworkDiff: scrapy.Field()
    dashPoolHashrate: scrapy.Field()
    dashShareNumber: scrapy.Field()

    # ETC
    etcActiveWorkerNumber: scrapy.Field()
    etcBlockNumber: scrapy.Field()
    etcCurrentRound: scrapy.Field()
    etcEstimateTime: scrapy.Field()
    etcNetworkDiff: scrapy.Field()
    etcPoolHashrate: scrapy.Field()
    etcShareNumber: scrapy.Field()

    # ETH
    ethActiveWorkerNumber: scrapy.Field()
    ethBlockNumber: scrapy.Field()
    ethCurrentRound: scrapy.Field()
    ethEstimateTime: scrapy.Field()
    ethNetworkDiff: scrapy.Field()
    ethPoolHashrate: scrapy.Field()
    ethShareNumber: scrapy.Field()

    # LTC
    ltcActiveWorkerNumber: scrapy.Field()
    ltcBlockNumber: scrapy.Field()
    ltcCurrentRound: scrapy.Field()
    ltcEstimateTime: scrapy.Field()
    ltcNetworkDiff: scrapy.Field()
    ltcPoolHashrate: scrapy.Field()
    ltcShareNumber: scrapy.Field()

    # SC
    scActiveWorkerNumber: scrapy.Field()
    scBlockNumber: scrapy.Field()
    scCurrentRound: scrapy.Field()
    scEstimateTime: scrapy.Field()
    scNetworkDiff: scrapy.Field()
    scPoolHashrate: scrapy.Field()
    scShareNumber: scrapy.Field()

    # ZEC
    zecActiveWorkerNumber: scrapy.Field()
    zecBlockNumber: scrapy.Field()
    zecCurrentRound: scrapy.Field()
    zecEstimateTime: scrapy.Field()
    zecNetworkDiff: scrapy.Field()
    zecPoolHashrate: scrapy.Field()
    zecShareNumber: scrapy.Field()
