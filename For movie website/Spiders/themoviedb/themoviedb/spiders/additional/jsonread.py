import requests, os, json, threading
if not os.path.exists('moviesImage2'):
    os.makedirs('moviesImage2')

with open('moviesOfficial2.json') as data_file:
    data = json.load(data_file)

def DownloadImage(piece,pieces):
    for i in range( (len(data)*piece/pieces) + 1, len(data) ):
        for j in range(len(data[i]['ImgUrls'])):
            pcurl = data[i]['ImgUrls'][j]
            print data[i]['ImgUrls'][j]
            res = requests.get(pcurl)
            imageFile = open(os.path.join('moviesImage2', data[i]['MovieId'] + '_' + str(j) + '.jpg'),'wb')
            print 'Downloaded %s...' % data[i]['MovieId'] + str(j) + '.jpg'
            print 'Thread %s' % piece
            print 'I = %s' % i
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        if i == (len(data)*piece/pieces):
            break
try:
    num0 = threading.Thread(target=DownloadImage, args=(0,6))
    num1 = threading.Thread(target=DownloadImage, args=(1,6))
    num2 = threading.Thread(target=DownloadImage, args=(2,6))
    num3 = threading.Thread(target=DownloadImage, args=(3,6))
    num4 = threading.Thread(target=DownloadImage, args=(4,6))
    num5 = threading.Thread(target=DownloadImage, args=(5,6))
    
    num0.start()
    num1.start()
    num2.start()
    num3.start()
    num4.start()
    num5.start()

    num0.join()
    num1.join()
    num2.join()
    num3.join()
    num4.join()
    num5.join()
except:
    print "Unable to start thread"

while 1:
    pass
#No such file or directory u'3:11072_0.jpg
#The24356_1.jpg was the picture before this one
#Probably the :
