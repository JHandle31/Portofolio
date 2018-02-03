import bs4, requests    
import urllib2
import socket

url = "http://free-proxy-list.net/"
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
length = soup.select("tbody tr")

pryxlist = []
for i in range(len(length)):
    typ = str(i+1)
    ip = soup.select("tbody tr:nth-of-type("+typ+") td")[0]
    port = soup.select("tbody tr:nth-of-type("+typ+") td")[1]
    pryxlist.append(ip.getText() + ':' + port.getText())


def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib2.ProxyHandler({'http': pip})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req=urllib2.Request('https://www.omdbapi.com/')  # change the URL to test here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:
        print "ERROR:", detail
        return True
    return False

def main():
    socket.setdefaulttimeout(120)

    # two sample proxy IPs
    proxyList = pryxlist

    for currentProxy in proxyList:
        if is_bad_proxy(currentProxy):
            print "Bad Proxy %s" % (currentProxy)
        else:
            print "%s is working" % (currentProxy)

if __name__ == '__main__':
    main()
