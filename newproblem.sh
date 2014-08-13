#!/bin/bash

if [ -z  $1 ] 
then 
    echo you must supply a problem number
    exit 1 
fi

if [ -d "problem$1" ] ; then
    echo problem$1 already exists
    exit 1
fi

cp -rf ./template_problem ./problem$1
