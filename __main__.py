import os
from pathlib import Path



main_repo = "C:/Users/Nate/Desktop/travis_docs"






#ask for date range
from datetime import date

today = str(date.today())
print("Today's date:", today)




#create repository
if not os.path.isdir(main_repo):
    os.makedirs(main_repo)
os.chdir(main_repo)

if not os.path.isdir(main_repo + "/" + today):
    os.makedirs(main_repo+"/"+today)



#navigate to emails
#addres:      nate.travis.testing@gmail.com
#password:    dickbutt2




#parse emails/download attachments

