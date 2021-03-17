import bs4, requests

res = requests.get('https://candidature.1337.ma/users/sign_in')

soup =  bs4.BeautifulSoup(res.text, 'html.parser')
btn = soup.select('#new_user > div.form-inputs > div.form-actions > input')
print(btn[0])