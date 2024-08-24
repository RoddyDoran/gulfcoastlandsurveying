from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/process-payment', methods=['POST'])
def process_payment():
    card_data = request.form
    token_response = generate_token(card_data)
    
    token = token_response["token_id"]

    # Call the C# script
    csharp_script_path = "/path/to/csharp/script"
    result = subprocess.run(["dotnet", csharp_script_path, token, card_data["email"]], capture_output=True, text=True)
    
    return jsonify({"result": result.stdout})

if __name__ == '__main__':
    app.run(debug=True)

