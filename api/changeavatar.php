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



// use sql statement to exact the user
$sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
$result = mysqli_query($con, $sql);
if(mysqli_num_rows($result) > 0){

            // to see if the use has points records
            $sql = "SELECT * FROM mdl_user_points WHERE user_id = '".$user_id."' ";
            if($result = mysqli_query($con, $sql)){
                // if this user has points records
                if(mysqli_num_rows($result) > 0){

                        $row = mysqli_fetch_assoc($result);
                        $user_points = $row['points'];
                        // do the points cutting here!
                        if($user_points >= $points){
                                $updated_points = $user_points - $points;
                                                                        $sql = "insert into mdl_user_points_trans (type,detail,userid,amount,spentTime) values('-','Change avatar','".$user_id."','".$points."',now())  ";
                                    mysqli_query($con, $sql);
                                                                        // update the points of user.
                                    $sql = "UPDATE mdl_user_points SET points='".$updated_points."' WHERE user_id='".$user_id."' ";
                                    mysqli_query($con, $sql);

                                    // send the related message to dajngp
                                    $data = array('status'=>1,'message'=>'Avatar changed successfully.', 'user_id'=>$user_id, 'points'=>$updated_points);
                                    echo json_encode($data);
                                    exit;
                        }else{      // else send the error message
                                    $data = array('status'=>0,'message'=>'User does not have sufficient points');
                                    echo json_encode($data);
                                    exit;
                        }



                }else{ // the user has no records

                    $data = array('status'=>0,'message'=>'No User points found for this user.');
                    echo json_encode($data);
                    exit;
                }

            }

}else{// this user does not exist
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