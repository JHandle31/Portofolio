import json, re
with open("movies.json","r") as add:
    json_data = json.load(add)
    print len(json_data)
    print json_data[1]['MovieId']
    for i in range(len(json_data)):
        json_data[i]['MovieId'] = re.sub('\W+','',json_data[i]['MovieId'])

with open('moviesOfficial2.json','w') as iets:
    iets.write(json.dumps(json_data) + '\n')
    
