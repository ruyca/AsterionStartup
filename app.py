from flask import Flask, request, jsonify
from flask_cors import CORS
from buisiness_analysis import query_chatgpt, preprocess_string
import json

# Create the Flask app
app = Flask(__name__)
CORS(app)

# Define a route for POST requests
@app.route('/', methods=['POST'])
def process_data():
    # Check if request content type is JSON
    if request.is_json: 
        # Parse JSON data from the request
        data = request.get_json()

        # Extract data fields
        q1 = data.get("q1")
        q2 = data.get("q2")
        q3 = data.get("q3")
        q4 = data.get("q4")
        q5 = data.get("q5")
        
        # Call the query_chatgpt function with the extracted data
        result = query_chatgpt(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
        processed_result = preprocess_string(result)

        json_data = json.loads(processed_result)
        # Return the result as JSON
        return json_data, 200
    else:
        # Return an error if request is not JSON
        return jsonify({"error": "Request must be JSON"}), 400

# Start the Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
