from flask import Blueprint
from flask_restful import Api

from .auth import GenerateTokenResource
from .dislike import DisLikesResource, DisLikeResource
from .like import LikesResource, LikeResource
from .profile import ProfileResource, ProfilesResource
from .user import UsersResource, UserResource
from .post import PostsResource, PostResource


api_bp = Blueprint('api', __name__, url_prefix="/api")
api = Api(api_bp)


api.add_resource(UsersResource, '/users', endpoint="users_list")
api.add_resource(UserResource, '/users/<int:user_id>', endpoint="users_details")

api.add_resource(PostsResource, '/posts', endpoint="posts_list")
api.add_resource(PostResource, '/posts/<int:post_id>', endpoint="posts_details")

api.add_resource(ProfilesResource, '/profiles', endpoint="profiles_list")
api.add_resource(ProfileResource, '/profile/<int:user_id>', endpoint="profile_details")

api.add_resource(LikesResource, '/likes', endpoint="likes_list")
api.add_resource(LikeResource, '/like/<int:like_id>', endpoint="like_details")

api.add_resource(DisLikesResource, '/dislikes', endpoint="dislikes_list")
api.add_resource(DisLikeResource, '/dislike/<int:dislike_id>', endpoint="dislike_details")

api.add_resource(GenerateTokenResource, '/generate-token', endpoint='generate_token')
