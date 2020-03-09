<?php

include(dirname(dirname(__FILE__)).'/include/config.php');
include(dirname(dirname(__FILE__)).'/include/encrypt.php');





// verfiy if the php side receive the id and points
if(isset($_REQUEST['user_id']) && isset($_REQUEST['points']) && isset($_REQUEST['encrypted_key'])){

// receive the user_id and related points here
$user_id = $_REQUEST['user_id'];
$points = $_REQUEST['points'];

$encrypted_key = $_REQUEST['encrypted_key'];

$cypher = new MyCypher();
$encrypted_api_key = $cypher->encrypt($api_key);

if (strcmp($encrypted_api_key,$encrypted_key)!=0){
        $data = array('status'=>0,'message'=>'wrong api key');
        echo json_encode($data);
        exit;
}

$sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
$result = mysqli_query($con, $sql);
if(mysqli_num_rows($result) > 0){
    if($_REQUEST['action']=="update"){
        $row = mysqli_fetch_assoc($result);
        if(isset($_REQUEST['alternatename'])){
            // get the user require change name here
        $nickname=$_REQUEST['alternatename'];
        $nicknamepoint=$points;
        $sql = "SELECT * FROM mdl_user_points WHERE user_id = '".$user_id."' ";
        if($result = mysqli_query($con, $sql)){
                if(mysqli_num_rows($result) > 0){
                    $row = mysqli_fetch_assoc($result);
                    $user_points = $row['points'];

                    if($user_points >= $nicknamepoint){
                        $updated_points = $user_points - $nicknamepoint;
                        //update the transaction table
                        $sql = "insert into mdl_user_points_trans (type,detail,userid,amount,spentTime) values('-','Change username','".$user_id."','".$nicknamepoint."',now())  ";
                        mysqli_query($con, $sql);
                        // update the points table
                        $sql = "UPDATE mdl_user_points SET points='".$updated_points."' WHERE user_id='".$user_id."' ";
                        mysqli_query($con, $sql);

                        $sql = "update mdl_user set alternatename = '".$nickname."' WHERE id = '".$user_id."' ";
                        $result = mysqli_query($con, $sql);
                        $sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
                        $result = mysqli_query($con, $sql);
                        $row = mysqli_fetch_assoc($result);

                        $data = array('status'=>1,'message'=>'  Username Updated ', 'user_id'=>$user_id, 'nickname'=>$row['alternatename']);
                        echo json_encode($data);
                        exit;
                    }else{
                        $data = array('status'=>0,'message'=>'User does not have sufficient points');
                        echo json_encode($data);
                        exit;
                    }
                }}		
		
            }else {
                
                 $data = array('status'=>0,'message'=>'Insufficient Parameters.');
            echo json_encode($data);
            exit;
     
            }
            
        }else {
            
        $row = mysqli_fetch_assoc($result);
        $data = array('status'=>1,'message'=>'Get Nickname', 'user_id'=>$user_id, 'nickname'=>$row['alternatename']);
        echo json_encode($data);
        exit;
        
        }
    
    }else{
        $data = array('status'=>0,'message'=>'User does not exist.');
        echo json_encode($data);
        exit;
    }
    
    }else{
            $data = array('status'=>0,'message'=>'Insufficient Parameters.');
            echo json_encode($data);
            exit;
    }
    
    ?>