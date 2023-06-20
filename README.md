# Tasks API

Tasks API is a playground project where I have developed a simple service that allows
authentication, storing to-do tasks, and modifying/creating/deleting such tasks.

# Usage

This server supports several API requests such as: 
1. Registration.
2. Authorization.
3. Displaying the list of tasks, and some basic CRUD operations.

To register a new user, you need to send a `POST` request to http://127.0.0.1:8000/api/v1/auth/users/. In the body of the 
request you must specify two fields `username` and `password`. Optionally, you can specify an `email` address.

Then you can login by sending a `POST` request to the address http://127.0.0.1:8000/auth/token/login/. In the body of the
request be sure to add the `username` and `password` keys. If the registration was successful, then the token key will be returned
to you as a response in the form of a JSON string.

Now to get a list of cases you need to send a `GET` request to the address http://127.0.0.1:8000/api/v1/task/. Additionally, in the 
request header you must add the "Authorization" key and the value must contain your token.

For example: `Authorization Token 6d7d2cd50989db8369791c4dca239241eff4da18.` 

If you want to know more, change or delete a task, at the end of the request you must specify the `id` of the task you need. 
For example: http://127.0.0.1:8000/api/task/69/

To read an entry, use a `GET` request, to update `PUT`, and to delete use `DELETE`. 
You also need to specify your token, so that the system understands that this is your account.

# Local development

Dear developer, before testing and making changes to the project, do not forget to download all the necessary libraries 
for correct work. After everything is set up to run the project, the file **manage.py** is distributed 
in the main directory. 

To deploy the changes locally, in the terminal enter
the command `python3 manage.py runserver` and after that you will start the local server. It is also necessary to migrate 
all databases that are present in the project. To do this, enter `python3 manage.py makemigrations` in the terminal. 

Then enter the following command `python3 manage.py migrate`. Next, you need to create a superuser so that you can easily 
work with the django admin panel.

If you want to disable the local server, then press the key combination `ctrl + c`.

## Good luck:)
