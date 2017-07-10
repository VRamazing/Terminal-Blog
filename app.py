from models.posts import Post
from database import Database

__author__ = "vignesh Ramesh"

Database.initialize()

post1 = Post("First","This is the first post","Vignesh Ramesh")
post2 = Post("Second","This is the second post","Vignesh Ramesh")

print(post1.content)

print(post2.content)