from urllib import request
from bs4 import BeautifulSoup as BS
import re
import csv
import io
import re


url = 'https://vcahospitals.com/know-your-pet/cat-breeds'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('div',{'class':'content-wrapper callout-list-wrapper'})

links_bs = []
for i in tags:
    for j in i.find_all('a'):
        links_bs.append('https://vcahospitals.com' + j['href'])

output_list = []
def details(url):
    html = request.urlopen(url)
    bs = BS(html.read(), 'html.parser')

    name = bs.find('h1').get_text()
    lifespan = bs.find('p',{'class':'life-span'}).strong.get_text()
    weight = bs.find('p',{'class':'weight'}).strong.get_text()
    foo_list = [name,lifespan,weight]

    #traits = bs.find_all('span',{'class':'sr-only'})
    traits = bs.find_all('li',{'class':'clearfix'})
    stars = [0]*8
    for i in range(8):
        try:
            stars[i] = len(traits[i].find_all('li',{'class':'active'}))
        except:
            stars[i] = 0
    foo_list.extend(stars)
    output_list.append(foo_list)

for link in links_bs:
    details(link)

#######################################################################


output_list = []
def details_2(url):
    html = request.urlopen(url)
    bs = BS(html.read(), 'html.parser')

    history = bs.find(text=re.compile("History")).parent.find_next_sibling().get_text(strip=True, separator=' ')

    behavior = bs.find(text=re.compile("Behavior")).parent.find_next_sibling().get_text(strip=True, separator=' ')

    look = bs.find(text=re.compile("Look")).parent.find_next_sibling().get_text(strip=True, separator=' ')

    grooming = bs.find(text=re.compile("Nutritional")).parent.find_previous_sibling().get_text(strip=True, separator=' ')

    nutritrional_needs = bs.find(text=re.compile("Nutritional")).parent.find_next_sibling().get_text(strip=True, separator=' ')

    fun_facts = bs.find(text=re.compile("Fun Facts")).parent.find_next_sibling().get_text(strip=True, separator=' ')

    foo_list = [history,behavior,look,grooming,nutritrional_needs,fun_facts]

    output_list.append(foo_list)

for link in links_bs:
    details_2(link)


###########################################################################################
output_list = []
output_list.append(['name', 'lifespan', 'weight','lap_cat','intelligence','ease_of_training',
      'grooming_requirements','shedding','good_with_children','good_with_dogs',
      'chattiness','history','behavior','look','grooming','nutritrional_needs',
      'fun_facts'])
def details_all(url):
    html = request.urlopen(url)
    bs = BS(html.read(), 'html.parser')

    name = bs.find('h1').get_text()
    lifespan = bs.find('p', {'class': 'life-span'}).strong.get_text()
    weight = bs.find('p', {'class': 'weight'}).strong.get_text()
    foo_list = [name, lifespan, weight]

    # traits = bs.find_all('span',{'class':'sr-only'})
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

for link in links_bs:
    details_all(link)

with open('scraped', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerows(output_list)

with io.open('out.csv', mode='w', encoding="utf-8") as csv_file:
    data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data.writerows(output_list)

#################33
l1 = ['name', 'lifespan', 'weight','lap_cat','intelligence','ease_of_training',
      'grooming_requirements','shedding','good_with_children','good_with_dogs',
      'chattiness','history','behavior','look','grooming','nutritrional_needs',
      'fun_facts']
l1.append(l1)
df = pd.DataFrame(columns=l1)
a_series = pd.Series(to_append, index = df.columns)
df = df.append(a_series, ignore_index=True)
l2=[]
l2.append(l1)
