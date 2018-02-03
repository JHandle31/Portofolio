from PIL import Image
from PIL import ImageFile
import progressbar
from time import sleep
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os, time
bar = progressbar.ProgressBar(maxval=100, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
start = time.time()
dirName = 'D:/xampp/htdocs/Cool/movieImages/'
dirName2 = 'D:/xampp/htdocs/Cool/movieImages_med/'
x = os.listdir(dirName)
size = 280, 400
for i in range(len(x)):
    im = Image.open(dirName + x[i])
    im.thumbnail(size)
    im.save(dirName2 + x[i], optimize=True, quality=60)
    bar.update((i / float(len(x))) * 100)

    sleep(0.1)
    
bar.finish()
print '------Done in %s seconds------' % (time.time() - start)
