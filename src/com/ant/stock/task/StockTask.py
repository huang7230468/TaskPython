# coding:utf-8
import  tushare as ts


class StockTask():

    ####获取市场中所有股票上市信息（沪A，深A，创业板）
    ####主要用来当做每天的列表信息
    def getAllStocksInfo(self):
        stocks = ts.get_stock_basics() ;
        stocks.to_excel('C:/allstock.xlsx')

    ####获取当日所有股票信息（包括现价，开盘价，最高价，最低价...）
    def getAllStocksInfo(self):
        stocks =  ts.get_today_all()
        stocks.to_excel('C:/allstock.xlsx')



StockTask = StockTask()
StockTask.getAllStocksInfo()