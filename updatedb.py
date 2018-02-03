import MySQLdb

conn = MySQLdb.connect(host= "localhost",
                       user= "root",
                       passwd="",
                       db="shouldwatch")
x = conn.cursor()
numb = 4439
arr = []

with open('movieVideoLinks.txt') as fl:
    for line in fl:
        arr.append(line)



for i in range(0,len(arr)):
    try:
        x.execute("""UPDATE movies SET movie_video='%s' WHERE id=%s """ % (arr[i],numb))
        conn.commit()
    except:
        conn.rollback()
        print 'error'
    numb-=1

conn.close()
                      
