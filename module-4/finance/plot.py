import matplotlib.pyplot as plt
import yfinance as yf
import datetime


# Установка модулей
# pip install matplotlib
# pip install yfinance

# если ошибка:
# pip install setuptools

# Создадим простой график Возраст / рост

# plt.plot([11, 12, 14, 15, 18], [143, 151, 167, 172, 180])
# plt.title("График возраста и роста")
# plt.show()



# Даты начала и конца отсчета
start_date = datetime.datetime.today() - datetime.timedelta(days=365)
end_date = datetime.datetime.today()


def plot_rub_usd():
    ticker = yf.Ticker("RUB=X")
    data = ticker.history(interval='1d', start=start_date, end=end_date)
    plt.figure(figsize=(10, 5), layout="constrained")
    plt.plot(data.index, data.Open)
    plt.title("График курса рубля к доллару")
    plt.show()


def plot_cny_usd():
    ticker = yf.Ticker("USDCNY=X")
    data = ticker.history(interval='1d', start=start_date, end=end_date)
    plt.figure(figsize=(10, 5), layout="constrained")
    plt.plot(data.index, data.Open, color="red")
    plt.title("Курс юаня к доллару")
    plt.show()


def plot_usd_btc():
    ticker = yf.Ticker("BTC-USD")
    data = ticker.history(interval='1d', start=start_date, end=end_date)
    plt.figure(figsize=(10, 5), layout="constrained")
    plt.plot(data.index, data.Open, color="gold")
    plt.title("Курс биткоина")
    plt.ylabel("USD")
    plt.show()


# Стили
# print(plt.style.available)
# plt.style.use('dark_background')

# Точка входа в программу
if __name__ == "__main__":

    plot_rub_usd()
    plot_cny_usd()
    plot_usd_btc()