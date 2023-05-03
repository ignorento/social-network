from flask import request, jsonify
from app import db
from app.models import Post
from app.schemas import PostSchema
from flask_restful import Resource

from app.services import PostService

post_service = PostService()

class PostsResource(Resource):
    def get(self):
        """
        Постьі все или все конкретного автора
        """
        author_id = request.args.get("author_id", type=int)

        query = db.session.query(Post)

        if author_id:
            query = query.filter(Post.author_id == author_id)

        posts = query.all()

        return jsonify(PostSchema().dump(posts, many=True))

    def post(self):
        json_data = request.get_json()
        post = post_service.create(**json_data)

        response = jsonify(PostSchema().dump(post, many=False))
        response.status_code = 201

        return response



class PostResource(Resource):
    def get(self, post_id=None):
        post = post_service.get_by_id(post_id)
        return jsonify(PostSchema().dump(post, many=False))

    def put(self, post_id=None):
        json_data = request.get_json()
        json_data['id'] = post_id
        # ищем author_id нашего поста
        author_id = db.session.query(Post.author_id).filter(Post.id == post_id).scalar()
        # перезаписіваем author_id если вдруг ктото его изменил
        json_data['author_id'] = author_id

        post = post_service.update(json_data)
        return jsonify(PostSchema().dump(post, many=False))

    def delete(self, post_id=None):
        status = post_service.delete(post_id)
        return jsonify(status=status)
