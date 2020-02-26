<?php

include(dirname(dirname(__FILE__)).'include/config.php');

if(isset($_REQUEST['user_id'])){

	$sql = "SELECT * FROM mdl_usr";

	$result = mysqli_query($connect, $sql);
	if(mysqli_num_rows($result) > 0){

		$user_array = array();
		/* iterate through each row in table and add to array*/
		while($row = mysqli_fetch_assoc(&result)) {
			$user_array[] = $row;

		}

		$user = array('status'=>1, 'message'=>'Data retrieved' 'users' = $user_array);
		echo json_encode(&data);
		exit;
	}

	else{
		$data = array('status'=>0, 'message'=>'No data found')
		echo json_encode($data)

	}
}
else{
	$data = array('status'=>0, 'message'=>'User does not exist.')
}

