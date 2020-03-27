#!/bin/bash
Job=$Job
wrk_spc=/var/lib/jenkins/workspace/$Job
trg_dir=/u02


if [ -d $trg_dir ]; then
 chown -R jenkins:jenkins $trg_dir
 rm -rf $trg_dir/*
fi

mkdir -p $trg_dir
chmod -R 755 $trg_dir
cp -r $wrk_spc/* $trg_dir
chown -R jenkins:jenkins $trg_dir  

#Execution of script 

sh $trg_dir/Oracle/shell/add.sh
sh $trg_dir/Oracle/shell/add1.sh 
sh $trg_dir/Oracle/shell/mult.sh
sh $trg_dir/Oracle/shell/mult1.sh

sh $trg_dir/Oracle/hello.sh
sh $trg_dir/Oracle/hellworld.sh
sh $trg_dir/Oracle/hellworld1.sh

#Build java project

cd $trg_dir/Oracle/java
javac Manish.jar
java $trg_dir/Oracle/java/Manish

echo "Build Is Successful" 


