from flask import Flask
app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return 'Welcome to the Home Page!'

# About page route
@app.route('/about')
def about001():
    return 'This is the About page.'

# Contact page route
@app.route('/contact')
def contact001():
    return 'Contact us at: contact@example.com'

if __name__ == '__main__':
    app.run(debug=True)
