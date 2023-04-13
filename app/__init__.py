"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq5ondvk4rjsva0qd0-a.oregon-postgres.render.com",
        database="todo_x2s9",
        user="todo_x2s9_user",
        password="13cFypW1vSvl9mkJ3PzUwibqdOONd7pW")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
