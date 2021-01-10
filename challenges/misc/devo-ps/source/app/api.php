<?php

$headers =  getallheaders();

foreach($headers as $key=>$val){

    if ($key == "Authorization") {
        if ($val != "token f4e53e561c6580d6d304f3f31e3102f5") {
            echo '{"status":400,"data":"Invalid Request"}';
            exit(0);
        } 
        else {
            echo'magpie{build_automation_genius}';
            exit(0);
        }
    }
}

echo '{"status":400,"data":"Invalid Request"}';

?> 