Cahier des charges — Enrôlement
    1. Contexte & objectifs

    Contexte : recenser et suivre tous les établissements pharmaceutiques (officines, dépôts, grossistes, industriels, labos, etc.).

    Objectifs :

    - Disposer d’une base de données centralisée et à jour.

    - Permettre l’enrôlement (création) + mise à jour des informations (CRUD).

    - Géolocaliser chaque établissement (coords GPS, adresse, zone).

    - Stocker photos et documents justificatifs.

    2. Fonctions:
    - CRUD établissement (fiche complète).

    - Géolocalisation (lat/lon + carte simple).

    - Import CSV/XLSX (mapping colonnes → champs).

    - Export CSV/XLSX.

    - Recherche par nom, type, zone, statut.
    - Tableau de bord pour chaque entité


    3. Données à collecter (à partir des fichiers Excel fournis)
    Les champs ci-dessous proviennent des onglets Excel transmis et seront adaptés en modèles de données. Certains champs seront communs à tous les types; d’autres sont spécifiques.

    3.1 Officine
    •	REGION
    •	DEPARTEMENT
    •	COMMUNE
    •	QUARTIER
    •	ADRESSE  EXACTE DE L'OFFICINE
    •	NOM DE L'OFFICINE
    •	NUMERO TELEPHONE
    •	ANNEE CREATION
    •	ANNEE   D'EXPLOITATION
    •	STATUT (Transfert-Rachat)
    •	PRENOM ET NOM TITULAIRE/PHARMACIEN RESPONSABLE
    •	NUMERO D'INSCRIPTION ORDRE DES PHARMACIEN
    •	SEXE 
    •	TRANCHE D'AGE
    •	NOMBRE D'ASSISTANTS
    •	NOMBRE D'EMPLOYE PHARMACIEN
    •	NOMBRE D'EMPLOYE NON PHARMACIEN
    •	NOMBRE D'AGENT DE SECURITE
    •	NOMBRE D'AGENT D'HYGIENE
    •	CHIFFRE D'AFFAIRE
    •	NOMBRE DE VEHICULE(livraison et transfert)
    •	POINTS DE GEOLOCALISATION
    •	OBSERVATIONS
    3.2 Dépôt de médicaments
    •	REGION
    •	DEPARTEMENT
    •	COMMUNE
    •	QUARTIER/VILLAGE/HAMEAU
    •	POINTS DE GEOLOCALISATION
    •	NOM DU DEPOT 
    •	ADRESSE  EXACTE DU DEPOT
    •	NUMERO TELEPHONE
    •	ANNEE D'OUVERTURE 
    •	PRENOM ET NOM RESPONSABLE/DEPOSITAIRE
    •	SEXE 
    •	OBSERVATIONS
    3.3 Grossiste répartiteur
    •	REGION
    •	DEPARTEMENT
    •	COMMUNE
    •	QUARTIER
    •	POINTS DE GEOLOCALISATION
    •	NOM GROSSISTE REPARTITEUR
    •	ADRESSE  EXACTE 
    •	NUMERO TELEPHONE
    •	ANNEE D'OUVERTURE 
    •	PRENOM ET NOM RESPONSABLE/DIRECTEUR
    •	NOMBRE D'EMPLOYE PHARMACIEN
    •	NOMBRE D'EMPLOYE NON PHARMACIEN
    •	NOMBRE D'AGENT DE SECURITE
    •	NOMBRE D'AGENT D'HYGIENE
    •	CHIFFRE D'AFFAIRE
    •	NOMBRE DE VEHICULE(livraison et transfert)
    •	OBSERVATIONS
    3.4 Agence de promotion
    •	REGION
    •	DEPARTEMENT
    •	COMMUNE
    •	QUARTIEr
    •	POINTS DE GEOLOCALISATION
    •	NOM DE L'AGENCE DE PROMOTION
    •	ADRESSE  EXACTE 
    •	NUMERO TELEPHONE
    •	ANNEE D'OUVERTURE 
    •	NUMERO DE L'AGREMENT
    •	DATE DE L'AGREMENT
    •	PRENOM ET NOM  DU PHARMACIEN RESPONSABLE
    •	NOMBRE D'EMPLOYE PHARMACIEN
    •	NOMBRE D'EMPLOYE NON PHARMACIEN
    •	CHIFFRE D'AFFAIRE
    •	NOM DU LABORATOIRE REPRESENTE
    •	OBSERVATIONS
    3.5 Établissement de fabrication
    •	REGION
    •	DEPARTEMENT
    •	COMMUNE
    •	QUARTIER
    •	POINTS DE GEOLOCALISATION
    •	NOM DE L'ETABLISSEMENT
    •	ADRESSE  EXACTE 
    •	NUMERO TELEPHONE
    •	ANNEE D'OUVERTURE 
    •	PRENOM ET NOM RESPONSABLE
    •	NOMBRE D'EMPLOYE PHARMACIEN
    •	NOMBRE D'EMPLOYE NON PHARMACIEN
    •	NOMBRE D'AGENT DE SECURITE
    •	NOMBRE D'AGENT D'HYGIENE
    •	CHIFFRE D'AFFAIRE
    •	OBSERVATIONS
    adopte un bon modele
    4. Tech:
    -docker
    - Odoo 16 ou 17.

    - PostgreSQL.

    - Local (Docker Compose simple), pas de Nginx/SSL.
    faire un joli design
    