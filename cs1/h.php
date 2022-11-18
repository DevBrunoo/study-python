<?php 

$password = $_GET["password"];
$user = $_GET["user"];

if ($user > 0){
    echo "seu nome de usuario e $user, \n e sua senha é $password";
} else {
    echo "nao existe";
}

?>

<fieldset>
    <form action="h.php" method="get">
        <fieldset>
            <br>
            <input type="text" class="user" name="user">
            <input type="text" class="password" name="password">
        </fieldset>
    </form>
</fieldset>