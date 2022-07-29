##################################################
## Ransomware & CVE notifier for Teams
##################################################
## License : MIT
##################################################
## Author: #JMousqueton (Julien Mousqueton)
## Copyright: Copyright 2022
## Version: 1.2
## Maintainer: #JMousqueton (Julien Mousqueton)
## Email: julien_at_mousqueton.io
##################################################
# Generic/Built-in
import os
import requests

# Other Libs
from configparser import ConfigParser

def send_teams(webhook_url:str, content:str, title:str, color:str="000000") -> int:
    """
      - Send a teams notification to the desired webhook_url
      - Returns the status code of the HTTP request
        - webhook_url : the url you got from the teams webhook configuration
        - content : your formatted notification content
        - title : the message that'll be displayed as title, and on phone notifications
        - color (optional) : hexadecimal code of the notification's top line color, default corresponds to black
    """
    response = requests.post(
        url=webhook_url,
        headers={"Content-Type": "application/json"},
        json={
            "themeColor": color,
            "summary": title,
            "sections": [{
                "activityTitle": title,
                "activitySubtitle": content
            }],
        },
    )
    return response.status_code # Should be 200

###
## Notification pour Ransomware
##
Url=os.getenv('MSTEAMS_WEBHOOK_RANSOM')

config = ConfigParser(interpolation=None)
config.read('addRansomware.cfg')
Date = config.get('Ransomware','Date')
Victime = config.get('Ransomware','Victime')
UrlVictime = config.get('Ransomware','UrlVictime')
Ransomware = config.get('Ransomware','Ransomware')
Ransom = config.get('Ransomware','Ransom')
Exfiltration = config.get('Ransomware','Exfiltration')
Crypted = config.get('Ransomware','Crypted')
Deadline = config.get('Ransomware','Deadline')
Production = config.get('Ransomware','Production')
Source = config.get('Ransomware','Source') 

if Date != "":
    if UrlVictime == "":
        Query = Victime
    else:
        Query = UrlVictime

    if Ransomware != "":
        Ransomware = "🏴‍☠️ : "+ Ransomware + "<br>"
    else:
        Ransomware = "🏴‍☠️ : <i>N/A</i><br>"

    if Ransom != "":
        Ransom = "💰 : "+ Ransom + "<br>"
    else:
        Ransom = "💰 : <i>N/A</i><br>"

    if Exfiltration != "":
        Exfiltration = "📡 : "+ Exfiltration + "<br>"
    else:
        Exfiltration = "📡 : <i>N/A</i><br>"

    if Crypted != "":
        Crypted = "🔐 : "+ Crypted + "<br>"
    else:
        Crypted = "🔐 : <i>N/A</i><br>"

    if Deadline != "":
        Deadline = "⏰ : "+ Deadline + "<br>"


    if Production != "":
        Production = "🔴 : "+ Production + "<br>"


    if Source != "":
        Source = "<br>🔎 : "+ Source + "<br>"
    else:
        Source = "<br>🔎 : <a href=\"https://ransomwatch.mousqueton.io\">Ransomwatch</a><br>"

    UrlVictime="🌍 : <a href=\"https://www.google.com/search?q="+ Query + "\">"+ Query + "</a><br>"
    Titre=Date + " - " + Victime 


    Texte =  UrlVictime + Ransomware + Ransom + Exfiltration + Crypted + Deadline + Production + Source
    if send_teams(Url,Texte,Titre) == 200: 
        fichier = open("addRansomware.cfg", "w")
        fichier.write("[Ransomware]\nDate = \nVictime = \nUrlVictime = \nRansomware =\nRansom = \nExfiltration = \nCrypted = \nProduction = \nDeadline = \nSource = \n")
        fichier.close()
        print('Une nouvelle cyberattaque a été notifiée')
else: print('Pas de nouvelle cyberattaque notifiée')
###
# Notification pour CVE
##
Url=os.getenv('MSTEAMS_WEBHOOK_CVE')

configCVE = ConfigParser(interpolation=None)
configCVE.read('addCVE.cfg')
Vendor = configCVE.get('CVE','Vendor')
Product = configCVE.get('CVE','Product')
Msg = configCVE.get('CVE','Msg')
Source = configCVE.get('CVE','Source')
Level = configCVE.get('CVE','Level')
CVSS = configCVE.get('CVE','CVSS')
CVE = configCVE.get('CVE','CVE')
Comment = configCVE.get('CVE','Comment')


if Vendor != "":
    if CVE != "": 
        CVE ="[" + CVE + "] "
    Titre = "🚨 " + CVE + "Vulnérabillité chez " + Vendor
    if Product != "":
        Product = "<b>Produit(s) impacté(s) : </b>" + Product + "<br>"
    if Level == "Critical":
        Level = "<b>Criticité : </b>🔴 Critical<br>"
    if Level == "High":
        Level = "<b>Criticité : </b>🟠 High<br>"
    if Level == "Medium":
        Level = "<b>Criticité : </b>🟡 Medium<br>"
    if CVSS != "":
        CVSS = "<b>Note CVSS v3 :</b> " +  CVSS + "/10 <br>"
    if Msg !="": 
        Msg = "📝 : " +  Msg + "<br>"
    if Source != "":
        Source = "<br>🌍 : <a href=\"" + Source + "\">" +  Source + "</a><br>" 
    if Comment != "":
        Comment = "🔎 : " + Comment + "<br>"
    Texte = Msg + Level + CVSS + Product +  Comment + Source
    if send_teams(Url,Texte,Titre) == 200:
        fichier = open("addCVE.cfg", "w")
        fichier.write("[CVE]\nVendor = \nProduct = \nMsg = \nSource = \nLevel = \nCVSS = \nCVE = \nComment = \n")
        fichier.close()
        print('Une nouvelle CVE a été notifiée')
else: print('Pas de nouvelle CVE notifiée')
