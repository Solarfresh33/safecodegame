import requests

URL = "http://127.0.0.1:5000/check"

# Tapez votre code ici pour bruteforce le site

for a in range(10):
    for b in range(10):
        for c in range(10):
            data = {
                'a': str(a),
                'b': str(b),
                'c': str(c)
            }
            response = requests.post(URL, data=data)
            if "win" in response.url or "Félicitations" in response.text:
                print(f"Code trouvé : {a}{b}{c}")
                exit()
                