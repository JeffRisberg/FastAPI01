from sqlalchemy.orm import joinedload

from .. import db
from .. models import User, Post, Category

def reset():
    print("reset")
    User.query.delete()

    admin = User(first_name='John', last_name = 'Smith', email = 'john.smith@gmail.com')
    guest = User(first_name='Bob',  last_name = 'Jones', email = 'bob.jones@gmail.com')

    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

    Post.query.delete()
    Category.query.delete()

    py = Category(name='Python')  # define this, write at end of session

    Post(title='Hello Python!', body='Python is pretty cool', category=py) #references category

    p = Post(title='Snakes', body='Ssssssss') # define this

    py.posts.append(p) # put this in the category

    db.session.add(py) # write the category
    db.session.commit()

    return ["done"]


def get_users():
    print("get_users")
    query = User.query
    resultSet = query.all()
    results = list(map(lambda u:
                   {'id': u.id, 'firstName': u.first_name, 'lastName': u.last_name, 'email': u.email},
                   resultSet))
    return results


def get_posts():
    query = Post.query.options(joinedload('category'))
    resultSet = query.all()
    results = list(map(lambda u:
                       {'id': u.id, 'title': u.title, 'body': u.body, 'category': u.category.name},
                       resultSet))
    return results

