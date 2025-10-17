# HBnB Part 2 

This directory contains all the task 2 of the HBnB project. You will find down below eplanations about the purpose of all directories and files, a complete description of the core business logic classes, as well as example of uses and instructions to run the application correctly. 

## Table of Contents

- [Overall project description](#overall-project-description)

**About the projects :**

- [Software and Language](#software-and-language)
- [Authors](#authors)

## Overall project description

 - **Project Structure**

The HBnB project is composed of several directories and sub-directories, each of them having a precise role in the application's works.  
Here is a simple representation of the purpose of each directory :

|   File/Directory       |   Description                                                                                    |
|------------------------|--------------------------------------------------------------------------------------------------|
| `app/`                 | Contains the core application code.                                                              |
| `api/`                 | Houses the API endpoints, organized by version.                                                  |
| `models/`              | Contains the business logic classes.                                                             |
| `services/`            | Implements the Facade pattern to manage interaction between layers.                              |
| `persistence/`         | Contains the in-memory repository; will later be replaced by a SQL Alchemy-based solution.       |
| `run.py`               | Entry point for running the Flask application.                                                   |
| `config.py`            | Used for configuring environment variables and application settings.                             |
| `requirements.txt`     | Lists all the Python packages required for the project.                                          |
| `README.md`            | Provides a brief overview of the project.                                                        |

- **Run the application**

To run properly the HBnB application, be sure to follow these steps correctly :
- Install the required packages contained in *requirements.txt* :
````
pip install -r requirements.txt
````
- Run the application by executing *run.py* :
````
python3 run.py
````
This project use Python3, you may want to have a similar version of Python to avoid errors.

## Core Business Logic Classes

In the *models* folder, you can found all the different entities that compose the core of the HBnB website. You can found down below the description of each of them, with a representation of their attributes, methods and relationships.

### Base Class

This entity contains all attributes and methods that will be the common ground of all the other entities. Every following classes will inherit from *Base Class*.

- **Attributes**

| Name         | Type       | Description                                                            |
|--------------|------------|------------------------------------------------------------------------|
| `id`         | `UUID`     | A unique identifier (UUID) automatically generated for each instance   |
| `created_at` | `datetime` | Timestamp indicating when the object was created                       |
| `updated_at` | `datetime` | Timestamp indicating the last time the object was updated              |

- **Methods**

| Name            | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `save()`        | Updates the `updated_at` timestamp to the current time                      |
| `update(data)`  | Updates the object's attributes using a dictionary                          |

### User

This entity define user's data and actions in the HBnB website.

- **Attributes**

| Name           | Type       | Description                                                                 |
|----------------|------------|-----------------------------------------------------------------------------|
| `first_name`   | `str`      | User's first name.                                                          |
| `last_name`    | `str`      | User's last name.                                                           |
| `email`        | `str`      | User's email address.                                                       |
| `is_admin`     | `bool`     | Indicates whether the user has administrative privileges.                   |
| `places`       | `list`     | List of places belonging to the user.                                       |
| `reviews`      | `list`     | List of reviews submitted by the user.                                      |

- **Methods**

| Name               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `add_places(place)`| Adds a place to the user's places list.                                     |
| `add_reviews(review)`| Adds a review to the user's reviews list.                                 |

- **Relationships**

| Related Entity | Relationship Type | Description |
|--------------------|-----------------------|------------------|
| `Place`            | One-to-Many           | A user can add multiple places|
| `Review`           | One-to-Many           | A user can add multiple reviews|

- **Example and usage**
````
# import the User class
from app.models.user import User

# create a user
user1 = User("Alice", "Dupont", "alice.dupont@example.com", is_admin=False)

# adding a place
user1.add_places("Holberton School")

# adding a review
user1.add_reviews("Great School !")
````

### Amenity

This entity define places's features such as Wi-Fi or TV. 

- **Attributes**

| Attribute   | Type   | Description                                                  |
|-------------|--------|--------------------------------------------------------------|
| `name`      | `str`  | The name of the amenity.                                     |
| `places`    | `list` | A list of places that offer this amenity.                    |

- **Methods**

| Method         |Description                                                   |
|----------------|--------------------------------------------------------------|
| `add_place(place)`    | Adds a place to the `places` list.                           |

- **Relationships**

| Related Entity     | Relationship Type     | Description |
|--------------------|-----------------------|------------------|
| `Place`            | Many-to-Many           | An amenity can be linked to multiple places that include this feature, and a place can have multiple amenities|

- **Example and usage**
````

# import the Amenity class
from app.models.amenity import Amenity

# create an amenity
wifi = Amenity("Wi-Fi")

# adding a place
wifi.add_place("Holberton School")
````

### Place

This entity define places' informations and adress, and contains owner's information as well as all the amenities it has.

- **Attributes**

| Attribute     | Type     | Description                                                                 |
|---------------|----------|-----------------------------------------------------------------------------|
| `title`       | `str`    | The title of the place.                                                     |
| `description` | `str`    | Description of the place.                                                   |
| `price`       | `float`  | Cost of the place.                                                          |
| `latitude`    | `float`  | Geographic latitude of the place.                                           |
| `longitude`   | `float`  | Geographic longitude of the place                                           |
| `owner_id`    | `str`    | Identifier of the user who owns the place.                                  |
| `amenities`   | `list`   | A list of amenities associated with the place.                              |
| `reviews`     | `list`   | A list of reviews submitted for the place.                                  |

- **Methods**

| Name               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `add_review(review)`| Adds a review to the `reviews` list.                                     |
| `add_amenity(amenity)`| Adds an amenity to the `amenities` list.                                  |

- **Relationships**

| Related Entity | Relationship Type | Description                                                                 |
|----------------|-------------------|-----------------------------------------------------------------------------|
| `Amenity`      | Many-to-Many      | A place can have multiple amenities. An amenity can be assigned to multiple places.|
| `Review`       | One-to-Many       | A place can receive multiple reviews.                                       |
| `User`         | Many-to-One       | Each place is owned by a single user.                                       |


- **Example and usage**
````
# import the Place class
from app.models.place import Place

# create a place
place1 = Place(
    title="Holberton School",
    description="A great school to learn Python",
    price=7450.0,
    latitude=48.117,
    longitude=-1.677,
    owner_id="01b254561r1238754"
)

# adding an amenity
place1.add_amenity("Free Wi-Fi")

# adding a review
place1.add_review("Loved the coffee")
````
### Review

This entity define review that can be assigned to places by the users of the application.

- **Attributes**

| Attribute   | Type     | Description                                           |
|-------------|----------|-------------------------------------------------------|
| `text`      | `str`    | The content of the review.                            |
| `rating`    | `int`    | The rating given by the user.                         |
| `place`     | `Place`  | The id of the place being reviewed.                   |
| `user`      | `User`   | The id of the user who submitted the review.          |

- **Relationships**

| Related Entity | Relationship Type | Description                                           |
|----------------|-------------------|-------------------------------------------------------|
| `Place`        | Many-to-One       | Each review is linked to one place.                   |
| `User`         | Many-to-One       | Each review is submitted by one user.                 |


- **Example and usage**
````
# import the Review class
from app.models.review import Review

# create a review
review1 = Review(
    text="Amazing School !",
    rating=5,
    place="fgdd8efsdsaz54tyuiok1bv",
    user="rhjiko5l423kn6fd45y"
)
````
