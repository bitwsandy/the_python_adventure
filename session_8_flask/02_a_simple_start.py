from flask import Flask

app = Flask(__name__)  # Create an instance of the Flask class

@app.route('/')  # Define the route for the home page
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode


# from flask import Flask:
#       This imports the Flask class from the Flask module.
# app = Flask(__name__):
#       - Creates an instance of the Flask application.
#       - __name__ is a special variable in Python that is used by Flask to determine
#         the root path of the application.
# @app.route('/'):
#       - A decorator that tells Flask what URL should trigger the following function.
#         Here, / denotes the root URL.
# def home():
#       - Defines a function that is called when a user visits the home route.
#       - This function returns the text "Hello, World!" which will be displayed in
#         the user's browser.
# if __name__ == '__main__': :
#       - A Python best practice that ensures the app only runs when the script is
#         executed directly (not imported).
# app.run(debug=True):
#       - Starts the Flask application with the debugger enabled, which helps in the
#         development phase by providing detailed error messages and automatically
#         reloading your app when changes are made.
