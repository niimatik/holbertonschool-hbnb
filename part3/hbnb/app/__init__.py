from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def create_app(config_class="config.DevelopmentConfig"):
    from app.api.v1.users import api as users_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.reviews import api as reviews_ns
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0',
              title='HBnB API',
              description='HBnB Application API',
              doc='/api/v1/')
    bcrypt.init_app(app)

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')

    # Register the amenities namespace
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    # Register the places namespace
    api.add_namespace(places_ns, path='/api/v1/places')

    # Register the reviews namespace
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
