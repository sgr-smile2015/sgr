#! /bin/bash

touch /home/gitwork/python/file
git add file  
git commit - m 'testing file to system'
git push 

sleep 5 

git rm file 
git commit -m 'testing file to system' 



