import json, requests, os

with open('D:\ToSort\Spiders\imdbScaper\imdbScaper\spiders/MoviesIMDB.json') as data_file:
    data = json.load(data_file)

for i in range(0,len(data)):
    try:
        url = data[i]['Poster'].split('.')[:-2]
        res = requests.get('.'.join(url) + '.jpg')
        print('Downloading image %s...' % str(data[i]['MovieId']) + '_poster.jpg')
        imageFile = open(os.path.join('ImagesIMDB', str(data[i]['MovieId'])) + '_poster.jpg', 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    except:
        print 'Could not download image %s' % (str(data[i]['MovieId']) + '_poster.jpg')
        
    

    
    
                     
