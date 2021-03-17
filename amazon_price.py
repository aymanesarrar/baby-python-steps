import bs4, requests

res = requests.get('https://harrypotter.fandom.com/wiki/List_of_spells')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elements = soup.select('.mw-headline > i > a')

harry_potter_spells = open('harry_potter_spells.txt', 'a')
for i in elements:
  harry_potter_spells.write(i.text + '\n')

harry_potter_spells.close()