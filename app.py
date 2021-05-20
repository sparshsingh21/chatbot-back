from flask import Flask,jsonify, request
import time
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def response():
   jsonResponse = request.get_json()
   if jsonResponse["query"].lower() == "hi":
       result = "Hello"
   elif jsonResponse["query"].lower() == "how are you?":
       result = "I'm good, how are you?"
   elif jsonResponse["query"].lower() == "i am fine":
       result = "That's great!"
   elif jsonResponse["query"].lower() == "what is the time now?":
       result = "Current time is " + time.ctime()
   elif jsonResponse["query"].lower() == "what is your age?":
       result = "I am just a session old xD"
   elif jsonResponse["query"].lower() == "bye":
       result = "It was nice talking to you. GoodBye :)"

   return jsonify({"response":result})


if __name__ == "__main__":
    app.run(debug=True)



