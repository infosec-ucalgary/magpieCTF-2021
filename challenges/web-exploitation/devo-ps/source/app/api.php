<?php

if(isset($_COOKIE['auth']) && $_COOKIE['auth'] == 'f4e53e561c6580d6d304f3f31e3102f5') {
    echo'magpie{build_automation_genius}';
} else {
    echo '{"status":400,"data":"Invalid Request"}';
}

?> 