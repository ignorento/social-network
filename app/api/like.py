from flask import request, jsonify

from flask_restful import Resource

from app import db
from app.models import Like
from app.schemas import LikeSchema
from app.services import LikeService

like_service = LikeService()


class LikesResource(Resource):
    def get(self):
        ordered_user = request.args.get('user_id', type=bool)
        ordered_post = request.args.get('post_id', type=bool)
        ordered_create = request.args.get('create_at', type=bool)

        likes_query = db.session.query(Like)
        if ordered_user:
            likes_query = likes_query.order_by(Like.user_id.asc())

        elif ordered_post:
            likes_query = likes_query.order_by(Like.post_id.asc())

        elif ordered_create:
            likes_query = likes_query.order_by(Like.create_at.desc())

        likes = likes_query.all()
        return jsonify(LikeSchema().dump(likes, many=True))

    def post(self):
        json_data = request.get_json()

        post_id = json_data['post_id']
        user_id = json_data['user_id']

        like = db.session.query(Like).filter(Like.user_id == user_id, Like.post_id == post_id).first()

        if like:
            response = jsonify(error="Like already set")
            response.status_code = 400
            return response

        like_add = like_service.create(**json_data)

        response = jsonify(LikeSchema().dump(like_add, many=False))
        response.status_code = 201

        return response


class LikeResource(Resource):
    def get(self, like_id=None):
        like = like_service.get_by_id(like_id)
        return jsonify(LikeSchema().dump(like, many=False))

    def delete(self, like_id=None):
        status = like_service.delete(like_id)
        return jsonify(status=status)
