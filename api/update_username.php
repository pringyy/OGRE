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
                    $row = mysqli_fetch_assoc($result);
                    $user_points = $row['points'];

                    if($user_points >= $nicknamepoint){
                        $updated_points = $user_points - $nicknamepoint;
                        $sql = "insert into mdl_user_points_trans (type,detail,userid,amount,spentTime) values('-','Change nickname','".$user_id."','".$nicknamepoint."',now())  ";
                        mysqli_query($con, $sql);

                        $sql = "UPDATE mdl_user_points SET points='".$updated_points."' WHERE user_id='".$user_id."' ";
                        mysqli_query($con, $sql);

                        $sql = "update mdl_user set alternatename = '".$nickname."' WHERE id = '".$user_id."' ";
                        $result = mysqli_query($con, $sql);
                        $sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
                        $result = mysqli_query($con, $sql);
                        $row = mysqli_fetch_assoc($result);