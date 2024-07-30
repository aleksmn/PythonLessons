import matplotlib.pyplot as plt
import yfinance as yf
import pandas_datareader.data as pdr
import datetime


# Установка модулей
# pip install matplotlib
# pip install yfinance==0.2.35
# pip install pandas_datareader

# если ошибка:
# pip install setuptools

# Создадим простой график Возраст / рост

# plt.plot([11, 12, 14, 15, 18], [143, 151, 167, 172, 180])
# plt.title("График возраста и роста")
# plt.show()


def plot_rub_usd():
    yf.pdr_override()
    df = pdr.DataReader("USDRUB=X", datetime.datetime.today() - datetime.timedelta(days=365))

    plt.plot(df.index, df.Open, color="green")

    plt.title("Курс рубля к доллару")
    plt.show()



def plot_cny_usd():
    yf.pdr_override()
    df = pdr.DataReader("USDCNY=X", datetime.datetime.today() - datetime.timedelta(days=365))

    plt.plot(df.index, df.Open, color="red")

    plt.title("Курс юаня к доллару")
    plt.show()


def plot_usd_btc():
    yf.pdr_override()
    df = pdr.DataReader("BTC-USD", datetime.datetime.today() - datetime.timedelta(days=365))
    plt.plot(df.index, df["Open"], color='gold')

    plt.title("Курс биткоина")
    plt.ylabel("USD")

    plt.show()




# Точка входа в программу
if __name__ == "__main__":

    plot_rub_usd()
    plot_cny_usd()
    plot_usd_btc()