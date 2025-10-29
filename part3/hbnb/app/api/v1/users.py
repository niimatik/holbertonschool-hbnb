from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity


api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True,
                                description='First name of the user'),
    'last_name': fields.String(required=True,
                               description='Last name of the user'),
    'email': fields.String(required=True,
                           description='Email of the user'),
    'password': fields.String(required=True,
                              description='password of the user')
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        try:
            user_data = api.payload
            # Simulate email uniqueness check
            existing_user = facade.get_user_by_email(user_data['email'])
            if existing_user:
                return {'error': 'Email already registered'}, 400
            new_user = facade.create_user(user_data)
            return {'id': new_user.id,
                    'message': 'user successfully created'}, 201
        except Exception:
            return {"error": "Invalid input data"}, 400

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve a list of all users"""
        # Placeholder for logic to return a list of all amenities
        all_users = facade.get_all_users()
        user_list = []
        for user in all_users:
            user_list.append({
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            })
        return user_list, 200


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name,
                'last_name': user.last_name, 'email': user.email}, 200

    @api.expect(user_model)
    @api.response(200, 'user updated successfully')
    @api.response(404, 'user not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, user_id):
        """Update an user's information"""
        # Placeholder for the logic to update an user by ID
        try:
            current_user = get_jwt_identity()
            user_data = api.payload
            if "first_name" in user_data:
                if not user_data["first_name"]:
                    return {"error": "You must have a first name !"}, 400
            if "last_name" in user_data:
                if not user_data["last_name"]:
                    return {"error": "You must have a last name !"}, 400
            if "email" in user_data or "password" in user_data:
                return {'error': 'You cannot modify email or password.'}, 400
            user = facade.get_user(user_id)
            if not user:
                return {'error': 'user not found'}, 404
            if user.id != current_user:
                return {'error': 'Unauthorized action.'}, 403
            facade.update_user(user_id, user_data)
            return {'id': user.id, 'first_name': user.first_name,
                    'last_name': user.last_name, 'email': user.email}, 200
        except Exception:
            return {"error": "Invalid input data"}, 400
