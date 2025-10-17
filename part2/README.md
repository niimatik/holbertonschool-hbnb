# HBnB Part 2 

This directory contains all the task 2 of the HBnB project. You will find down below eplanations about the purpose of all directories and files, a complete description of the core business logic classes, as well as example of uses and instructions to run the application correctly. 

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
| `delete()`      | Deletes the current object                                                  |

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
