from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/booktracker_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # "To Read", "Reading", "Finished"
    review = db.Column(db.Text, nullable=True)

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    books = Book.query.order_by(Book.id.desc()).limit(5).all()
    return render_template('home.html', books=books)

@app.route('/books')
def books():
    genre_filter = request.args.get('genre', None)
    if genre_filter:
        books = Book.query.filter_by(genre=genre_filter).all()
    else:
        books = Book.query.all()
    return render_template('books.html', books=books, genre_filter=genre_filter)

@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        status = request.form['status']
        review = request.form['review']

        new_book = Book(title=title, author=author, genre=genre, status=status, review=review)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('books'))
    return render_template('add_book.html')

@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        book.status = request.form['status']
        book.review = request.form['review']
        db.session.commit()
        return redirect(url_for('book_detail', book_id=book.id))
    return render_template('book_detail.html', book=book)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['query']
        books = Book.query.filter(Book.title.ilike(f"%{search_query}%") | Book.author.ilike(f"%{search_query}%")).all()
        return render_template('search.html', books=books, query=search_query)
    return render_template('search.html', books=[], query="")

if __name__ == "__main__":
    app.run(debug=True)