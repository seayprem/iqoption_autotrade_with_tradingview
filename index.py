from iqoptionapi.stable_api import IQ_Option



# Login
def signIn(username, password):
    global API = IQ_Option(username, password)
    global API.connect()
    return True


# Mode Real Money & PRATICE Money
# You can change this here.
def changeModeBalance():
    pass


# Tracking Signal StrongBuy Buy Nature Sell StrongSell
def trackingSignal():
    pass

# Main Process
if __name__ == "__main__":
    pass
