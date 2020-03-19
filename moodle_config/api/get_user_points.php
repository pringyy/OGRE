<?php

//THIS FILE IT USED TO RETRIEVE THE AMOUNT OF OGRE POINTS THE USER HAS AND SEND THEM TO DJANGO APPLICATION

include(dirname(dirname(__FILE__)).'/include/config.php');
include(dirname(dirname(__FILE__)).'/include/encrypt.php');

if(isset($_REQUEST['user_id']) && isset($_REQUEST['encrypted_key'])){
    
    $user_id = $_REQUEST['user_id'];
    $encrypted_key = $_REQUEST['encrypted_key'];

    $cypher = new MyCypher();
    $encrypted_api_key = $cypher->encrypt($api_key);

    //Checks to see that the API keys match with Django and Moodle server
    if (strcmp($encrypted_api_key,$encrypted_key)!=0){
        $data = array('status'=>0,'message'=>'wrong api key');
        echo json_encode($data);
        exit;
    }
    
    $sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
    $result = mysqli_query($con, $sql);

    if(mysqli_num_rows($result) > 0){

        //Select the users points here
        $sql = "SELECT * FROM mdl_user_points WHERE user_id = '".$user_id."' ";
        if($result = mysqli_query($con, $sql)){
            if(mysqli_num_rows($result) > 0){
               
                $row = mysqli_fetch_assoc($result);
                $points = $row['points'];
                $user_id = $row['user_id'];
                //Send the user points data to Django
                $data = array('status'=>1,'user_id'=>$user_id, 'points'=>$points);
                echo json_encode($data);
                exit;
                
            }else{
                //Sends data to Django
                $data = array('status'=>0,'message'=>'No User points found for this user.');
                echo json_encode($data);
                exit;
            }
        }
    }else{ //Reaches here if the user does not exist
        //Sends data to Django
        $data = array('status'=>0,'message'=>'User does not exist.');
        echo json_encode($data);
        exit;
    }
      
}else{
        //Sends data to Django
        $data = array('status'=>0,'message'=>$_REQUEST);
        echo json_encode($data);
        exit;
}

?>