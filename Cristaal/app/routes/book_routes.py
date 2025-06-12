from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Book
from .. import db

book_bp = Blueprint('books', __name__, url_prefix='/api/books')

@book_bp.route('/', methods=['GET'])
@jwt_required()
def get_books():
    user_id = get_jwt_identity()
    books = Book.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": b.id, "title": b.title, "author": b.author} for b in books])

@book_bp.route('/', methods=['POST'])
@jwt_required()
def add_book():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], user_id=user_id)
    db.session.add(new_book)
    db.session.commit()
    return jsonify(message='Book created'), 201

@book_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_book(id):
    user_id = get_jwt_identity()
    book = Book.query.filter_by(id=id, user_id=user_id).first()
    if not book:
        return jsonify(message='Book not found'), 404
    data = request.get_json()
    book.title = data['title']
    book.author = data['author']
    db.session.commit()
    return jsonify(message='Book updated'), 200

@book_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    user_id = get_jwt_identity()
    book = Book.query.filter_by(id=id, user_id=user_id).first()
    if not book:
        return jsonify(message='Book not found'), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify(message='Book deleted'), 200
