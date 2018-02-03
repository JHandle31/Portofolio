import MySQLdb, json

db = MySQLdb.connect("localhost","root","","shouldwatch")
db.set_character_set('utf8')
cursor = db.cursor()

with open('D:/Official-movie-file_2.json') as data_file:
    data = json.load(data_file)


#movie_id = 
#movie_title = 2
#movie_story = 3
#movie_genre = 4
#movie_metaScore = 5
#movie_released = 6
#movie_actors = 7
#movie_runtime = 8
#movie_backdrop = 9
for i in range(len(data)):
    movie_id = data[i]['MovieId']
    movie_title = data[i]['Title']
    movie_story = data[i]['Story']
    movie_genre = ', '.join([str(x) for x in data[i]['Genres']])
    
    try:
        movie_metaScore = data[i]['metascore']
    except:
        movie_metaScore = 0
        
    movie_released = data[i]['Released']
    movie_actors = ', '.join([str(x.encode('utf-8')) for x in data[i]['Actors']])
    
    try:
        movie_runtime = data[i]['runtime']
    except:
        movie_runtime = 'NA'

    movie_backdrops = len(data[i]['BackdropUrls'])
        
    print (movie_title.encode('utf-8'))

    cursor.execute("""INSERT INTO movies (
movie_id,
movie_title,
movie_story,
movie_genre,
movie_metaScore,
movie_released,
movie_actors,
movie_runtime,
movie_backdrops) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                   (movie_id,movie_title,movie_story,movie_genre,movie_metaScore,movie_released,movie_actors,movie_runtime,movie_backdrops))
    db.commit()


db.close()
