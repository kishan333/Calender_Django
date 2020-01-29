# Calender_Django
step 1: Make one folder and copy it or clone in that folderand also install virtualenv is system.(pip install virtualenv)
step 2: Create virtual enviourment.(virtualenv <enviourment_name> e.g. virtualenv venv)
step 3: Go inside the folder and install requirement.txt file.(pip install -r requirement.txt)
step 4: Go inside the calender_project folder open setting.py file and change Database config as per your requirements.(e.g. my database is mysql ,you can use other also.)
step 5: Come out to main folder where manage.py file is and run folloing command.
      ----- python manage.py makemigratios
      ----- python manage.py migrate
      ----- python manage.py runserver


After this command url will come like http://127.0.0.1/8000 go to that url and you will check the output.

In admin path only admin can go login and check the functionality.
To login process you need to create user follow the following command.
  ----- python manage.py createsuperuser
  Insert admin name
  Insert email-id (you can also leave it if you want)
  Insert Strong password and agian enter same in next field.
  -- now your user is craeted go and check the url and enter calender_event you want.
  
  go to (http://127.0.0.1/8000/calender) this path login with your created user and event check the output.
  
  Thank you to checkout my project.
  If you have any query please add in issues i'll try solve your querys, Thank You.
