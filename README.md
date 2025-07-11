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
- NPM

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

4.  **Appliquez les migrations de la base de données, seulement pour la premiere installation :**

    ```bash
    cd LITRevu
    python manage.py migrate
    ```

5. **Démarrer Tailwind CSS* : , seulement pour la premiere installation :*

    ```bash
    cd theme/static_src
    npm install
    npm run dev
    ```
6.  **Démarrez le serveur de développement :**

    ```bash
    python manage.py runserver
    ```

    L'application sera accessible à l'adresse `http://127.0.0.1:8000/`.  


**Créer un super utilisateur pour accéder a la partie admin : **

    ```bash
    python manage.py createsuperuser
    ```
    Suivez les instructions pour créer un nom d'utilisateur, une adresse e-mail et un mot de passe.
