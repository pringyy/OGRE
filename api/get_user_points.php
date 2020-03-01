<?php

include(dirname(dirname(__FILE__)).'/include/config.php');


if(isset($_REQUEST['user_id'])){
    
    
    $user_id = $_REQUEST['user_id'];
    
    $sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
    $result = mysqli_query($con, $sql);
    if(mysqli_num_rows($result) > 0){

        // select the user points here
    $sql = "SELECT * FROM mdl_user_points WHERE user_id = '".$user_id."' ";
    if($result = mysqli_query($con, $sql)){
    if(mysqli_num_rows($result) > 0){
       
       $row = mysqli_fetch_assoc($result);
       $points = $row['points'];
       $user_id = $row['user_id'];
       
        $data = array('status'=>1,'user_id'=>$user_id, 'points'=>$points);
        echo json_encode($data);
        exit;
        
    }else{
        $data = array('status'=>0,'message'=>'No User points found for this user.');
        echo json_encode($data);
        exit;
    }

    }
    }else{
        $data = array('status'=>0,'message'=>'User does not exist.');
        echo json_encode($data);
        exit;
    }
    
    
    
}else{
        $data = array('status'=>0,'message'=>$_REQUEST);
        echo json_encode($data);
        exit;
}

?>