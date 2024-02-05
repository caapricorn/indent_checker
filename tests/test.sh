#!/bin/bash

#export LANG=C.UTF-8

# Activate the virtual environment
#source C:/Users/Alexandra/PycharmProjects/"indentChecker2(3)"/indentChecker2/venv/Scripts/activate

for file in C:/Users/sasho/PycharmProjects/MatrixIndentation/indent_check-master2/indent_check-master/tests/acc/*
do
py main.py "$file"
echo "$file"
done > acc_test_results.txt