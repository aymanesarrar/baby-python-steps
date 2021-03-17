import bs4, requests

res = requests.get('https://en.wikipedia.org/wiki/List_of_cities_in_Morocco')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elements = soup.select('tbody > tr > td:nth-child(2)')

text_file = open('cities.txt', 'a')

for i in elements:
  text_file.write(i.text + '\n')

text_file.close()