# LIBRARY-SYSTEM

A simple DDS system designed using django and mySql

Required
1. package: pymysql and mysqlclient
2. local mySql server

Steps to run the code:
create a schema - library_system
navigate to project folder and run the below commands:
python manage.py migrate --- creates the necessary tables according to described model
python manage.py runserver

application is accessible at : http://localhost:8000/library_system/

