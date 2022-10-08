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

    print(User.query.all())
    #[<User u'admin'>, <User u'guest'>]
    print(User.query.filter_by(first_name='Bob').first())
    # <User u'admin'>

    query = User.query
    resultSet = query.all()
    results = list(map(lambda u:
                   {'id': u.id, 'firstName': u.first_name, 'lastName': u.last_name, 'email': u.email},
                   resultSet))
    return results


def get_posts():
    print("get_posts")

    query = Category.query.options(joinedload('posts'))
    for category in query:
        print(category, category.posts)

    py = Category.query.filter_by(name='Python').first()

    query = Post.query.with_parent(py).filter(Post.title != "Snakes")
    resultSet = query.all()

    print(resultSet)

    query = Post.query.options(joinedload('category'))
    resultSet = query.all()
    results = list(map(lambda u:
                       {'id': u.id, 'title': u.title, 'body': u.body, 'category': u.category.name},
                       resultSet))
    return results

