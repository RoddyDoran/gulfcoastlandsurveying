from flask import Flask, request, jsonify, redirect, url_for
import subprocess
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16 MB

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'
    return

@app.route('/process-payment', methods=['POST'])
def process_payment():
    amount = request.form['amount']
    
    payload = f'card_source=INTERNET&amount={int(float(amount) * 100)}&card_number=4012000098765439&exp_month=12&exp_year=2025&cvv=999'
    
    conn = http.client.HTTPSConnection("testapi.payarc.net")
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxNjQ4NSIsImp0aSI6IjE5ZjdmMTI1MmEzNDg0NTc4OTMwYWE2Y2VhYTFiNzdmNWVmNGUxZTQ2NWIwY2ZmMDgwYjdmMDYwODUxYWNkNGY1Y2I4NmE4M2RjMmE2MTcwIiwiaWF0IjoxNzEyNzkzNTAwLCJuYmYiOjE3MTI3OTM1MDAsImV4cCI6MTg3MDQ3MzUwMCwic3ViIjoiMzM3NjUiLCJzY29wZXMiOiIqIn0.W4lOdTAIeU7rF-lXWoHnyhVXAgmkPm8j_P3V3jvD3GLjgQP61isMA6ZtBzVKbgUWCE7h-8XkgU1_2x6T4NImVqLqf4drtU-CL1w_qTF54gC1YdPfHnUInsiG14dZ3m2k0HgM_GfE7rcUTqVr-RLPGZCDzfrljmdu5S9pgFM_bEt-QFpFo5D829hqS3gIAzavg8pgV8lcJaAj_qJOAWZozts5a8a9MbSSF6PdubJrfJjL9X87BEbx14EahpCbfkkcX7eDD9T_SGuxU0GcexsMpm3mFSxMF2VFFdWCIh5lAn-DL7DBNqXE0wKJgQ5eafW9t4ywN-iLzbxxDddAn7uMaby8MCw3KqSG24z8JMR3exr2FhSI4a1SqT21CYfo0RM9XpQ9wkqAe9HSfYzQ4xGHxCHbez0Vuu98zxXUndMcLLCG-_ZeVFDBgvkaeiaTzHvxObtO_h2KHXVNl5PBNn7t81DHWtf9SysXgZBqZZYkFKNX92iVA2Dwh6WepzpAg73ixGJzAN_XYfR_M3L5dLVPwSjLFAIqRHR5HrE6RRqFraBhtmt0zIggi7GNgaebEbWbnEGaDC6zn6XXeEZT17EQPkU1wM4rGzGEBjl5HrAr7R4EDX0stYHMqkN7TM6hQ9Qbn8mSc8hicRtPA92cVeiJDEHmN0OmvymxOPnLHbfwLwk'
    }
    
    conn.request("POST", "/v1/tokens", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

    # Call the C# script
    csharp_script_path = "/path/to/csharp/script"
    result = subprocess.run(["dotnet", csharp_script_path, token, card_data["email"]], capture_output=True, text=True)
    
    return jsonify({"result": result.stdout})

if __name__ == '__main__':
    app.run(debug=True)

