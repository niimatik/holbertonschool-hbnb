from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True,
                             description='Latitude of the place'),
    'longitude': fields.Float(required=True,
                              description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True,
                             description="List of amenities ID's")
})


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        # Placeholder for the logic to register a new place
        place_data = api.payload
        new_place = facade.create_place(place_data)
        return {
            'id': new_place.id,
            'title': new_place.title,
            'description': new_place.description,
            'price': new_place.price,
            'latitude': new_place.latitude,
            'longitude': new_place.longitude,
            'owner_id': new_place.owner_id,
        }, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        # Placeholder for logic to return a list of all places
        all_places = facade.get_all_places()
        place_list = []
        for i in all_places:
            place_list.append({
                "id": i.id,
                "title": i.title,
                "latitude": i.latitude,
                "longitude": i.longitude
            })
        return place_list, 200


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Placeholder for the logic to retrieve a place by ID
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        owner_data = facade.get_user(place.owner_id)
        amenities_list = []
        for i in place.amenities:
            name_amenity = facade.get_amenity(i)
            amenities_list.append({
                "id": i,
                "name": name_amenity.name
            })
        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": place.owner_id,
                "first_name": owner_data.first_name,
                "last_name": owner_data.last_name,
                "email": owner_data.email
            },
            "amenities": amenities_list
        }, 200


    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Placeholder for the logic to update a place by ID
        place_data = api.payload
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        facade.update_place(place_id, place_data)
        return {"message": "Place updated successfully"}, 200


    @api.expect(amenity_model)
    @api.response(404, 'Place not found')
    @api.response(404, 'Amenity not found')
    @api.response(200, 'Amenity added successfully')
    def post(self, place_id):
        """Add a new amenity"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        amenity = api.payload
        all_amenities = facade.get_all_amenities()
        for i in all_amenities:
            if i.name == amenity["name"]:
                place.add_amenity(i.id)
                return {"message": "Amenity added successfully"}, 200
        return {"error": "Amenity not found"}, 404
