#!/bin/bash

wrk_spc=/Users/manishroy/.jenkins/workspace/MyJOB
dep_dir=/u02

if [ -d $dep_dir ]; then
 rm -rf $dep_dir
fi

mkdir $dep_dir

cp -r $wrk_spc/* /u02/
chmod -R 755 /u02

#Execution of script 

sh /u02/Oracle/shell/add.sh
sh /u02/Oracle/shell/add1.sh 
sh /u02/Oracle/shell/mult.sh
sh /u02/Oracle/shell/mult1.sh

sh /u02/Oracle/hello.sh
sh /u02/Oracle/hellworld.sh
sh /u02/Oracle/hellworld1.sh


echo "Build Is Successful" 


