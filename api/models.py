from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, func
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin



metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    serialize_rules = ("-users.post",)

    @validates('post')
    def validate_post(self,key, post):
        if not post and not 1 <= post <= 600:
            raise ValueError
        return post
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True ,nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=func.now())
    
    @validates('username')
    def validate_username(self,key,username):
        if not username and not 1 <= username <= 20:
            raise ValueError
        return username

    @validates('password')
    def validate_password(self,key,password):
        if not password and not 6 <= password <= 20:
            raise ValueError
        return password
    
    @validates('email')
    def validate_email(self,key,email):
        if not email and not 5 <= email <= 30:
            raise ValueError
        return email
    
    @validates('firstname')
    def validate_firstname(self,key,firstname):
        if not firstname and not "":
            raise ValueError
        return firstname
    
   
class RePost(db.Model, SerializerMixin):
    __tablename__ = 'reposts' 
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    serialize_rules = ("-users.repost",)

class Like(db.Model, SerializerMixin):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    serialize_rules = ("-users.like",)
    