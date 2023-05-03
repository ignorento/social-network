from flask import Blueprint
from flask_restful import Api
from .user import UsersResource, UserResource
from .post import PostsResource, PostResource


api_bp = Blueprint('api', __name__, url_prefix="/api")
api = Api(api_bp)


api.add_resource(UsersResource, '/users', endpoint="users_list")
api.add_resource(UserResource, '/users/<int:user_id>', endpoint="users_details")

api.add_resource(PostsResource, '/posts', endpoint="posts_list")
api.add_resource(PostResource, '/posts/<int:post_id>', endpoint="posts_details")

