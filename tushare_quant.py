# -*-coding=utf-8-*-
__author__ = 'Rocky'
import sys,time
import tushare as ts
from toolkit import Toolkit
DATA_GETTING_FLAG="#"
def basic_usage():
    df=ts.get_today_all()
    print df[df['code']=='000006']
    #print df.to_excel('tets.xls')
    #print df[df['code']=='000006']

def quanshan():
    data=Toolkit.getUserData('data.cfg')
    print data
    ts.set_broker('htzq',user=data['huatai'],passwd=data['huatai_passwd'])
    ts.get_broker()
    htzq=ts.TraderAPI('htzq')
    htzq.login()
    info=htzq.baseinfo()
    print info

def getNewStock():
    df= ts.new_stocks()
    df.to_excel('new_stock.xls','gbk')

def _write_console():
    sys.stdout.write(DATA_GETTING_FLAG)
    sys.stdout.flush()

def main():
    #basic_usage()

    #getNewStock()
    for i in range(2):
        _write_console()
        time.sleep(2)
    quanshan()


if __name__=='__main__':

    main()
