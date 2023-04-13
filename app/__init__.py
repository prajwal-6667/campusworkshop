"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq51pmbg5e4khqnno0-a.oregon-postgres.render.com",
        database="todo_bezp",
        user="root",
        password="rG7E7WSNmgONqYchN35JfPYaSZ89VwQl")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
