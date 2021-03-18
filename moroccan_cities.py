import bs4, requests

res = requests.get('https://en.wikipedia.org/wiki/List_of_cities_in_Morocco')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elements = soup.select('tbody > tr > td:nth-child(2)')

text_file = open('cities.txt', 'a')

for i in elements:
  text_file.write(i.text + '\n')

text_file.close()

#HTML can be parsed with BeautifulSoup Module
# BeautifulSoup is imported witht the name bs4
# Pass the String with the HTML to the bs4 BeautifulSoup function to get the Soup object
# The Soup object has a select() method that can be passed a string of the CSS selector for an HTML tag
# The select() method will return a list of matching Element objects