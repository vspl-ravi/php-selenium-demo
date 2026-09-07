<?php
$error = '';
$success = false;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username'] ?? '');
    $password = trim($_POST['password'] ?? '');

    if ($username === 'admin' && $password === 'password123') {
        $success = true;
    } else {
        $error = 'Invalid username or password';
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample PHP Login</title>
</head>
<body>
    <h1>Login</h1>

    <?php if ($success): ?>
        <div id="welcome-message">Welcome, admin! Login successful.</div>
    <?php else: ?>
        <form method="POST" action="">
            <input type="text" name="username" id="username" placeholder="Username">
            <input type="password" name="password" id="password" placeholder="Password">
            <button type="submit" id="login-btn">Login</button>
        </form>

        <?php if ($error): ?>
            <div id="error-message" style="color:red;"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>
    <?php endif; ?>
</body>
</html>
