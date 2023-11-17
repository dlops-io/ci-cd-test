#!/bin/bash

echo "Container is running!!!"

echo -en "\033[92m
The following commands are available:
    http-server
        Run the Web Server
\033[0m
"

if [ "${DEV}" = 1 ]; then
  /bin/bash
else
  http-server
fi
