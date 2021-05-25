from flask import Flask,jsonify, request
from flask_cors import CORS
import time
app = Flask(__name__)
CORS(app)

@app.route('/bot', methods=['POST'])
def response():
   jsonResponse = request.get_json()
   if jsonResponse["query"].lower() == "hi":
       result = "Hello"
   elif "how are you" in jsonResponse["query"]:
       result = "I'm good, how are you?"
   elif "fine" in jsonResponse["query"] or "good" in jsonResponse["query"]:
       result = "That's great!"
   elif "time" in jsonResponse["query"]:
       result = "Current time is " + time.ctime()
   elif "your age" in jsonResponse["query"]:
       result = "I am just a session old xD"
   elif "bye" in jsonResponse["query"]:
       result = "It was nice talking to you. GoodBye :)"
   elif "your height" in jsonResponse["query"]:
       result = "I dont have height"
       
   else:
       result = "Sorry I didn't get that."

   return jsonify({"response":result})


if __name__ == "__main__":
    app.run(debug=True)
