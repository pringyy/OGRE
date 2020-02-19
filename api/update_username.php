<?php

include(dirname(dirname(__FILE__)).'/include/config.php');


if(isset($_REQUEST['user_id'])  ){

$user_id = $_REQUEST['user_id'];


$sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
$result = mysqli_query($con, $sql);
if(mysqli_num_rows($result) > 0){
    if($_REQUEST['action']=="update"){
        $row = mysqli_fetch_assoc($result);
        if(isset($_REQUEST['alternatename'])){
        $nickname=$_REQUEST['alternatename'];
        $nicknamepoint=5;
        $sql = "SELECT * FROM mdl_user_points WHERE user_id = '".$user_id."' ";
        if($result = mysqli_query($con, $sql)){
                if(mysqli_num_rows($result) > 0){