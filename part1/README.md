# 📘 Projet : *Titre de votre projet*

---

## 📝 Introduction

> ✍️ **Décrivez ici l'objectif du projet, son contexte et les motivations.**
>
> Par exemple : Ce projet a été réalisé dans le cadre de [...]. Il a pour but de [...].

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

## 🔹 Partie 3 : *Titre de la troisième partie*

> 🎯 **Objectif :**
>
> Mettez en avant les résultats, les tests ou les fonctionnalités clés finalisées ici.

### 📈 Résultats / Sorties attendues :

- Résultat A
- Résultat B
- Résultat C

---

## ✅ Conclusion

> 📌 **Résumé du projet, des enseignements tirés, et des perspectives éventuelles.**
>
> Mentionnez les limites, les améliorations possibles, ou les suites prévues du projet.

---

## ✉️ Contact

> Pour toute question, contactez : **[Votre Prénom Nom]**  
> 📧 Email : `votre.email@example.com`

























Dans ce diagramme de sequence l'utilistateur recherche des lieux.
Il fait d'abord la demande a l'API de lire les donnés l'API demande au businessligic layer de chercher les donnés correspondantes.
Ensuite le business logic layer demande a la data base de lire les donnés une fois trouver il les renvois jusqu'a l'utilisateur sous forme de liste.

Dans ce diagramme de sequence l'utilisateur créer un lieu.
Il fait d'abord un appelle API de création puis l'API valide les donnés au près du businesslogic layer qui recherche les donnés dans la database si elle existe il renvoie les donner a l'utilisateur 
et si elle n'existe pas il save les donner puis le businesslogic layer valide le lieux et l'API a créer le lieux.

Dans ce diagramme de sequence l'utilisateur créer un nouveau compte.
Il fait d'abord un appelle API de création puis l'API valide les donnés au près du businesslogic layer qui recherche les donnés dans la database si elle existe il renvoie les donner a l'utilisateur 
et si elle n'existe pas il save les donner puis le businesslogic layer valide le compte et l'API le créer.

Dans ce diagramme de sequence l'utilisateur créer une review.
Il fait d'abord un appelle API de création puis l'API valide les donnés au près du businesslogic layer qui demande a la database de save les donner puis le businesslogic layer valide la review et l'API la créer.
