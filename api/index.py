from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Post
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
api = Api(app)
db.init_app(app)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

# class Posts(Resource):
#     def get(self):
#         posts = Post.query.all()
#         if not posts:
#             return make_response({'error': 'No posts found'}, 404)
#         return make_response(posts.to_dict(),200)
    
#     def post(self):
#         new_post = Post()
#         data = request.get_json()

#         try:
#             for key in data:
#                 setattr(self, key, data[key])
#             db.session.add(new_post)
#             db.session.commit()
#             return make_response(new_post.to_dict(), 201)
#         except ValueError as error:
#             new_error = {"error": str(error)}
#             return make_response(new_error, 400)

# api.add_resource(Posts, "/posts")    