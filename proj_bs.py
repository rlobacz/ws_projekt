from urllib import request
from bs4 import BeautifulSoup as BS
import re
import csv
import io
import time

start = time.time()
#reading initial url
url = 'https://vcahospitals.com/know-your-pet/cat-breeds'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

#finding urls
tags = bs.find_all('div',{'class':'content-wrapper callout-list-wrapper'})

#creating list of urls
links_bs = []
for i in tags:
    for j in i.find_all('a'):
        links_bs.append('https://vcahospitals.com' + j['href'])

###########################################################################################
#list for output data
output_list = []
output_list.append(['name', 'lifespan', 'weight','lap_cat','intelligence','ease_of_training',
      'grooming_requirements','shedding','good_with_children','good_with_dogs',
      'chattiness','history','behavior','look','grooming','nutritrional_needs',
      'fun_facts'])
#function that scrape data about single cat
def details_all(url):
    html = request.urlopen(url)
    bs = BS(html.read(), 'html.parser')

    name = bs.find('h1').get_text()
    lifespan = bs.find('p', {'class': 'life-span'}).strong.get_text()
    weight = bs.find('p', {'class': 'weight'}).strong.get_text()
    foo_list = [name, lifespan, weight]

    traits = bs.find_all('li', {'class': 'clearfix'})
    stars = [0] * 8
    for i in range(8):
        try:
            stars[i] = len(traits[i].find_all('li', {'class': 'active'}))
        except:
            stars[i] = 0
    foo_list.extend(stars)

    history = bs.find(text=re.compile("History")).parent.find_next_sibling().get_text(strip=True, separator=' ')

    behavior = bs.find(text=re.compile("Behavior")).parent.find_next_sibling().get_text(strip=True, separator=' ')

    look = bs.find(text=re.compile("Look")).parent.find_next_sibling().get_text(strip=True, separator=' ')

    grooming = bs.find(text=re.compile("Nutritional")).parent.find_previous_sibling().get_text(strip=True, separator=' ')

    nutritrional_needs = bs.find(text=re.compile("Nutritional")).parent.find_next_sibling().get_text(strip=True, separator=' ')

    fun_facts = bs.find(text=re.compile("Fun Facts")).parent.find_next_sibling().get_text(strip=True, separator=' ')

    foo_list.extend([history,behavior,look,grooming,nutritrional_needs,fun_facts])

    output_list.append(foo_list)

#looping through links
i=1
mian = str(len(links_bs))
for link in links_bs:
    print("Progress: " + str(i) + "/" + mian)
    details_all(link)
    i = i+1

#saving data to csv
with io.open('data_cats.csv', mode='w', encoding="utf-8") as csv_file:
    data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data.writerows(output_list)

end = time.time()
print("Beautiful Soup scraper ran in " + str(round(end-start,2)) + " seconds.")