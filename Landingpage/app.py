from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-scraper', methods=['POST'])
def run_scraper():
    try:
        data = request.get_json()
        url = data.get('url', '')  # Extract the URL from the request data
        if not url:
            return jsonify({'error': 'No URL provided'}), 400

        # Ensure the correct path to websc.py
        result = subprocess.run(['python', 'C:\\Users\\ANUSHKA PANDEY\\Downloads\\Vastra_main\\Vastra-master\\Landingpage\\websc.py', url], capture_output=True, text=True)
        output = result.stdout
        if result.stderr:
            output += '\nError: ' + result.stderr
        return jsonify({'output': output, 'error': result.stderr})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
