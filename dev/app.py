from flask import Flask, render_template_string

app = Flask(__name__)

# Dev version - Blue theme
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>My App - DEV Environment</title>
    <style>
        body { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: Arial, sans-serif; 
            margin: 0; padding: 40px; 
            color: white; text-align: center;
        }
        .container { 
            background: rgba(255,255,255,0.1); 
            padding: 30px; 
            border-radius: 15px;
            backdrop-filter: blur(10px);
            max-width: 600px; 
            margin: 0 auto;
        }
        h1 { color: #ff6b6b; margin-bottom: 20px; }
        .version { 
            background: #4ecdc4; 
            padding: 10px; 
            border-radius: 5px; 
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Development Environment</h1>
        <div class="version">
            <h2>Version: DEV-1.0.0</h2>
        </div>
        <p>This is the development version of our application</p>
        <p>Running on: Python Flask</p>
        <p>Status: <strong>Active Development</strong></p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)