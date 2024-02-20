from bs4 import BeautifulSoup
import time
import pandas as pd


browser = webdriver.Safari()
browser.get("https://en.wikipedia.org/wiki/List_of_brightest_stars")

scraped_data = []

def scrape():
    for i in range(1,2):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        bright_star_table = soup.find_all("table", attrs={"class", "wikitable"})[2]

        table_body = bright_star_table.find("tbody")

        table_rows = table_body.find_all("tr")

        for tr in table_rows:
            td = tr.find_all("td")
            row = [i.text.rstrip() for i in td]
            scraped_data.append(row)

scrape()

stars_data = []

for i in range(1, len(scraped_data)):
    star_dict = {
        "rank": scraped_data[i][0],
        "visual magnitude": scraped_data[i][1],
        "name": scraped_data[i][2],
        "bayer designation": scraped_data[i][3],
        "distance": scraped_data[i][4],
        "spectral type": scraped_data[i][5]
    }
    stars_data.append(star_dict)

headers = ["rank", "visual magnitude", "name", "bayer designation","distance", "spectral type"]
df = pd.DataFrame(stars_data, columns=headers)
df.to_csv("stars.csv",index=False, index_label="id")


browser.quit()

