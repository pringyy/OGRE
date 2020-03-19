<?php

//THIS IS TO REMOVE POINTS WHEN USERS CHANGE THEIR PROFILE PICTURE

include(dirname(dirname(__FILE__)).'/include/config.php');
include(dirname(dirname(__FILE__)).'/include/encrypt.php');

// Verify if the php side receive the id and points
if(isset($_REQUEST['user_id']) && isset($_REQUEST['points']) && isset($_REQUEST['encrypted_key'])){

//Receive the user ID and related points here by stroing them in a variables
$user_id = $_REQUEST['user_id'];
$points = $_REQUEST['points'];
$encrypted_key = $_REQUEST['encrypted_key'];

$cypher = new MyCypher();
$encrypted_api_key = $cypher->encrypt($api_key);

//Checks to see that the API keys match with Django and Moodle server
if (strcmp($encrypted_api_key,$encrypted_key)!=0){
        $data = array('status'=>0,'message'=>'wrong api key');
        echo json_encode($data);
        exit;
}

// Use SQL statement to find the exact user
$sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
$result = mysqli_query($con, $sql);
if(mysqli_num_rows($result) > 0){

            // Checks to see if the user has points records
            $sql = "SELECT * FROM mdl_user_points WHERE user_id = '".$user_id."' ";
            if($result = mysqli_query($con, $sql)){
                //If this user has points records
                if(mysqli_num_rows($result) > 0){

                        $row = mysqli_fetch_assoc($result);
                        $user_points = $row['points'];
                        // Removes points if the user can afford!
                        if($user_points >= $points){
                                $updated_points = $user_points - $points;
                                                                        $sql = "insert into mdl_user_points_trans (type,detail,userid,amount,spentTime) values('-','Change avatar','".$user_id."','".$points."',now())  ";
                                    mysqli_query($con, $sql);
                                                                        // update the points of user.
                                    $sql = "UPDATE mdl_user_points SET points='".$updated_points."' WHERE user_id='".$user_id."' ";
                                    mysqli_query($con, $sql);

                                    // Send the related message back to Django
                                    $data = array('status'=>1,'message'=>'Avatar changed successfully.', 'user_id'=>$user_id, 'points'=>$updated_points);
                                    echo json_encode($data);
                                    exit;
                        }else{      // Else send the error message
                                    $data = array('status'=>0,'message'=>'User does not have sufficient points');
                                    echo json_encode($data);
                                    exit;
                        }

                }else{ // Reaches here if the user has no records

                    $data = array('status'=>0,'message'=>'No User points found for this user.');
                    echo json_encode($data);
                    exit;
                }

            }

}else{// Reaches here if this user does not exist
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