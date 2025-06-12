import pytest
from app import create_app, db

@pytest.fixture(scope='module')
def test_client():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test_biblofast.db",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "JWT_SECRET_KEY": "clave-super-secreta-test"
    }

    app = create_app(test_config=test_config)

    with app.app_context():
        db.create_all()  # crea las tablas de cero solo para test
        yield app.test_client()
        db.session.remove()
        db.drop_all()
