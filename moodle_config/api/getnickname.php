<?php

//THIS IS THE BACKEND FOR REMOVING POINTS AND CHANGING THE NICKNAME WHEN USERS UPDATE THEIR NICKNAME

include(dirname(dirname(__FILE__)) . '/include/config.php');
include(dirname(dirname(__FILE__)) . '/include/encrypt.php');

//Verify if the php side receives the id and points
if (isset($_REQUEST['user_id']) && isset($_REQUEST['points']) && isset($_REQUEST['encrypted_key'])) {
    
    //Get the user_id and related points from database here
    $user_id = $_REQUEST['user_id'];
    $points  = $_REQUEST['points'];

    $encrypted_key = $_REQUEST['encrypted_key'];
    $cypher            = new MyCypher();
    $encrypted_api_key = $cypher->encrypt($api_key);
    
    //Checks to see if the API key matches between the Moodle server and Django application
    if (strcmp($encrypted_api_key, $encrypted_key) != 0) {
        $data = array(
            'status' => 0,
            'message' => 'wrong api key'
        );
        echo json_encode($data);
        exit;
    }
    
    $sql    = "SELECT * FROM mdl_user WHERE id = '" . $user_id . "' ";
    $result = mysqli_query($con, $sql);

    if (mysqli_num_rows($result) > 0) {
        if ($_REQUEST['action'] == "update") {
            
            $row = mysqli_fetch_assoc($result);
            
            if (isset($_REQUEST['alternatename'])) {
                //Get the users name they want to change to here
                $nickname      = $_REQUEST['alternatename'];
                $nicknamepoint = $points;
                $sql           = "SELECT * FROM mdl_user_points WHERE user_id = '" . $user_id . "' ";
                
                if ($result = mysqli_query($con, $sql)) {
                    if (mysqli_num_rows($result) > 0) {
                        
                        $row         = mysqli_fetch_assoc($result);
                        $user_points = $row['points'];
                        
                        if ($user_points >= $nicknamepoint) { //if the user can afford to change
                            
                            $updated_points = $user_points - $nicknamepoint;
                            //Update the transaction table
                            $sql            = "insert into mdl_user_points_trans (type,detail,userid,amount,spentTime) values('-','Change username','" . $user_id . "','" . $nicknamepoint . "',now())  ";
                            mysqli_query($con, $sql);
                            //Update the points table
                            $sql = "UPDATE mdl_user_points SET points='" . $updated_points . "' WHERE user_id='" . $user_id . "' ";
                            mysqli_query($con, $sql);
                            
                            $sql    = "update mdl_user set alternatename = '" . $nickname . "' WHERE id = '" . $user_id . "' ";
                            $result = mysqli_query($con, $sql);
                            $sql    = "SELECT * FROM mdl_user WHERE id = '" . $user_id . "' ";
                            $result = mysqli_query($con, $sql);
                            $row    = mysqli_fetch_assoc($result);
                            $data = array('status' => 1,'message' => '  Username Updated ','user_id' => $user_id,'nickname' => $row['alternatename']);
                            echo json_encode($data);
                            exit;
                        
                        } else { //Reaches here if the user does not have enough points
                            //Send data back to Django
                            $data = array(
                                'status' => 0,
                                'message' => 'User does not have sufficient points'
                            );
                            echo json_encode($data);
                            exit;
                        }
           
                    } else {
                        //Send data back to Django
                        $data = array('status' => 0,'message' => 'User does not have sufficient points');
                        echo json_encode($data);
                        exit;
                    }
        
                 } else {
                    //Send data back to Django
                    $row  = mysqli_fetch_assoc($result);
                    $data = array('status' => 1,'message' => 'Get Nickname','user_id' => $user_id,'nickname' => $row['alternatename']);
                    echo json_encode($data);
                    exit;
                }
            }
        }
    }
}else{ //Reaches here if inpiut parameters are incorrect
    $data = array('status'=>0,'message'=>'Insufficient Parameters.');
    echo json_encode($data);
    exit;
}

?>