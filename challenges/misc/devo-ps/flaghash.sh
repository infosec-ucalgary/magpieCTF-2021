#!/bin/bash

# TODO: This URL should be changed to reflect the correct endpoint URL when challenge is hosted
FLAG="`curl http://host.docker.internal/scripts/devo-ps/api.php --header 'Authorization: token f4e53e561c6580d6d304f3f31e3102f5'`"
echo $( md5sum <<< $FLAG | cut -d " " -f1)

