#!/bin/bash

DIR=/var/www/html/pdf/
SIZE=$(du -sm $DIR | grep -oP "\d+")
if [[ $SIZE -gt 100 ]]; then
	rm -r $DIR*.pdf
fi
