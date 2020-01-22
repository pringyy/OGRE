<?php

include(dirname(dirname(__FILE__)).'/include/config.php');


if(isset($_REQUEST['user_id']) && isset($_REQUEST['points'])){

$user_id = $_REQUEST['user_id'];
$points = $_REQUEST['points'];

$sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
$result = mysqli_query($con, $sql);
if(mysqli_num_rows($result) > 0){


            $sql = "SELECT * FROM mdl_user_points WHERE user_id = '".$user_id."' ";
            if($result = mysqli_query($con, $sql)){
                if(mysqli_num_rows($result) > 0){
                   
                    $sql = "UPDATE mdl_user_points SET points='".$points."' WHERE user_id='".$user_id."' ";
                    mysqli_query($con, $sql);
            
                   
                    $data = array('status'=>1,'message'=>'Points updated successfully.', 'user_id'=>$user_id, 'points'=>$points);
                    echo json_encode($data);
                    exit;
                    
                }else{
                    
                    $sql = "INSERT INTO mdl_user_points (user_id, points) VALUES ('".$user_id."', '".$points."')";
                    mysqli_query($con, $sql);
                    
                    $data = array('status'=>1,'message'=>'Points Recorded successfully.', 'user_id'=>$user_id, 'points'=>$points);
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
        $data = array('status'=>0,'message'=>'Insufficient Parameters.');
        echo json_encode($data);
        exit;
}

?>