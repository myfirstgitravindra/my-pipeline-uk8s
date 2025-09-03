from flask import Flask, render_template_string

app = Flask(__name__)

# Prod version - Green theme
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>My App - PROD Environment</title>
    <style>
        body { 
            background: linear-gradient(135deg, #0ba360 0%, #3cba92 100%);
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
        h1 { color: #fff; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        .version { 
            background: #ff9a3c; 
            padding: 10px; 
            border-radius: 5px; 
            margin: 20px 0;
        }
        .badge {
            background: #e74c3c;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 12px;
            margin-left: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>✅ Production Environment <span class="badge">LIVE</span></h1>
        <div class="version">
            <h2>Version: PROD-1.0.0</h2>
        </div>
        <p>This is the production version of our application</p>
        <p>Running on: Python Flask</p>
        <p>Status: <strong>Stable & Live</strong></p>
        <p>🛡️ Enterprise Grade | 📈 High Availability</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)