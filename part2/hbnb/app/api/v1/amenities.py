from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        # Placeholder for the logic to register a new amenity
        amenity_data = api.payload
        existing_amenity = facade.get_all_amenities()
        for i in existing_amenity:
            if amenity_data['name'] == i['name']:
                return {'error': 'amenity already exist'}, 400
        if type(amenity_data['name']) is not str:
            return {'error': 'input data is invalid'}, 400
        new_amenity = facade.create_amenity(amenity_data)
        return {'id': new_amenity.id, 'name': new_amenity.name}, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        # Placeholder for logic to return a list of all amenities
        return facade.get_all_amenities(), 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        # Placeholder for the logic to retrieve an amenity by ID
        list_amenity = facade.get_all_amenities()
        for i in list_amenity:
            if amenity_id == i['id']:
                return facade.get_amenity(amenity_id), 200
        return {'error': 'Amenity not found'}, 404

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        # Placeholder for the logic to update an amenity by ID
        amenity_data = api.payload
        if type(amenity_data['name']) is not str:
            return {'error': 'input data is invalid'}, 400
        list_amenity = facade.get_all_amenities()
        for i in list_amenity:
            if amenity_id == i['id']:
                return facade.update_amenity(amenity_id), 200
        return {'error': 'Amenity not found'}, 404
