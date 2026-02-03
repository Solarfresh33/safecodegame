<?php
session_start();

// On vérifie qu'il y a bien un code en session pour éviter l'accès direct "gratuit"
if (!isset($_SESSION['vault_code'])) {
    header('Location: index.php');
    exit;
}

// Optionnel : on peut détruire le code après la victoire
// unset($_SESSION['vault_code']);
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Coffre-fort - Victoire</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
    <h1>Coffre ouvert !</h1>
    <p>Bravo, tu as trouvé la bonne combinaison.</p>
    <div class="flag">
        Flag : <span>YNOV{Bravo!tuasgagné}</span>
    </div>
    <a class="btn" href="index.php">Recommencer avec un nouveau coffre</a>
</div>
</body>
</html>
