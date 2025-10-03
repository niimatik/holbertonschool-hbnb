# 📘 Projet : HBNB

---

## 📝 Introduction

> ✍️ Dans le cadre de ce projet, nous avons entrepris la reproduction du site Airbnb — renommé ici "Hbnb".
>
> Ce travail a pour objectif de représenter de manière claire et structurée le fonctionnement interne de l’application, d'un point de vue technique.
> Les diagrammes produits permettent de visualiser les interactions entre les composants du système, les flux de données, ainsi que les comportements attendus des utilisateurs et le système.
>
> Les principaux types de diagrammes abordés dans ce projet incluent :
> - Le diagramme de package
> - Le diagramme de classes
> - Le diagramme de séquence

---

## 🔹 Partie 1 : *Titre de la première partie*

> 🎯 **Objectif :**
>
> Expliquez ce que cette partie couvre, les étapes ou les modules concernés.

### ✅ Détails :

- Élément 1
- Élément 2
- Élément 3

---

## 🔹 Partie 2 : *Titre de la deuxième partie*

This class diagram presents the differents classes of the HbnB website. You can now visualise how the website is composed into four different classes, each of them having a specific role in the website structure.


Let's have a quick review of the different classes on this diagram :

First, the Base Model call contains a bunch of usefull methods that most of other classes will use. It contains an ID that every class will have to identify them, alongside the CRUD methods : Create, Read, Update and Delete.

The User class will contain all the informations about each users of the website. Some of these data are very personnal, such as the user email or password, and this is why we decided to make these informations private. With this class, any user can register, and update or delete their first name, last name, email and password. We also included an administrator idendificator, so the website owner can modifiy the HbnB website when connected.

The Place class will handle informations about places available on the website. Each places gather a bunch of information : title, description, place, location (latitude and longitude), owner and amenities (note that the amenites available for each places are part of the Amenity class). Each of these information can be created, updated, deleted or listed.

The Review class will concern messages and notes each user of HbnB can give to a place. It contains a place, a user, a rating and a comment. Such as the Place class, each of these attributes can be created, updated, deleted or listed.

Last but not least, the Amenity class contains all the aminities available for each places on HbnB. It contains the name and the description of the amenity. These two attributes can also be created, updated, deleted or listed.

Concerning the relations between each classes, User, Place and Amenity got an Association relation. For example, a user can have several place, but one place only belong to one user.
The relation between Place and Review is a Composition relation, meaning that if the place is deleted, every review related to this place will also be deleted.
The relation between the Base Model and all the other classes si a Generalisation relation, meaning that all classes inherits from the Base Model class.

---

## 🔹 Partie 3 : Les diagrammes de sequences

---

### 1

<img width="720" height="456" alt="diagramme-sequence_list_place drawio_720" src="https://github.com/user-attachments/assets/e8088316-0109-44f4-9a0f-425a7d5669ca" />


Dans ce diagramme de sequence l'utilistateur recherche des lieux.
Il fait d'abord la demande a l'API de lire les donnés l'API demande au businessligic layer de chercher les donnés correspondantes.
Ensuite le business logic layer demande a la data base de lire les donnés une fois trouver il les renvois jusqu'a l'utilisateur sous forme de liste.

### 2

<img width="720" height="570" alt="diagramme-sequence_place_creation drawio_720" src="https://github.com/user-attachments/assets/b21bcc85-595d-42a7-ae61-f0c6258d64ba" />


Dans ce diagramme de sequence l'utilisateur créer un lieu.
Il fait d'abord un appelle API de création puis l'API valide les donnés au près du businesslogic layer qui recherche les donnés dans la database si elle existe il renvoie les donner a l'utilisateur
et si elle n'existe pas il save les donner puis le businesslogic layer valide le lieux et l'API a créer le lieux.

### 3

<img width="720" height="570" alt="diagramme-sequence_register drawio_720" src="https://github.com/user-attachments/assets/43c38b1a-5de0-43fa-b987-435aec6e0bf5" />


Dans ce diagramme de sequence l'utilisateur créer un nouveau compte.
Il fait d'abord un appelle API de création puis l'API valide les donnés au près du businesslogic layer qui recherche les donnés dans la database si elle existe il renvoie les donner a l'utilisateur
et si elle n'existe pas il save les donner puis le businesslogic layer valide le compte et l'API le créer.

### 4

<img width="720" height="456" alt="diagramme-sequence_review_submit drawio_720" src="https://github.com/user-attachments/assets/e7ce1833-6236-47f3-8489-8d6f76e627ff" />


Dans ce diagramme de sequence l'utilisateur créer une review.
Il fait d'abord un appelle API de création puis l'API valide les donnés au près du businesslogic layer qui demande a la database de save les donner puis le businesslogic layer valide la review et l'API la créer.

## ✅ Conclusion

> 📌 **Résumé du projet, des enseignements tirés, et des perspectives éventuelles.**
>
> Mentionnez les limites, les améliorations possibles, ou les suites prévues du projet.

---

## ✉️ Author

- [@niimatik](https://github.com/niimatik)
- [@GuillaumeLerayGirardeau](https://github.com/GuillaumeLerayGirardeau)
- [@](https://github.com/)
