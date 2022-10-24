from flask import Flask, request, abort
import logging

app = Flask(__name__)

@app.route('/')
def index():
    return "test"

"""
Test this route with test.py. The route receives a POST request, and prints the JSON data included. 
"""
@app.route('/hook', methods=['POST'])
def webhook():
    vals = []
    if request.method == 'POST':
        data = request.json
        
        # parses data from test.py, and adds test values to vals array
        for entry in data["data"]:
            vals.append(entry["val"])

        print(vals)
        return f'Your data was received: {vals}', 200
    else:
        abort(400)

"""
In order to expose route to web, need to use something like ngrok.
With ngrok, if server is running on port 5000, we use the command: "ngrok http 5000"
to generate a public URL. This public url can then be used to hit the flask endpoint.
"""
@app.route('/github', methods=['POST'])
def github_webook():
    print("works")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')