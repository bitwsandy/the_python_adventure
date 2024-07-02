from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    # Passing 'name' variable to the template
    return render_template('index1.html', name='Visitor')

if __name__ == '__main__':
    app.run(debug=True)
