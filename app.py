from flask import Flask, render_template, request, session, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def generer_combinaison():
    """Génère une combinaison aléatoire de 4 chiffres entre 0 et 9"""
    return [secrets.randbelow(10) for _ in range(4)]

@app.route('/')
def index():
    # Génère une nouvelle combinaison à chaque visite de la page d'accueil
    session['combinaison'] = generer_combinaison()
    return render_template('index.html')

@app.route('/verifier', methods=['POST'])
def verifier():
    try:
        # Récupère la combinaison stockée en session
        combinaison_correcte = session.get('combinaison')
        
        if not combinaison_correcte:
            return redirect(url_for('index'))
        
        # Récupère les chiffres entrés par l'utilisateur
        chiffre1 = int(request.form.get('chiffre1', -1))
        chiffre2 = int(request.form.get('chiffre2', -1))
        chiffre3 = int(request.form.get('chiffre3', -1))
        chiffre4 = int(request.form.get('chiffre4', -1))
        
        combinaison_utilisateur = [chiffre1, chiffre2, chiffre3, chiffre4]
        
        # Vérifie si la combinaison est correcte
        if combinaison_utilisateur == combinaison_correcte:
            return redirect(url_for('win'))
        else:
            return render_template('index.html', erreur=True)
            
    except (ValueError, TypeError):
        return render_template('index.html', erreur=True)

@app.route('/win')
def win():
    # Vérifie qu'on a bien passé par la vérification
    if 'combinaison' not in session:
        return redirect(url_for('index'))
    
    combinaison = session.get('combinaison')
    return render_template('win.html', combinaison=combinaison)

@app.route('/bruteforce')
def bruteforce():
    """Page d'aide pour montrer comment bruteforcer avec des boucles imbriquées"""
    return render_template('bruteforce.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
