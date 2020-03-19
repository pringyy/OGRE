<?php

/*THIS CODE IS THE MOODLE BACKEND FOR VERIFYING USER REGISTRATION DETAILS SUPPLIED ON THE DJANGO END*/

include(dirname(dirname(__FILE__)).'/include/config.php');
include(dirname(dirname(__FILE__)).'/include/encrypt.php');
define('AJAX_SCRIPT', true);
define('REQUIRE_CORRECT_ACCESS', true);
define('NO_MOODLE_COOKIES', true);

require_once(dirname(dirname(__FILE__)).'/config.php');
require_once($CFG->libdir . '/externallib.php');

//Allow CORS requests.
header('Access-Control-Allow-Origin: *');


if((isset($_REQUEST['username']) && $_REQUEST['username'] != "") && (isset($_REQUEST['password']) && $_REQUEST['password'] != '') && isset($_REQUEST['encrypted_key'])){

    $encrypted_key = $_REQUEST['encrypted_key'];

    $cypher = new MyCypher();
    $encrypted_api_key = $cypher->encrypt($api_key);
    
    //Checks to see if the API keys match between Moodle server and Django application
    if (strcmp($encrypted_api_key,$encrypted_key)!=0){
            $data = array('status'=>0,'message'=>'wrong api key');
            echo json_encode($data);
            exit;
    }
    
    //Gets the moodle username and paswword here
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

    //Use this moodle offical api to verify the django user is a Moodle user
    $user = authenticate_user_login($username, $password, false, $reason, false);

    if (!empty($user)) {
      
        $data = array('status'=>1, 'message'=>'Login Successfull.', 'userinfo'=>array("id"=>$user->id,"username"=>$user->username,"firstname"=>$user->firstname,"lastname"=>$user->lastname,"nickname"=>$user->alternativename));
        echo json_encode($data);
        exit;
        
    } else { //reaches here if the details enetered by the Django user do not match any moodle records 
    
        $data = array('status'=>0,'message'=>'No user found.');
        echo json_encode($data);
        exit;
    
    }
    
}else{ //reaches here if the form submitted has not got all the parameters required
    $data = array('status'=>0,'message'=>'Insufficient Parameters.');
    echo json_encode($data);
    exit;
}

?>