import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get("https://weather.com/weather/tenday/l/1635c698505df4d47cc0a87bdf5b697154d56b59b2efd7f8b6d12d2457476fb0")
soup = BeautifulSoup(page.content, "html.parser")
complete_data = soup.find(class_ = "region region-main")

dateAndTimes = complete_data.findAll(class_ = "date-time")
description = complete_data.findAll(class_ = "description")
temperature = complete_data.findAll(class_ = "temp")
precipitation = complete_data.findAll(class_ = "precip")
windSpeed = complete_data.findAll(class_ = "wind")
humidit = complete_data.findAll(class_ = "humidity")




timeList = [date.get_text() for date in dateAndTimes]
#print(timeList)
descriptionList = [desc.get_text() for desc in description]
del descriptionList[0]
#print(descriptionList)
tempList = [temp.get_text() for temp in temperature]
del tempList[0]
#print(tempList)
precipList = [precip.get_text() for precip in precipitation]
del precipList[0]
#print(precipList)
windList = [wind.get_text() for wind in windSpeed]
del windList[0]
#print(windList)
humiditList = [humi.get_text() for humi in humidit]
del humiditList[0]
#print(humiditList)




weather_stuff = pd.DataFrame(
    {
        'DAY': timeList,
        'Description': descriptionList,
        'Temperature': tempList,
        'Wind Speed': windList,
        'Humidit': humiditList,
        'Precipitation': precipList,

    })

print(weather_stuff)

weather_stuff.to_csv('weather.csv')