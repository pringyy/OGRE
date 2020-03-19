<?php

include(dirname(dirname(__FILE__)).'/include/config.php');
include(dirname(dirname(__FILE__)).'/include/encrypt.php');

if(isset($_REQUEST['user_id']) && isset($_REQUEST['encrypted_key'])){
    
    $user_id = $_REQUEST['user_id'];
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
        $data = array('status'=>0,"current"=> 1,"rowCount"=>10,'user_id'=>'null','total'=>'null','rows'=>'null');
        echo json_encode($data);
        exit;
    }

    }
    }else{
        $data = array('status'=>0,"current"=> 1,"rowCount"=>10,'user_id'=>'null','total'=>'null','rows'=>'null');
        echo json_encode($data);
        exit;
    }
       
}else{
        $data = array('status'=>0,"current"=> 1,"rowCount"=>10,'user_id'=>'null','total'=>'null','rows'=>$data);
        echo json_encode($data);
        exit;
}

?>