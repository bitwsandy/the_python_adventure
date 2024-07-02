from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data: List of dictionaries, each representing a book
books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'genre': 'Fiction'},
    {'title': 'The Grapes of Wrath', 'author': 'John Steinbeck', 'genre': 'Fiction'},
    {'title': 'Silent Spring', 'author': 'Rachel Carson', 'genre': 'Non-fiction'},
    {'title': 'The Gene', 'author': 'Siddhartha Mukherjee', 'genre': 'Non-fiction'}
]

@app.route('/', methods=['GET', 'POST'])
def home():
    genre_query = request.form.get('genre')  # Get the genre from the form input
    if genre_query:
        # Filter books that match the genre query
        filtered_books = [book for book in books if genre_query.lower() == book['genre'].lower()]
        return render_template('index2.html', books=filtered_books, genre=genre_query)
    return render_template('index2.html', books=books, genre='')

if __name__ == '__main__':
    app.run(debug=True)
