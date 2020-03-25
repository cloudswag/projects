from flask import Flask, render_template, jsonify, request, make_response
from flask_api import status

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    some_json = request.get_json()
    return jsonify({"you sent" : some_json}), 201
  else:
    return jsonify({"main" : "code screen"})

@app.route("/fib/<int:num>", methods=["GET"])
def fib(num): 
  number_type = float(num)
  if number_type >= 0:
    if num == 0:
      fibs_list = [0]
    elif num == 1:
      fibs_list = [1]
    elif num > 1:
      fibs = [0, 1] 
      fibs_list = fibs + [fibs.append(fibs[i-1]+fibs[i-2]) for i in range(2,(num))]*0
    return jsonify({"result" : fibs_list}), 200
  else:
    my_resp = make_response("Error Non Postive Number!")
    my_resp.status_code = 403
    return my_resp

if __name__ == "__main__":
  app.run(debug=True, port=8080)