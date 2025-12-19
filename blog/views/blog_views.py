# blog/views/blog_views.py
# This file contains the view functions for the blog application.
# Placeholder for routing and handling requests.

from flask import render_template, request
from blog.models.post import Post

# Placeholder list of posts (in a real app, this would be from a database)
posts = [
    Post(1, "Welcome to the Blog", "This is the first post.", "Admin"),
    Post(2, "Second Post", "Content for the second post.", "Author")
]

def index():
    """
    View function for the home page, displaying a list of posts.
    """
    return render_template('index.html', posts=posts)

def post_detail(post_id):
    """
    View function for displaying a single post.
    """
    post = next((p for p in posts if p.id == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404

# Note: In a Flask app, these would be decorated with @app.route
# For example:
# @app.route('/')
# def index():
#     ...

# @app.route('/post/<int:post_id>')
# def post_detail(post_id):
#     ...