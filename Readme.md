# Gomu Gomu Developpeur - Workflow Template 🚀

Bienvenue sur le dépôt du bot du channel Gomu Gomu Developpeur !

Ce dépôt héberge le code source du workflow et du  bot qui alimente le channel Telegram de l'organisation Gomu Gomu Developpeur. Ansi nous pourrons le réutilisé dans d'autre projet différent .

Le bot est conçu pour vous tenir informé de toute l'activité sur le dépôt principal de l'organisation. Il surveille les actions effectuées par les membres et vous envoie des notifications en temps réel via Telegram.

## Fonctionnalités du bot

- Détection des commits et pushs : Le bot identifie chaque commit et push effectué sur le dépôt principal et envoie un message d'information sur le channel Telegram.
- Suivi des Pull Requests : Le bot détecte la création de nouvelles Pull Requests et informe le channel Telegram pour une meilleure collaboration.

## Prérequis

Pour exécuter le bot, vous aurez besoin de :

- Un compte GitHub
- Un bot Telegram créé pour interagir avec le channel. (Plusieurs services en ligne permettent de créer des bots Telegram.)
- Un channel Telegram pour intéragir avec le bot dans notre cas notre nos l'avons configuré  pour la communauté Gomu Gomu Developpeur .
- Python

## Installation

1. Cloner le dépôt:
   ```bash
   git clone https://github.com/GomuDevelopers/workflow_template.git
   ```
2. Configuration du bot
    Créez un fichier nommé .env dans la racine du projet ou allez créé des variable secret et renseignez les variables d'environnement suivantes :
   ```bash
     BOT_TOKEN=YOUR_BOT_TOKEN
     TELEGRAM_CHAT_ID=YOUR_TELEGRAM_CHAT_ID
   ```
   
    **Remplacez les valeurs suivantes**
    - `YOUR_BOT_TOKEN`: Le token d'accès de votre bot Telegram.
    - `YOUR_TELEGRAM_CHAT_ID`: L'identifiant unique de votre channel Telegram.
      
## Contribuer au projet
  Nous encourageons les contributions à ce projet ! N'hésitez pas à créer des issues pour signaler des bugs ou proposer des améliorations.  Vous pouvez également 
  soumettre des Pull Requests pour intégrer vos modifications au code source.
  