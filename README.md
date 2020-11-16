# modec
The focus to this project is to do a simple REST api with some test case.


#how to run

#pre-requisites

python >= 3.4

#commands

pip install -r requirements.txt

python manage.py runserver

#to use a interface for testing purpose please do the following

#python manage.py createsuperuser

#python manage.py runserver

#http://localhost:8000/admin/


# points to the future

#the test cases were not that elaborated, so maybe there will be a bug or two

#the coverage is still bellow acceptance

#although the endpoint to get all the valid equipments by vessel is implemented, I forgot to write the test

# Security Concerns

#The security_key of my project was deployed here, i didn't bother put on my .env file to help those looking at this project, but in a real-life application, NEVER expose your security_key folks
