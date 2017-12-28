## Small Python Project

This is a simple project with python and flask, with implementation of tests using nose test, covering unit test.
I am also using docker to package the application inside a container, and make it portable to any other host.
The application is simple, it is an api that calculates the volume of cube and cylinders, passing the necessary parameters.

### Why flask?
Flask is an excellent web framework for making apis quickly and with few lines of code. For this example he is perfect. It has a very good flask based project called Sanic that supports async request and has a good perfomance. Other than the large number of questions in stackoverflow are 19,546 questions. Until now the community is still very active.

### Dependencies

- Python 2.7 >=
- Flask 0.12.2
- Pip 8.1.1 >=
- Nose 1.3.7
- Coverage 4.4.2
- Flask-restful 0.3.6

### Installation 

You need python 2.7>= and pip installed on your machine. With the two installed, run the command:

```
# pip install -r requirements.txt
```

And run:

```
# python run.py
```

To build a Docker image and execute the application inside the container, just run the command:

```
# docker build -t flask-app .
```


### View application

To view the running application go to:

http://localhost:5000/

In this small example, we have 3 endpoints:

Receives the parameter `side` 
 - GET http://localhost:5000/cube?side=10

Receives the parameter `radius` 
 - GET http://localhost:5000/cylinder?radius=10

Receives the parameter `radius` and `side`
 - GET http://localhost:5000/geometry?radius=10&side=10

If it does not pass the parameter it returns status 400 bad request

### Extras information
### Tests

To execute all test, run the comand:

```
# nosetests
```

### Tests Coverage

| Name        | Stmts         | Miss | Cover  |
| ----------- |:-------------:| ----:| ------:|
| app/\__init__.py            |  0  |    0 |  100% |
|app/api/\__init__.py        |  0  |    0 |  100% |
|app/api/cube.py            | 10  |   10 |    0% |
|app/api/cylinder.py        | 10  |   10 |    0% |
|app/api/geometry.py        | 12  |   12 |    0% |
|app/common/\__init__.py     |  0  |    0 |  100% |
|app/common/cube.py         |  2  |    0 |  100% |
|app/common/cylinder.py     |  3  |    0 |  100% |
|app/routes.py              | 12  |   12 |    0% |
|TOTAL                       |49   |  44  |  10% |

