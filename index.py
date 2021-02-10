from iqoptionapi.stable_api import IQ_Option
from tradingview_ta import TA_Handler, Interval, Exchange, Compute
import logging, time, json, configparser

print("_______________________________________")
print("Programm AutoTrade Follow Signal Website Tradingview")
print("_______________________________________")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Easy to use.")
print("Right Now!!!!!! API Not working in 2021.")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")


# ForLoop Fixed Bug
def infinite():
    while True:
        yield


# Configuration 
def settings():
    setting = configparser.RawConfigParser()
    setting.read('settings/config.txt')

    config = {
        'username': setting.get('SETTING', 'username'),
        'password': setting.get('SETTING', 'password'),
        'mode_balance': setting.get('SETTING', 'mode_balance'),
        'symbol': setting.get('SETTING', 'symbol'),
        'interval': setting.get('SETTING', 'interval'),
        'money': setting.get('SETTING', 'money'),
        'exp_mode': setting.get('SETTING', 'exp_mode'),
        'loop_time': setting.get('SETTING', 'loop_time'),
        'time_sleep': setting.get('SETTING', 'time_sleep')
    }

    return config

config = settings()

# Username & Password
print("Logging")
API = IQ_Option(config['username'], config['password'])

# Connected
API.connect()
print("Login Success.")

# Change Mode Balance
# 1. REAL
# 2. PRACTICE
API.change_balance(config['mode_balance'])

# Check Balance
def balance():
    value = API.get_balance()
    # currency = API.get_currency()
    return "balance : ", value


# trackingTradingview Signal
# Example EURUSD
# If EURUSD send BUY
# system send you message "buy"
def trackingTradingview():
    forex = TA_Handler(
        symbol = config['symbol'],
        screener = "forex",
        exchange = Exchange.FOREX,
        interval = Interval.INTERVAL_5_MINUTES
    ) 

    analysis = forex.get_analysis()
    return 'Signal : ' + analysis.summary['RECOMMENDATION']
    # return Compute.PSAR(analysis.indicators["P.SAR"], analysis.indicators["open"])

# Setting Order
# Money, active, put/call, 1m 5m
def binaryMode(money, active, action, expirations_mode):
    binary = API.buy(money, active, action, expirations_mode)
    return binary


# Put Order
def processToOrder():
    money = config['money']
    active = config['symbol']
    exirations_mode = config['exp_mode']
    call = "call"
    put = "put"
    tracking = trackingTradingview()
    binaryMode_Buy = binaryMode(money, active, call, exirations_mode)
    binaryMode_Sell = binaryMode(money, active, put, exirations_mode)

    if(tracking == "STRONG_BUY"):
        result = binaryMode_Buy
        print("Signal : ", trackingTradingview())
        print("IQOPTION : BUY")
    elif(tracking == "STRONG_SELL"):
        result = binaryMode_Sell
        print("Signal : ", trackingTradingview())
        print("IQOPTION : SELL")
    elif(tracking == "BUY"):
        result = binaryMode_Buy
        print("Signal : ", trackingTradingview())
        print("IQOPTION : BUY")
    elif(tracking == "SELL"):
        result = binaryMode_Sell
        print("Signal : ", trackingTradingview())
        print("IQOPTION : SELL")
    else:
        result = "Next Time"

    return result 


if __name__ == "__main__":
    try:
        print(balance())
        for i in range(int(config['loop_time'])):
            # print(trackingTradingview())
            print(processToOrder())
            time.sleep(int(config['time_sleep']))
        print("System Close...")
    except KeyboardInterrupt:
        print('bye')
