# 📘 Project: HBNB

---

## 📝 Introduction

> ✍️ As part of this project, we undertook the reproduction of the Airbnb website — renamed here as "Hbnb".
>
> The goal of this work is to clearly and structurally represent the internal functioning of the application from a technical point of view.
> The diagrams created allow us to visualize interactions between the system components, data flows, and expected behaviors of both users and the system.
>
> The main types of diagrams included in this project are:
> - Package Diagram
> - Class Diagram
> - Sequence Diagram

---

## 🔹 Part 1: *Title of the first part*



---

## 🔹 Part 2: Class Diagram

This class diagram presents the different classes of the Hbnb website. You can visualize how the site is structured into four main classes, each with a specific role.

Let's go through the classes shown in this diagram:

First, the `BaseModel` class contains several useful methods that most other classes will use. It holds an ID that every class inherits to uniquely identify its instances, along with CRUD methods: Create, Read, Update, and Delete.

The `User` class contains all information about users of the website. Some of this data is very personal, such as email and password, which is why we made them private. With this class, any user can register, and update or delete their first name, last name, email, and password. We also included an administrator identifier, so the website owner can modify the Hbnb website when logged in.

The `Place` class handles information about the places listed on the website. Each place includes multiple attributes: title, description, location (latitude and longitude), owner, and amenities (note that amenities belong to the `Amenity` class). Each of these attributes can be created, updated, deleted, or listed.

The `Review` class manages messages and ratings that users can leave for places. It includes the place, the user, a rating, and a comment. Just like the `Place` class, all of these fields can be created, updated, deleted, or listed.

Finally, the `Amenity` class contains all the available amenities for places listed on Hbnb. It includes the name and description of the amenity. These fields also support create, update, delete, and list operations.

### Relationships between classes:
- `User`, `Place`, and `Amenity` have **association** relationships. For example, a user can have several places, but a place belongs to only one user.
- Between `Place` and `Review`, there's a **composition** relationship — if a place is deleted, all its associated reviews are also deleted.
- The relation between `BaseModel` and all other classes is a **generalization** — all classes inherit from `BaseModel`.

---

## 🔹 Part 3: Sequence Diagrams

---

The following sequence diagrams show the interactions between the different layers of the application in different scenarios.

### 1. Listing Places

<img width="720" height="456" alt="diagramme-sequence_list_place drawio_720" src="https://github.com/user-attachments/assets/e8088316-0109-44f4-9a0f-425a7d5669ca" />

In this sequence diagram, the user searches for places.
They first send a read request to the API, which then asks the business logic layer to search for the corresponding data.
The business logic layer then queries the database. Once the data is found, it's returned all the way back to the user as a list.

---

### 2. Creating a Place

<img width="720" height="570" alt="diagramme-sequence_place_creation drawio_720" src="https://github.com/user-attachments/assets/b21bcc85-595d-42a7-ae61-f0c6258d64ba" />

In this sequence diagram, the user creates a new place.
They first send a creation request to the API, which validates the data through the business logic layer.
If the data already exists in the database, it's returned to the user.
If not, the data is saved, the business logic layer validates the new place, and the API confirms its creation.

---

### 3. Registering a New User

<img width="720" height="570" alt="diagramme-sequence_register drawio_720" src="https://github.com/user-attachments/assets/43c38b1a-5de0-43fa-b987-435aec6e0bf5" />

In this diagram, the user creates a new account.
The user sends a creation request to the API, which checks the validity of the data via the business logic layer.
If the user already exists in the database, the existing data is returned.
Otherwise, the new data is saved, the business logic layer confirms the new user, and the API finalizes the creation.

---

### 4. Submitting a Review

<img width="720" height="456" alt="diagramme-sequence_review_submit drawio_720" src="https://github.com/user-attachments/assets/e7ce1833-6236-47f3-8489-8d6f76e627ff" />

In this diagram, the user submits a review.
They send a creation request to the API, which validates the data via the business logic layer.
The business logic layer asks the database to save the review, confirms the creation, and the API returns the result to the user.

---

## ✅ Conclusion

This project allowed us to better understand the internal architecture of a platform like Airbnb, through the modeling of its components and data flows.
Using UML diagrams, we were able to clearly express the system's structure, logic, and interactions.
This approach is essential for building scalable, maintainable, and well-documented applications.

---

## ✉️ Authors

- [@niimatik](https://github.com/niimatik)
- [@GuillaumeLerayGirardeau](https://github.com/GuillaumeLerayGirardeau)
- [@](https://github.com/)
