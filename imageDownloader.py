import bs4, requests, json, os, re
from threading import Thread
import subprocess

with open('D:\Official-movie-file.json') as data_file:
    files = json.load(data_file)

print len(files)



def downloadImage(part,totalParts):
    start = (len(files) / totalParts) * part
    finish = ((len(files) / totalParts) * (part+1) - 1)
    print start,finish ,'\n'
    for i in range(start,finish):
        MovId = re.sub('\W+','',files[i]['MovieId'])
        try:
            url = files[i]['ImgUrls']
        except:
            print('Error')
            errors = open('Errors.txt','a')
            errors.write(MovId)
            errors.write('\n')
            errors.close()
        try:
            res = requests.get(url)
            print('Downloading image %s... %s' % (url,part))
            try:
                imageFile = open(os.path.join('Movie-posters-official', MovId) + '.jpg', 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
            except:
                errors = open('Errors.txt','a')
                errors.write('Error on' + str(i))
                errors.close()
        except:
            print 'Error in movie number %s with movieId %s and the url %s' % (i, MovId, url)

def downloadImageBackdrop(part,totalParts):
    start = (len(files) / totalParts) * part
    finish = ((len(files) / totalParts) * (part+1) - 1)
    print start,finish ,'\n'
    for i in range(start,finish):
        MovId = re.sub('\W+','',files[i]['MovieId'])
        try:
            url = files[i]['BackdropUrls']
        except:
            print('Error')
            errors = open('Errors.txt','a')
            errors.write(MovId)
            errors.write('\n')
            errors.close()
        for j in range(len(url)):
            try:
                res = requests.get(url[j])
                print('Downloading image %s... %s' % (url[j],part))
                try:
                    imageFile = open(os.path.join('Movie-backdrops-official', MovId) + '_bdrop' + str(j) + '.jpg', 'wb')
                    for chunk in res.iter_content(100000):
                        imageFile.write(chunk)
                    imageFile.close()
                except:
                    errors = open('Errors.txt','a')
                    errors.write('Error on' + str(i))
                    errors.close()
            except:
                print 'Error in movie number %s with movieId %s and the url %s' % (i, MovId, url) 


threads = []
totalParts = 8

for i in range(totalParts+1):
    t = Thread(target=downloadImageBackdrop, args=(i, totalParts))
    threads.append(t)

for x in threads:
    x.daemon = True
    x.start()
    

for x in threads:
    x.join()
