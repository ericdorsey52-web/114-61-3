# app.py
# Main Flask application for the simple blog.
# This file sets up the Flask app, registers routes, and runs the server.

from flask import Flask
from blog.views.blog_views import index, post_detail

app = Flask(__name__, template_folder='blog/templates')

# Register routes
@app.route('/')
def home():
    return index()

@app.route('/post/<int:post_id>')
def post(post_id):
    return post_detail(post_id)

if __name__ == '__main__':
    app.run(debug=True)