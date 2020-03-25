Dell Sample Code Screen

Create a RESTFUL Service The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. I.e. given n = 5, appropriate output would represent the sequence [0, 1, 1, 2, 3]. Given a negative number, it will respond with an appropriate error. Tested on MAC Created on Python version 3.8.1 Install Python v3, Flask, Flask Api, Jsonify using brew

API Client tested using POSTMAN

Using VSCODE with Python and Flask plugins

Open the "restapi_serivce.py" to view the code and start the Flask service by Running the Python File in Terminal (Play button).

Output to Terminal Should be as follows as an example:

Serving Flask app "restapi_service" (lazy loading) Environment: production WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. Debug mode: on Running on http://127.0.0.1:8080/ (Press CTRL+C to quit) Restarting with stat Debugger is active! Debugger PIN: 103-764-124 Open Postman and using the GET request lets start with Test #1.

The web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0. I.e. given n = 5, appropriate output would represent the sequence [0, 1, 1, 2, 3]. -- Enter http://localhost:8080/fib/{number} ---- example in the GET URL should be http://localhost:8080/fib/5 ---- output will be as follows: { "result": [ 0, 1, 1, 2, 3 ] }

Errors when entering a negative number should be as follows:

<title>404 Not Found</title>
