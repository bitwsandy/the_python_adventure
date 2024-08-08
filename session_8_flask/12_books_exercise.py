from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'reviews': []},
    {'id': 2, 'title': '1984', 'author': 'George Orwell', 'reviews': []}
]

@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_id = len(books) + 1
        new_book = {
            'id': new_id,
            'title': request.form['title'],
            'author': request.form['author'],
            'reviews': []
        }
        books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add_book.html')

@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book_details(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if request.method == 'POST':
        review = request.form['review']
        book['reviews'].append(review)
        return redirect(url_for('book_details', book_id=book_id))
    return render_template('book_details.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)
