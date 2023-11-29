from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def main():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to the Fun Flask App!</title>
        <style>
            body {
                font-size: 24px;
                background-color: #d1b3ff; /* Light purple background */
                color: #333; /* Text color */
                margin: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Fun Flask App!</h1>
    </body>
    </html>
    """)

@app.route('/custom-greeting/<name>')
def playful_greeting(name):
    return render_template_string(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello, {name}!</title>
        <style>
            body {{
                font-size: 24px;
                background-color: #d1b3ff; /* Light purple background */
                color: #333; /* Text color */
                margin: 20px;
            }}
        </style>
    </head>
    <body>
        <p>Hello, {name}! Welcome to the headintheclouds playground of our Flask app. Ready for some fun?</p>
    </body>
    </html>
    """, name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
