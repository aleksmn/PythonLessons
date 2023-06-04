import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import pandas_datareader.data as pdr

# Простой пример
# Возраст / рост

# plt.plot([11, 12, 14, 15, 18], [143, 151, 167, 172, 180])

# plt.show()

# Инфо пр yfinance
# https://algotrading101.com/learn/yfinance-guide/
# print(dir(yfinance))

# Инфо по  pandas_datareader
# https://pandas-datareader.readthedocs.io/en/latest/



def plot_rub_usd():
    yf.pdr_override()
    df = pdr.DataReader("USDRUB=X", datetime.datetime.today() - datetime.timedelta(days=365))

    # print(df[df['Close'] > 110])

    df = df[df['Close'] > 10]
    df = df[df['Close'] < 110]

    plt.plot(df.index, df.Close, color='green')

    plt.title("Курс рубля к доллару")
    plt.show()



def plot_usd_btc():
    yf.pdr_override()
    df = pdr.DataReader("BTC-USD", datetime.datetime.today() - datetime.timedelta(days=365))
    plt.plot(df.index, df["Close"], color='red')

    plt.title("Курс биткоина")

    plt.show()






if __name__ == "__main__":

    # тесты
    plot_rub_usd()
    # plot_usd_btc()


