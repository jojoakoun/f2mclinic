# f2mclinic

# Requirements
Créer une application Customer Relationship Management pour la clinique F2M.


## Les entités
 * les utilisateurs: Défini toute personne membre de la clinique F2M et qui a accès à l'application
 * Les Entreprises: Sont les entreprises qui ont signé un contract avec la clinique F2M
 * Les fiches patients: Sont les données des personnes travaillant dans les entreprises et qui viennent au cabinet pour leur bilan et consultation
 * Les résultats de test: Le bilan médical du patient
 * Les questionnaires: Liste des questionnaires qu'un patient doit remplir avant bilan médical

## Les actions
  Il sera possible d'effectuer plusieurs actions definies ci dessous:
   - Créer, modifier un utilisateur (1)
   - Consulter un utilisateur (2)
   - supprimer un utilisateur (3)
   - Assigner un profil à un utilisateur (4)
   - Revoquer les accès d'un utilisateur (5)
   - Réactiver les accès d'un utilisateur (6)
   - Consulter une entreprise (7)
   - Créer, modifier une entreprise (8)
   - supprimer une entreprise (9)
   - Consulter une fiche patient (10)
   - Créer, modifier une fiche patient (11)
   - supprimer une fiche patient (12)
   - Ajouter un patient à une entreprise (13)
   - Envoyer demande de validation des résultats (14)
   - Creer, modifier un questionnaire pour un patient (15)
   - Consulter un questionnaire (16)
   - Créer, Modifer un resultat (17)
   - Supprimer un résultat (18)
   - Consulter un résultat (19)
 
## Les profils et utilisateurs
L'application doit avoir plusieurs profiles qui ont des droits spécifiques d'actions à effectuer.
Un utlisateur est toujours associé à un profil
  
  ### Les profils
    - Administrateur: * (peut tout faire)
    - Medecin: 7,10,14,16,19
    - Technicien: 10,16,17,18,19
    - Aide soignant: 7,8,10,11,12,13,14,15,16,19


## Restrictions
Une entité ne peut être supprimé si et seulement si elle n'a aucune autre entité rattachée à elle.


## Modèle de donnée (Todo)

- Entreprise
- Patient
- Role
- Utilisateur 
- Questionnaire
- Resultat 

## Relations entre les donnees 
- Une Entreprise a plusieurs patients 
- Un patient appartient a une Entreprise
- Un utilisateur appartient un role 
- Un role a plusieurs utilisateurs
- Un resultat appartient a un patient
- Un patient a plusieurs resultats
- Un questionnaire appartient a un patient 
- Un patient a plusieurs questionnaires

# Installation

supprimer son env et le recréer

```python
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate 
```

