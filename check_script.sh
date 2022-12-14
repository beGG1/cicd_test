#!/bin/bash

res_linter=$( flake8 .)

if [$res_linter = ''];
then
    echo 'Linter check accepted'
else
    echo $res_linter
    exit 0
fi

res_pytest=$( pytest)