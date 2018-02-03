import bs4
import requests
url = 'https://coinmarketcap.com/currencies/basic-attention-token/historical-data/?start=20130428&end=20180107'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
d = soup.select('table tbody .text-right')
totarr = []
fh = open('d:/batData.txt','a')
print len(d)
for i in range(len(d)):
        data = soup.select('table tbody .text-right')[i]
        x = data.find_all('td')
        d = x[1].getText() + 'xx' + x[2].getText() + 'xx' + x[3].getText() + 'xx' + x[4].getText() + 'xx' + x[5].getText() + 'xx' + x[6].getText()
        d = d.replace('-','0')
        fh.write(d.replace(',','')+'\n')
