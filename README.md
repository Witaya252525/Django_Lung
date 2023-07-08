# Django_Profile_July23
Install Python ( Where) add to path
check python active ==> Typing idle will lead to python shell   / if typing python is black color
https://pypi.org/search/?q=django
C:\Users\Lenovo>pip -V
pip 23.1.2 from C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
check  pip -v
sandbox = virtualenv
pip install virtualenv
สร้าง Folder  ของ website
cd folder python -m virtualenv venv(Name)
python -m virtualenv name of virtual env.

Born to dev Create folder /cd in folder_name  and  python -m --pip install --upgrade pip  for update  python on folder_name // next step is install virtual env // still stay in old folder typing virtualenv  -p python Project_name create virtual environment 
cd new Project name (Project-name) infront path  then acticate ....  ==>  .\Scripts\activate    ......จะได้ pip /setuptools/wheel  ...>>> pip install django /after installed test django-admin will see package  //   django-admin   startproject  store .  ( Activate Project_name)   
python manage.py runserver




C:\Users\Lenovo\OneDrive\WEBDEVELOP2023\Django_Lung>python -m virtualenv venv
C:\Users\Lenovo\OneDrive\WEBDEVELOP2023\Django_Lung>.\venv\scripts\activate
(venv) C:\Users\Lenovo\OneDrive\WEBDEVELOP2023\Django_Lung>pip install django
(venv) C:\Users\Lenovo\OneDrive\WEBDEVELOP2023\Django_Lung>

..............................................................................................................................................................................................................................................................
Project  who_witaya
App Home
........................................................................

(venv) C:\Users\Lenovo\OneDrive\WEBDEVELOP2023\Django_Lung\who_witaya\who_witaya>cd..

(venv) C:\Users\Lenovo\OneDrive\WEBDEVELOP2023\Django_Lung\who_witaya>python manage.py startapp home

(venv) C:\Users\Lenovo\OneDrive\WEBDEVELOP2023\Django_Lung\who_witaya>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
July 07, 2023 - 06:15:39
Django version 4.2.3, using settings 'who_witaya.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
...........................................................................................................................................................
(venv) C:\Users\Lenovo\OneDrive\WEBDEVELOP2023\Django_Lung\who_witaya>python manage.py migrate

(venv) C:\Users\Lenovo\OneDrive\WEBDEVELOP2023\Django_Lung\who_witaya> python manage.py createsuperuser
Username (leave blank to use 'lenovo'): admin
Email address: witayachai@gmail.com
Password:  12345678
Password (again):
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
