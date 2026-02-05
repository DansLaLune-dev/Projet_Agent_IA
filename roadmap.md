# Roadmap Agile | Projet Rapport de Stage | Fait par Capitaine Robin

Ce document présente la roadmap agile du projet, découpée en versions (milestones), avec les objectifs et les fonctionnalités associées à chaque étape.

---

## Version v0.1 — Workflow
**Objectif principal :** Définir le workflow global et poser les bases du projet.  

**Tâches :**
- Créer un fichier `roadmap.md` et structurer les versions
- Concevoir le workflow de l’agent (Excalidraw)
- Initialiser l’agent et le contexte
- Préparer la mémoire (court et long terme)

**Livrable :**
- Image du workflow commitée : ProjetWorkflow.excalidraw,ProjetWorkflow.png
- Roadmap.md

---

## Version v0.2 — Agent de génération de contenu
**Objectif principal :** Générer automatiquement les sections principales du rapport.  

**Tâches :**
- Génération de la présentation de l’entreprise
- Génération de l’état de l’art du sujet
- Génération des sections résultats (architecture, choix techniques, limites)
- Ajout des sources à la fin du document

**Livrable :**
- Fichier Markdown contenant toutes les sections générées

---

## Version v0.3 — Interaction & gestion du contexte
**Objectif principal :** Permettre une interaction humaine intelligente et une bonne gestion du contexte.  

**Tâches :**
- Interaction humaine :
  - Sélection de la section à générer
  - Validation/refus d’une génération
  - Modification des instructions
- Gestion de la mémoire :
  - Mémoire court terme : sections en cours
  - Mémoire long terme : contexte et décisions validées
- Possibilité d’arrêter et reprendre le workflow

**Livrable :**
- Agent capable d’interagir intelligemment
- Reprise de workflow fonctionnelle

---

## Version v0.4 — Outils, export & robustesse
**Objectif principal :** Permettre l’usage d’outils intelligents et l’export du rapport.  

**Tâches :**
- Utilisation intelligente des outils externes
- Export final du rapport en Markdown
- Export PDF (bonus)
- Détection de prompt injection (bonus)

**Livrable :**
- Fichier Markdown final
- Fichier PDF (optionnel)
- Système de sécurité contre prompt injection (optinnel)

---

## Version v1.0 — Livraison finale
**Objectif principal :** Finaliser le projet et documenter les choix.  

**Tâches :**
- Rédaction d’un rapport expliquant :
  - Roadmap
  - Architecture
  - Gestion du contexte
  - Interactions humaines
  - Outils et observabilité
- Nettoyage du repo et préparation de la livraison

**Livrable :**
- Rapport final
- Repo complet et fonctionnel

---

## Notes importantes
- Chaque commit sur `main` correspond à une nouvelle version.
- Les tâches peuvent être modifiées en fonction de l’avancement du projet.