<?php

include(dirname(dirname(__FILE__)).'/include/config.php');


if(isset($_REQUEST['user_id'])){
    
    
    $user_id = $_REQUEST['user_id'];
    
    $sql = "SELECT * FROM mdl_user WHERE id = '".$user_id."' ";
    $result = mysqli_query($con, $sql);
    if(mysqli_num_rows($result) > 0){

        // select the points of users and order it( from table mdl_user_points and mdl_user)
    $sql = "select mdl_user_points.user_id, mdl_user.username,mdl_user_points.points from mdl_user_points,mdl_user where mdl_user.id = mdl_user_points.user_id order by mdl_user_points.points desc;";
    if($result = mysqli_query($con, $sql)){
    if(mysqli_num_rows($result) > 0){
       
		while($row = mysqli_fetch_assoc($result)){
			$data[]=$row;
		}
		 
		 $total=mysqli_num_rows($result);
		 // send the leadboard data
		 $data = array('status'=>1,"current"=> 1,"rowCount"=>10,'user_id'=>$user_id,'total'=>$total,'rows'=>$data);
		 echo json_encode($data);
		 exit;
        
    }else{
        $data = array('status'=>0,'message'=>'we could not get any user points now!');
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