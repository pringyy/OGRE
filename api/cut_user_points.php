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
                   
                        $row = mysqli_fetch_assoc($result);
                        $user_points = $row['points'];
                        
                        if($user_points >= $points){
                                $updated_points = $user_points - $points;
									$sql = "insert into mdl_user_points_trans (type,detail,userid,amount,spentTime) values('-','Game play','".$user_id."','".$points."',now())  ";
                                    mysqli_query($con, $sql);  
									
                                    $sql = "UPDATE mdl_user_points SET points='".$updated_points."' WHERE user_id='".$user_id."' ";
                                    mysqli_query($con, $sql);                
                                   
                                    $data = array('status'=>1,'message'=>'Points deducted successfully.', 'user_id'=>$user_id, 'points'=>$updated_points);
                                    echo json_encode($data);
                                    exit;    
                        }else{
                                    $data = array('status'=>0,'message'=>'User does not have sufficient points');
                                    echo json_encode($data);
                                    exit;    
                        }
                        
                        
                    
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
        $data = array('status'=>0,'message'=>'Insufficient Parameters.');
        echo json_encode($data);
        exit;
}

?>