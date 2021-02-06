#!/bin/bash

# TODO: This URL should be changed to reflect the correct endpoint URL when challenge is hosted
FLAG="`curl -b 'auth=f4e53e561c6580d6d304f3f31e3102f5' http://srv3.magpiectf.ca:9355/api.php`"
echo $( md5sum <<< $FLAG | cut -d " " -f1)

