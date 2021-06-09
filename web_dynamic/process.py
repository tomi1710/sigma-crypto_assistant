#!/usr/bin/python3
"""
Made by Facundo Diaz - Tomas De Castro - Tadeo Grach for Holberton School 2021 """


""" IMPORTS EXTERN MODULES """
import time
from datetime import datetime
""" IMPORTS FILES """
import persistence
import entities 
import mail
import info
import percent

""" In case url 1 is not working, changing for these
url = "https://api2.binance.com/"
url = "https://api3.binance.com/"
"""
url = "https://api.binance.com/"
i, a, b = 0

print("Start process at ", datetime.now())

while(i >= 0):
    btc_price = info.consultar_precio_BTC(url)
    persistence.save_price_bitcoin(btc_price)
    eth_price = info.consultar_precio_ETH(url)
    persistence.save_price_ethereum(eth_price)
    doge_price = info.consultar_precio_DOGE(url)
    persistence.save_price_doge(doge_price)
    a = percent.detectar_picos(a)
    b = percent.chequear_movimientos(b)

    """ Save trends every hour """
    if i % 60 == 0:
        percent.insert_in_tendencias()
        print("Insert tendencia at", datetime.now())

    """ Every 3 hours clear history of constants and peaks """
    if i % 180 == 0:
        if a != 0:
            a = 0
            print("Clean mail history of 'detectar_picos'")
        if b != 0:
            b = 0
            print("Clean mail history of 'chequear_movimientos'")

    """ Send daily summary """
    if i % 1440 == 0:
        mail.daily_resume()
        print("Sending daily resume at", datetime.now())

    print("LAP: ", i, "--" , datetime.now())
    i += 1    
    time.sleep(60)
