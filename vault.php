<?php
session_start();

// Si pas de code en session, on redirige vers l'accueil pour en générer un
if (!isset($_SESSION['vault_code'])) {
    header('Location: index.php');
    exit;
}

$code_secret = $_SESSION['vault_code'];
$message = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $d1 = isset($_POST['d1']) ? (int)$_POST['d1'] : 0;
    $d2 = isset($_POST['d2']) ? (int)$_POST['d2'] : 0;
    $d3 = isset($_POST['d3']) ? (int)$_POST['d3'] : 0;
    $d4 = isset($_POST['d4']) ? (int)$_POST['d4'] : 0;

    $proposition = "{$d1}{$d2}{$d3}{$d4}";

    if ($proposition === $code_secret) {
        // Si c'est le bon code, on va vers la page win
        header('Location: win.php');
        exit;
    } else {
        $message = "Mauvaise combinaison. Le coffre reste fermé.";
    }
}
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Coffre-fort - Tentative</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
    <h1>Entrer la combinaison</h1>
    <p>Entre les 4 chiffres que ton script a trouvés.</p>

    <?php if (!empty($message)) : ?>
        <div class="error"><?= htmlspecialchars($message, ENT_QUOTES, 'UTF-8'); ?></div>
    <?php endif; ?>

    <form method="post" class="vault-form">
        <div class="digits">
            <input type="number" name="d1" min="0" max="9" required>
            <input type="number" name="d2" min="0" max="9" required>
            <input type="number" name="d3" min="0" max="9" required>
            <input type="number" name="d4" min="0" max="9" required>
        </div>
        <button type="submit" class="btn">Déverrouiller</button>
    </form>

    <p class="hint">
        Astuce pédagogique : écris un script PHP qui teste toutes les combinaisons
        avec 4 boucles imbriquées (de 0 à 9 pour chaque chiffre) et qui envoie
        la bonne combinaison à cette page.
    </p>

    <a class="link" href="index.php">Regénérer un nouveau coffre</a>
</div>
</body>
</html>
