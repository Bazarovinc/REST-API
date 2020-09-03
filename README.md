# REST-API
## How to start server
When you clone repo. Change directory for test_api:
```
$>cd test_api
```
Then just run server:
```
$>python manage.py runserver
```
Copy adress, that will be writen after message: "Starting development server at".
<img align="center" src="https://github.com/Bazarovinc/REST-API/blob/master/imagies/example.jpg" width="100%" />
## How to use API
### To get info about all users
* Make GET-request on http://127.0.0.1:8000/api/users
### To get info about one user
* Make GET-request on http://127.0.0.1:8000/api/users/id, where id - int, id of user
### To create new user
* Make POST-request on http://127.0.0.1:8000/api/users, with next message:
```
{
    "user":
        {
            "name": "Nikita",
            "x": 1,
            "y": 1,
            "description": "First user"
        }
}
```
### To change some info of user
* Make PUT-request on http://127.0.0.1:8000/api/users/id, where id - int, id of user, with some messgae like this:
```
{
    "user":
        {
            "x": 5,
            "y": 3,
        }
}
```
### To delete user
* Make DELETE-request on http://127.0.0.1:8000/api/users/id, where id - int, id of user.
### To find K users in M killimetres around point with coordinates (x, y)
* Make GET-request on http://127.0.0.1:8000/api/search, with message like this:
```
{
    "search":
    {
        "x": 0,
        "y": 0,
        "k": 5,
        "m": 10
    }
}
```
