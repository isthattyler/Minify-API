#!/usr/bin/bash

function minify() {
    if [ "$1" == "html" ];
    then
        python ~/Script/Minify-API/html.py
    else
        python ~/Script/Minify-API/css.py
    fi
}
