# CTI-Teams-Notification

> For internal use :) 

Quick & Dirty README.md 😛 

Notification sur des canaux Teams d'une nouvelle CVE (via addCVE.cfg)

Notification d'une nouvelle cyberattaque en France (via addRansomware.cfg)

Une action Github se déclenche sur cloture d'une PR et si les fichiers addCVE ou add Ransomware sont renseignés va publier les informations sur channel d'un groupe Teams. 

⚠️ Renseigner les environnements CI :
- MSTEAMS_WEBHOOK_RANSOM
- MSTEAMS_WEBHOOK_CVE 

avec les URL "Webhook" de vos canaux Teams 
