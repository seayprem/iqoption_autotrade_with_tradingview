from iqoptionapi.stable_api import IQ_Option
from tradingview_ta import TA_Handler, Interval, Exchange, Compute
import logging 


# Username & Password
print("Logging")
API = IQ_Option("username || email", "password")

# Connected
API.connect()
print("Login Success.")

# Change Mode Balance
# 1. REAL
# 2. PRACTICE
API.change_balance("REAL")

# Check Balance
def balance():
    value = API.get_balance()
    return value


# trackingTradingview Signal
# Example EURUSD
# If EURUSD send BUY
# system send you message "buy"
def trackingTradingview():
    forex = TA_Handler(
        symbol = "EURUSD",
        screener = "forex",
        exchange = Exchange.FOREX,
        interval = Interval.INTERVAL_5_MINUTES
    ) 

    analysis = forex.get_analysis()
    return analysis.summary['RECOMMENDATION']
    # return Compute.PSAR(analysis.indicators["P.SAR"], analysis.indicators["open"])

# Order
def binaryMode(money, active, action, expirations_mode):
    binary = API.buy(money, active, action, expirations_mode)
    return binary

def processToOrder():
    pass

if __name__ == "__main__":
    try:
        print(trackingTradingview())
    except KeyboardInterrupt:
        print('bye')
