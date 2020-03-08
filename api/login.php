<?php

define('AJAX_SCRIPT', true);
define('REQUIRE_CORRECT_ACCESS', true);
define('NO_MOODLE_COOKIES', true);

require_once(dirname(dirname(__FILE__)).'/config.php');
require_once($CFG->libdir . '/externallib.php');
include(dirname(dirname(__FILE__)).'/include/encrypt.php');

// Allow CORS requests.
header('Access-Control-Allow-Origin: *');



if((isset($_REQUEST['username']) && $_REQUEST['username'] != "") && (isset($_REQUEST['password']) && $_REQUEST['password'] != '') && isset($_REQUEST['encrypted_key'])){

    $encrypted_key = $_REQUEST['encrypted_key'];

    $cypher = new MyCypher();
    $encrypted_api_key = $cypher->encrypt($api_key);
    
    if (strcmp($encrypted_api_key,$encrypted_key)!=0){
            $data = array('status'=>0,'message'=>'wrong api key');
            echo json_encode($data);
            exit;
    }
    
// get the moodle username and passwword here
$username = required_param('username', PARAM_USERNAME);
$password = required_param('password', PARAM_RAW);

echo $OUTPUT->header();

if (!$CFG->enablewebservices) {
    throw new moodle_exception('enablewsdescription', 'webservice');
}

$username = trim(core_text::strtolower($username));

if (is_restored_user($username)) {
    throw new moodle_exception('restoredaccountresetpassword', 'webservice');
}
$systemcontext = context_system::instance();
$reason = null;

// use this moodle offical api to verify the django user
$user = authenticate_user_login($username, $password, false, $reason, false);

if (!empty($user)) {
  
    $data = array('status'=>1, 'message'=>'Login Successfull.', 'userinfo'=>array("id"=>$user->id,"username"=>$user->username,"firstname"=>$user->firstname,"lastname"=>$user->lastname,"nickname"=>$user->alternativename));
    echo json_encode($data);
    exit;
    
} else {
    
    $data = array('status'=>0,'message'=>'No user found.');
    echo json_encode($data);
    exit;
    
}
    
}else{
    $data = array('status'=>0,'message'=>'Insufficient Parameters.');
    echo json_encode($data);
    exit;
}

?>