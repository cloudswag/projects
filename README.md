Dell Sample Code Screen

# Test Cases 
Create a RESTFUL Service The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. I.e. given n = 5, appropriate output would represent the sequence [0, 1, 1, 2, 3]. 

Given a negative number, it will respond with an appropriate error. 

# Requirements
Python version 3.8.1 
Flask 
Flask API 
Jsonify

# Procedures
$ brew install python3 pip3 
$ pip3 install flask
$ pip3 install flask_api 
$ pip3 install jsonify 
$ cd projects * once git cloned proceed to the project directory *
$ python3 restapi_service.py

*Output after Rest Service Started*

Serving Flask app "restapi_service" (lazy loading) Environment: production WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. Debug mode: on Running on http://127.0.0.1:8080/ (Press CTRL+C to quit) Restarting with stat Debugger is active! Debugger PIN: 103-764-124 


$ open http://localhost/8080 
$ curl -X POST http://localhost:8080/fib/5

# Test Case 1
The REST service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. I.e. given n = 5, appropriate output would represent the sequence [0, 1, 1, 2, 3]. -- Enter http://localhost:8080/fib/{number} 

---- example in the POST URL should be curl -X POST http://localhost:8080/fib/5 
---- output will be as follows: { "result": [ 0, 1, 1, 2, 3 ] }

# Test Case 2
Errors when entering a negative number should be as follows:

<title>404 Not Found</title>
