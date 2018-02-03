import requests, bs4, time

now = time.time()

tar = open('D:\TITLES.txt','r')
num_lines = sum(1 for line in open('movieTitles.txt'))
tarLinks = open('D:\movieVideoLinks.txt','a')

tarline = tar.read().split('\n')
for i in range(num_lines):
    line = tarline[i]
    line += ' official trailer'
    line = line.split(' ')
    url='https://www.youtube.com/results?search_query=+' + '+'.join(line)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    print('Getting video url of %s...' % ' '.join(line))
    videoLink = soup.select('.yt-lockup-thumbnail a')[0]
    tarLinks.write(videoLink['href'] + '\n')

print time.time() - now
