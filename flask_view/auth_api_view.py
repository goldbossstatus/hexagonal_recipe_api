from api.api_interfaces import IAuthAPI
from flask import request, jsonify, Flask


class AuthView:
    def __init__(self,
                 app: Flask,
                 auth_api: IAuthAPI,):

        @app.route('/api/v1/authenticate', methods=['POST'])
        def authenticate():
            user_id = request.form.get('user_id')
            password = request.form.get('password')
            r = auth_api.authenticate(user_id=user_id, password=password)
            return jsonify({'result': r}), 200

        @app.route('/api/v1/revoke/<string:jwt_token>', methods=['PUT'])
        def revoke(jwt_token):
            user_id = request.form.get('user_id')
            password = request.form.get('password')
            r = auth_api.revoke(user_id=user_id, password=password, jwt_st=jwt_token)
            return jsonify({'result': r})

        @app.route('/api/v1/is-authenticated/<string:jwt_token>', methods=['GET'])
        def is_authenticated(jwt_token):
            r = auth_api.is_authenticated(jwt_token)
            return jsonify({'result': r})

        # todo implement after expiration logic is done
        # @app.route('/api/v1/is-expired/str:jwt_token>', methods=['GET'])
        # def is_expired(jwt_token):
        #     r = auth_api.is_expired(jwt_st=jwt_token)
        #     return jsonify({'result': r})
