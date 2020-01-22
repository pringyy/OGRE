<?php

define('AJAX_SCRIPT', true);
define('REQUIRE_CORRECT_ACCESS', true);
define('NO_MOODLE_COOKIES', true);

require_once(dirname(dirname(__FILE__)).'/config.php');
require_once($CFG->libdir . '/externallib.php');

// Allow CORS requests.
header('Access-Control-Allow-Origin: *');



if((isset($_REQUEST['username']) && $_REQUEST['username'] != "") && (isset($_REQUEST['password']) && $_REQUEST['password'] != '')){



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
$user = authenticate_user_login($username, $password, false, $reason, false);

if (!empty($user)) {
 	
    $data = array('status'=>1, 'message'=>'Login Successfull.', 'userinfo'=>array("id"=>$user->id,"username"=>$user->username,"firstname"=>$user->firstname,"lastname"=>$user->lastname));
    echo json_encode($data);
    exit;
    
} else {
    
    $data = array('status'=>0,'message'=>'No user found, must be a user from moodle!');
    echo json_encode($data);
    exit;
    
}
    
}else{
    $data = array('status'=>0,'message'=>'Insufficient Parameters.');
    echo json_encode($data);
    exit;
}

?>
