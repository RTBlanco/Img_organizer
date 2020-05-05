# Image Organizer 

import os, time, shutil

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

 
try:    # tries to creaste new file it already exits continues on 
    os.mkdir(os.path.join(desktop,'Images'))
except FileExistsError:
    pass

while True:
    files = os.listdir(desktop)

    for item in files:
        if item.endswith(('png','jpg','jpeg')):
            # Gets the last time the file was modified
            file_time = time.strftime("%a-%d-%m-%Y", time.localtime(os.path.getmtime(os.path.join(desktop, item))))
            
            if not os.path.exists(os.path.join(desktop, 'Images', file_time)): # Checks if sub folder exits, creates one if False 
                current_date = time.strftime("%a-%d-%m-%Y", time.localtime())
                os.mkdir(os.path.join(desktop, 'Images', current_date))
                shutil.move(os.path.join(desktop, item), os.path.join(desktop,'Images',current_date, item))
            else:
                shutil.move(os.path.join(desktop, item), os.path.join(desktop,'Images',file_time, item))

