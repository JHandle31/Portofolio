import requests, json, os, time

start = time.time()

filename = 'D:\Official-movie-file2.json'
with open(filename) as data_file:
    files = json.load(data_file)

ef = open('D:/Errors2.txt', 'a')

for i in range(len(files)):
    title = '+'.join(files[i]['Title'].split(' '))
    year = files[i]['Released']
    url = 'http://theapache64.xyz:8080/movie_db/search?keyword=%s+%s' %(title, year)
    res = requests.get(url)

    x = res.json()
    try:
        print x['data']['imdb_id']
        files[i]['imdb-id'] = x['data']['imdb_id']
    except:
        print 'Error'
        ef.write(title.encode('utf-8') + ' ' + year + ' ' + files[i]['MovieId'] + '\n')


os.remove(filename)
ef.close()
with open (filename, 'w') as f:
    json.dump(files, f, indent=4)

print 'Done --------- %s seconds ---------' % (time.time() - start)
