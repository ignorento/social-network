from flask_restful import Resource
from flask import request, jsonify

from app import db
from app.models import Profile
from app.schemas import ProfileSchema
from app.services import ProfileService

profile_service = ProfileService()


class ProfileResource(Resource):
    def get(self, user_id=None):
        profile = profile_service.get_by_id(user_id)
        return jsonify(ProfileSchema().dump(profile, many=False))

    def put(self, user_id=None):
        json_data = request.get_json()
        json_data['user_id'] = user_id

        profile_id = db.session.query(Profile.id).filter(Profile.user_id == user_id).scalar()
        json_data['id'] = profile_id

        profile = profile_service.update(json_data)
        return jsonify(ProfileSchema().dump(profile, many=False))


class ProfilesResource(Resource):
    def get(self):
        ordered = request.args.get('user_id', type=bool)

        profiles_query = db.session.query(Profile)
        if ordered:
            profiles_query = profiles_query.order_by(Profile.user_id.asc())

        profiles = profiles_query.all()
        return jsonify(ProfileSchema().dump(profiles, many=True))
