#Image from CSV Downloader
#by: therealretailer

import requests
import pandas

data = pandas.read_csv('links.csv')

data_link = data['link']
data_name = data['name']

#Status:
print("Script will download: ", len(data), "items")

#Give me the loop:
i = 0
while i < len(data):
    URL = data_link[i]
    response = requests.get(URL)
    current_name = data_link[i]
    open(str(data_name[i]), "wb").write(response.content) 
    print(i, 'Downloading:', data_name[i], 'from:', data_link[i])
    i += 1
