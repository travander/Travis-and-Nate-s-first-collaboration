import os
from pathlib import Path
import ezgmail
from datetime import date
#pip install --user --upgrade ezgmail

main_repo = "C:/Users/Nate/Desktop/travis_docs"
project_location = "C:/Users/Nate/Documents/GitHub/Travis-and-Nate-s-first-collaboration"






#ask for date range
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

os.chdir(project_location)
ezgmail.init()


print('Access Granted, reading emails:', '\r\n','\r\n')

threads = ezgmail.search('security')
#print(threads[0])


ezgmail.summary(threads)
#['tulips.jpg', 'canal.jpg', 'bicycles.jpg']
#threads[0].messages[0].downloadAttachment('tulips.jpg')
#threads[0].messages[0].downloadAllAttachments(downloadFolder='vacation2019')


#parse emails/download attachments

