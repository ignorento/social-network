from flask import request, jsonify
from flask_restful import Resource
from app import db
from app.models import Dislike
from app.schemas import DisLikeSchema
from app.services import DislikeService

dislike_service = DislikeService()


class DisLikesResource(Resource):
    def get(self):
        ordered_user = request.args.get('user_id', type=bool)
        ordered_post = request.args.get('post_id', type=bool)
        ordered_create = request.args.get('create_at', type=bool)

        dislikes_query = db.session.query(Dislike)
        if ordered_user:
            dislikes_query = dislikes_query.order_by(Dislike.user_id.asc())

        elif ordered_post:
            dislikes_query = dislikes_query.order_by(Dislike.post_id.asc())

        elif ordered_create:
            dislikes_query = dislikes_query.order_by(Dislike.create_at.desc())

        dislikes = dislikes_query.all()
        return jsonify(DisLikeSchema().dump(dislikes, many=True))

    def post(self):
        json_data = request.get_json()

        post_id = json_data['post_id']
        user_id = json_data['user_id']

        dislike = db.session.query(Dislike).filter(Dislike.user_id == user_id, Dislike.post_id == post_id).first()

        if dislike:
            response = jsonify(error="Dislike already set")
            response.status_code = 400
            return response

        dislike_new = dislike_service.create(**json_data)

        response = jsonify(DisLikeSchema().dump(dislike_new, many=False))
        response.status_code = 201

        return response


class DisLikeResource(Resource):
    def get(self, dislike_id=None):
        dislike = dislike_service.get_by_id(dislike_id)
        return jsonify(DisLikeSchema().dump(dislike, many=False))

    def delete(self, dislike_id=None):
        status = dislike_service.delete(dislike_id)
        return jsonify(status=status)
