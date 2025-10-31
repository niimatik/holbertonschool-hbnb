--creation of the hbnb database
CREATE DATABASE IF NOT EXISTS hbnb_db;

USE hbnb_db;

CREATE TABLE IF NOT EXISTS users (
	id CHAR(36) PRIMARY KEY,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	email VARCHAR(255) UNIQUE,
	password VARCHAR(255),
	is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS places (
	id CHAR(36) PRIMARY KEY,
	title VARCHAR(255),
	description TEXT,
	price DECIMAL(10, 2),
	latitude FLOAT,
	longitude FLOAT,
	owner_id CHAR(36),
	FOREIGN KEY (owner_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS reviews (
	id CHAR(36) PRIMARY KEY,
	text TEXT,
	rating INT,
	user_id CHAR(36),
	place_id CHAR(36)
);

CREATE TABLE IF NOT EXISTS amenities (
	id CHAR(36) PRIMARY KEY,
	name VARCHAR(255) UNIQUE
);


CREATE TABLE IF NOT EXISTS place_amenity(
	place_id char(36),
	amenity_id char(36),
	PRIMARY KEY (place_id, amenity_id),
	FOREIGN KEY (place_id) REFERENCES places(id),
	FOREIGN KEY (amenity_id) REFERENCES amenities(id)
);
