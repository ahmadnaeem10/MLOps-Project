# tests/test_routes.py
import pytest
from app import create_app, db
from app.models import User
from flask_login import login_user
from werkzeug.security import generate_password_hash
import json

@pytest.fixture
def app():
    app = create_app('testing')  # Assuming 'testing' config for test environment
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_db():
    # Create a new database for testing and add test users
    db.create_all()

    # Add a test user for login
    user = User(username='testuser', password=generate_password_hash('password'))
    db.session.add(user)
    db.session.commit()

    yield db  # Allows tests to run

    # Drop all tables after the tests
    db.session.remove()
    db.drop_all()


# Test for Home route (Requires Login)
def test_home_page(client, init_db):
    # Log in the test user
    user = User.query.filter_by(username='testuser').first()
    login_user(user)

    response = client.get('/home')
    assert response.status_code == 200
    assert b'Welcome to the Weather Prediction App' in response.data  # Adjust as per your page content


# Test for User Registration
def test_register(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert b'Register' in response.data  # Make sure the register page is loading correctly

    # Test POST request for registration
    response = client.post('/register', data={
        'username': 'newuser',
        'password': 'newpassword'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Your account has been created!' in response.data
    assert User.query.filter_by(username='newuser').first() is not None


# Test for User Login
def test_login(client, init_db):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data  # Ensure login page loads correctly

    # Test unsuccessful login
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'wrongpassword'
    })
    assert b'Login unsuccessful' in response.data

    # Test successful login
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'password'
    }, follow_redirects=True)
    assert b'Welcome to the Weather Prediction App' in response.data


# Test for User Logout
def test_logout(client, init_db):
    # Log in the user first
    user = User.query.filter_by(username='testuser').first()
    login_user(user)

    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome to the Weather Prediction App' in response.data  # Assuming home page shows this


# Test for Weather Prediction
def test_predict(client, init_db):
    # Log in the user first
    user = User.query.filter_by(username='testuser').first()
    login_user(user)

    # Mock the model prediction
    response = client.post('/predict', data={
        'feature1': 25.0,
        'feature2': 15.0
    })

    assert response.status_code == 200
    assert b'Predicted Temperature' in response.data  # The page should show prediction text
