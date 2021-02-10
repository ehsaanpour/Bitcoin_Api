#first Api Test
import requests
import json
import matplotlib.pyplot as plt



#price section function
def price_bit():
    global price
    global day_time
    URL_price= 'https://api.coindesk.com/v1/bpi/historical/close.json'
    request_bource = requests.get(URL_price)
    json_price_file = request_bource.json()['bpi']
    price = list(json_price_file.values())
    time_list = list (json_price_file.keys())
    day_time = []
    for i in time_list:
        day_time.append(i.split('-')[2])

    
#show plot funcion
def show_plot():
    plt.plot(day_time,price)
    plt.title('PLZ do Full screen this page ')
    plt.show()
    

#price function
price_bit()

#show plot
show_plot()

