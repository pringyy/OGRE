<?php

include(dirname(dirname(__FILE__)).'/include/config.php');


if(isset($_REQUEST['user_id'])  ){

$user_id = $_REQUEST['user_id'];


$sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
$result = mysqli_query($con, $sql);
if(mysqli_num_rows($result) > 0){