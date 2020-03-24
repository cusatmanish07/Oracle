#!/bin/bash
/Users/manishroy/Manish
wrk_spc=/Users/manishroy/.jenkins/workspace/MyJOB
home_dir=/tmp/Manish


if [ -d $home_dir ]; then
 rm -rf $home_dir
fi

mkdir -p $home_dir

cp -r $wrk_spc/* $home_dir
chmod -R 755 /u02

#Execution of script 

sh $home_dir/Oracle/shell/add.sh
sh $home_dir/Oracle/shell/add1.sh 
sh $home_dir/Oracle/shell/mult.sh
sh $home_dir/Oracle/shell/mult1.sh

sh $home_dir/Oracle/hello.sh
sh $home_dir/Oracle/hellworld.sh
sh $home_dir/Oracle/hellworld1.sh


echo "Build Is Successful" 


