## Small Python Project

This is a simple project with python and flask, with implementation of tests using nose test, covering unit tests and integration test.
I am also using docker to package the application inside a container, and make it portable to any other host.

### Why flask?
Flask is an excellent web framework for making apis quickly and with few lines of code. For this example he is perfect. It has a very good flask based project called Sanic that supports async request and has a good perfomance. Other than the large number of questions in stackoverflow are 19,546 questions. Until now the community is still very active.

### Dependencies

- Python 2.7 >=
- Flask 0.12.2
- Pip 8.1.1 >=
- Nose 1.3.7
- Coverage 4.4.2

### Installation 

You need python 3.1+ and pip installed on your machine. With the two installed, run the command:

```
# pip install -r requirements.txt
```

And run:

```
# python run.py
```

To view the running application go to:

http://localhost/

### Extras information
### Tests

To execute all test, run the comand:

```
# nosetests
```

