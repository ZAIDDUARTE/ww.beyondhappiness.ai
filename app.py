from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# The HTML and JavaScript are embedded directly in the Python file using render_template_string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot Interface</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        textarea, button, pre {
            display: block;
            margin: 10px;
        }
    </style>
</head>
<body>
    <h1>Test Beyond Happiness API</h1>
    <textarea id="query" placeholder="Enter your query here..."></textarea><br>
    <button id="send">Send Request</button>
    <h2>Response:</h2>
    <pre id="response"></pre>

    <script>
        document.getElementById('send').onclick = async () => {
            const query = document.getElementById('query').value;
            const responseArea = document.getElementById('response');
            responseArea.textContent = 'Loading...';

            try {
                const response = await fetch('/api/request', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ query })
                });
                
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }

                const data = await response.json();
                // Display only the response content
                responseArea.textContent = data.response || 'No response content available.';
            } catch (error) {
                responseArea.textContent = `Error: ${error.message}`;
            }
        };
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    # Render the HTML template with JavaScript included in the same route
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/request', methods=['POST'])
def api_request():
    data = request.get_json()
    query = data.get('query')

    # Example API request to an external service
    try:
        external_response = requests.post('https://staging.beyondhappiness.ai/request_bookenabled_message/', 
                                          json={"query": query}, 
                                          headers={
                                              'Accept': 'application/json',
                                              'Content-Type': 'application/json'
                                          })
        external_response.raise_for_status()  # Raise error for bad responses
        return jsonify(external_response.json())  # Return the external API's response
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
