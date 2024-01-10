# Importer le module time pour utiliser la fonction sleep
import time

# Définir une fonction pour afficher l'heure avec un tuple
def afficher_heure(heure, minute, seconde):
    # Convertir l'heure, les minutes et les secondes en chaînes de caractères
    # La méthode zfill(2) ajoute un zéro devant si nécessaire pour avoir toujours deux chiffres
    heure_str = str(heure).zfill(2)
    minute_str = str(minute).zfill(2)
    seconde_str = str(seconde).zfill(2)
    # Afficher l'heure sous le format HH:MM:SS
    print(heure_str + ":" + minute_str + ":" + seconde_str)

# Définir une fonction pour régler l'alarme
def regler_alarme(heure_alarme, minute_alarme, seconde_alarme, heure_actuelle, minute_actuelle, seconde_actuelle):
    # Si l'heure actuelle correspond à l'heure de l'alarme
    if (heure_actuelle, minute_actuelle, seconde_actuelle) == (heure_alarme, minute_alarme, seconde_alarme):
        # Afficher un message d'alarme
        print("Alarme ! Il est " + ":".join(map(str, (heure_alarme, minute_alarme, seconde_alarme))))

# Définir l'heure de l'alarme manuellement
heure_alarme, minute_alarme, seconde_alarme = (16, 30, 10)

# Définir l'heure actuelle manuellement
heure_actuelle, minute_actuelle, seconde_actuelle = (16, 30, 00)

# Boucle infinie : # Cette boucle s'exécute indéfiniment jusqu'à ce que le programme soit arrêté manuellement.
while True:
    # Afficher l'heure actuelle
    afficher_heure(heure_actuelle, minute_actuelle, seconde_actuelle)
     # Vérifier si l'heure actuelle correspond à l'heure de l'alarme
    regler_alarme(heure_alarme, minute_alarme, seconde_alarme, heure_actuelle, minute_actuelle, seconde_actuelle)
    
    # Incrementer l'heure actuelle d'une seconde
    # Si les secondes, les minutes ou les heures dépassent leurs limites respectives (60 pour les secondes et les minutes, 24 pour les heures), elles sont remises à zéro et l'unité de temps suivante est incrémentée.
    seconde_actuelle += 1
    # Si les secondes atteignent 60, remettre les secondes à 0 et ajouter 1 aux minutes
    if seconde_actuelle == 60:
        seconde_actuelle = 0
        minute_actuelle += 1
        # Si les minutes atteignent 60, remettre les minutes à 0 et ajouter 1 à l'heure
        if minute_actuelle == 60:
            minute_actuelle = 0
            heure_actuelle += 1
            # Si l'heure atteint 24, remettre l'heure à 0
            if heure_actuelle == 24:
                heure_actuelle = 0

    # Le programme fait une pause d'une seconde avant de recommencer la boucle.
    time.sleep(1)

