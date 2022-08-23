from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/agastya/OneDrive/Desktop/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers=["Name", "Distance", "Mass", "Radius"]
    star_data=[]
    for i in range(0,203):
        soup=BeautifulSoup(browser.page_source, "html.parser")
        for th_tag in soup.find_all("th",attrs=("class","brightest starst")):
            tr_tags=th_tag.find_all("tr")
            temp_list=[]
            for index, tr in enumerate(tr_tags): 
                if index == 1:
                 temp_list.append(tr.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
with open("star.csv", "w") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)
scrape()

