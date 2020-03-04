<?php

include(dirname(dirname(__FILE__)).'/include/config.php');


if(isset($_REQUEST['user_id'])){
    
    
    $user_id = $_REQUEST['user_id'];
    
    $sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
    $result = mysqli_query($con, $sql);
    if(mysqli_num_rows($result) > 0){

    // select the transaction data from this table mdl_user_points_trans
    $sql = "SELECT * FROM mdl_user_points_trans WHERE userid = '".$user_id."' order by id desc ";
    if($result = mysqli_query($con, $sql)){
    if(mysqli_num_rows($result) > 0){
       
       while($row = mysqli_fetch_assoc($result)){
		   $data[]=$row;
	   }
        
		$total=mysqli_num_rows($result);
		
        $data = array('status'=>1,"current"=> 1,"rowCount"=>10,'user_id'=>$user_id,'total'=>$total,'rows'=>$data);
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