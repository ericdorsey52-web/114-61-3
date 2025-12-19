# blog/models/post.py
# This file contains the Post model for the blog application.
# Placeholder implementation using a simple class.

class Post:
    """
    A simple Post model representing a blog post.
    Attributes:
        id: Unique identifier for the post
        title: Title of the post
        content: Content of the post
        author: Author of the post
        created_at: Creation timestamp
    """
    def __init__(self, id, title, content, author, created_at=None):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.created_at = created_at or "2023-01-01"  # Placeholder timestamp

    def __str__(self):
        return f"Post(id={self.id}, title='{self.title}', author='{self.author}')"

# Example usage:
# post = Post(1, "My First Post", "This is the content.", "Author Name")
# print(post)