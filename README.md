# LITRevu

## Description du Projet

LITRevu est une application web basée sur Django qui permet aux utilisateurs de créer et de gérer des critiques de livres et des tickets. C'est un projet conçu pour démontrer les compétences en développement web avec Django.

## Fonctionnalités

- Création et gestion de tickets (demandes de critiques).
- Création et gestion de critiques de livres.
- Association de critiques à des tickets.
- Interface utilisateur intuitive.

## Technologies Utilisées

- Python 3.x
- Django (version spécifiée dans `requirements.txt`)
- HTML/CSS

## Installation

Suivez ces étapes pour configurer et exécuter le projet localement :

1.  **Clonez le dépôt :**

    ```bash
    git clone https://github.com/xavierjeanne/OC_project_9
    cd OC_project_9
    ```

2.  **Créez et activez un environnement virtuel (recommandé) :**

    ```bash
    python -m venv env
    # Sur Windows
    .\env\Scripts\activate
    # Sur macOS/Linux
    source env/bin/activate
    ```

3.  **Installez les dépendances :**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Appliquez les migrations de la base de données :**

    ```bash
    python manage.py migrate
    ```

5.  **Démarrez le serveur de développement :**

    ```bash
    python manage.py runserver
    ```

    L'application sera accessible à l'adresse `http://127.0.0.1:8000/`.

