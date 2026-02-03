<?php
session_start();

// Génère une nouvelle combinaison aléatoire de 4 chiffres à chaque visite
$code = '';
for ($i = 0; $i < 4; $i++) {
    $code .= random_int(0, 9);
}
$_SESSION['vault_code'] = $code;
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Coffre-fort Ynov</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
    <h1>Coffre-fort Ynov</h1>
    <p>
        Un coffre-fort à 4 chiffres vient d’être généré aléatoirement.<br>
        Ton objectif : écrire un script qui teste toutes les combinaisons possibles
        avec des boucles imbriquées (4 boucles) pour trouver le bon code.
    </p>
    <p class="info">
        À chaque rechargement de cette page, le code secret change.<br>
        Tu dois donc automatiser la recherche du code.
    </p>
    <a class="btn" href="vault.php">Accéder au coffre</a>
</div>
</body>
</html>
