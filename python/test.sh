#! /bin/bash

touch /home/gitwork/python/file
git add /home/gitwork/python/file  
git commit - m 'testing file to system'
git push 

sleep 5 

git rm /home/gitwork/python/file 
git commit -m 'testing file to system' 



