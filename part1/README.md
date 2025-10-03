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

> 🎯 **Objectif :**
>
> Décrivez les aspects techniques ou fonctionnels abordés dans cette section.

### 🔧 Technologies / Méthodes utilisées :

- Technologie 1
- Méthode 2
- Outil 3

---

## 🔹 Partie 3 : Les diagrammes de sequences

---

### 1



Dans ce diagramme de sequence l'utilistateur recherche des lieux.
Il fait d'abord la demande a l'API de lire les donnés l'API demande au businessligic layer de chercher les donnés correspondantes.
Ensuite le business logic layer demande a la data base de lire les donnés une fois trouver il les renvois jusqu'a l'utilisateur sous forme de liste.

### 2



Dans ce diagramme de sequence l'utilisateur créer un lieu.
Il fait d'abord un appelle API de création puis l'API valide les donnés au près du businesslogic layer qui recherche les donnés dans la database si elle existe il renvoie les donner a l'utilisateur 
et si elle n'existe pas il save les donner puis le businesslogic layer valide le lieux et l'API a créer le lieux.

### 3



Dans ce diagramme de sequence l'utilisateur créer un nouveau compte.
Il fait d'abord un appelle API de création puis l'API valide les donnés au près du businesslogic layer qui recherche les donnés dans la database si elle existe il renvoie les donner a l'utilisateur 
et si elle n'existe pas il save les donner puis le businesslogic layer valide le compte et l'API le créer.

### 4



Dans ce diagramme de sequence l'utilisateur créer une review.
Il fait d'abord un appelle API de création puis l'API valide les donnés au près du businesslogic layer qui demande a la database de save les donner puis le businesslogic layer valide la review et l'API la créer.

## ✅ Conclusion

> 📌 **Résumé du projet, des enseignements tirés, et des perspectives éventuelles.**
>
> Mentionnez les limites, les améliorations possibles, ou les suites prévues du projet.

---

## ✉️ Author
