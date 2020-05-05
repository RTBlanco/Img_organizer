#! usr/bin/env python3
# Image Organizer 

import os, datetime, time, shutil

# tries to creaste new file it already exits continues on 
try:
    os.mkdir('/home/ronny/Desktop/images')
except FileExistsError:
    pass

while True:
    files = os.listdir('/home/ronny/Desktop')

    for item in files:
        if item.endswith(('png','jpg','jpeg')):
            file_time = time.strftime("%a-%d-%m-%Y", time.localtime(os.path.getmtime(f'/home/ronny/Desktop/{item}')))

            if not os.path.exists(f'/home/ronny/Desktop/images/{file_time}'):
                current_date = time.strftime("%a-%d-%m-%Y", time.localtime())
                os.mkdir(f'/home/ronny/Desktop/images/{current_date}')
                shutil.move(f'/home/ronny/Desktop/{item}', f'/home/ronny/Desktop/images/{current_date}/{item}')
            else:
                shutil.move(f'/home/ronny/Desktop/{item}', f'/home/ronny/Desktop/images/{file_time}/{item}')

      




# use --> time.strftime("%a-%d-%m-%Y", time.localtime()) to get the current date 
