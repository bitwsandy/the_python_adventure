from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # HTML form and template string
    html_form = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Username Form</title>
    </head>
    <body>
        <h1>Submit your username</h1>
        <form method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username">
            <button type="submit">Submit</button>
        </form>
        {% if username %}
            <h2>Hello, {{ username }}!</h2>
        {% endif %}
    </body>
    </html>
    '''

    if request.method == 'POST':
        username = request.form.get('username')
        return render_template_string(html_form, username=username)
    return render_template_string(html_form, username=None)

if __name__ == '__main__':
    app.run(debug=True)
