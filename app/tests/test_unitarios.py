from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Book

def test_generate_password_hash():
    password = "1234"
    hashed = generate_password_hash(password)
    assert hashed != password

def test_check_password_hash():
    password = "1234"
    hashed = generate_password_hash(password)
    assert check_password_hash(hashed, password)

def test_book_instance():
    book = Book(title="Mi libro", author="Yo", user_id=1)
    assert book.title == "Mi libro"
    assert book.author == "Yo"
    assert book.user_id == 1
