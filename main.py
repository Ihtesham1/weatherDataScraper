import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get("https://weather.com/weather/tenday/l/1635c698505df4d47cc0a87bdf5b697154d56b59b2efd7f8b6d12d2457476fb0")
soup = BeautifulSoup(page.content, "html.parser")
complete_data = soup.find(class_ = "region region-main")

dateAndTimes = complete_data.findAll(class_ = "date-time")


timeList = [date.get_text() for date in dateAndTimes]
print(timeList)