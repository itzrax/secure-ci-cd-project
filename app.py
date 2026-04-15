from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Secure CI/CD Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
                padding-top: 80px;
            }

            .card {
                background: #1e293b;
                padding: 30px;
                margin: auto;
                width: 400px;
                border-radius: 12px;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.4);
            }

            .status {
                font-size: 22px;
                margin-top: 15px;
                color: #22c55e;
                font-weight: bold;
            }

            button {
                margin-top: 20px;
                padding: 10px 20px;
                border: none;
                background: #3b82f6;
                color: white;
                border-radius: 8px;
                cursor: pointer;
            }

            button:hover {
                background: #2563eb;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>🔐 Secure CI/CD System</h1>
            <p>DevSecOps Pipeline Dashboard</p>

            <div class="status">System Secure ✅</div>

            <button onclick="alert('Pipeline is monitored via GitHub Actions 🚀')">
                Check Pipeline Status
            </button>
        </div>
    </body>
    </html>
    """)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)