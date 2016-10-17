#! /bin/bash

touch file
git add file > /tmp/mygit.log 2>&1 &
git commit -m 'testing file to system' > /tmp/mygit.log 2>&1 &
git push > /tmp/mygit.log 2>&1 &

sleep 5 
rm ./file

git rm file > /tmp/mygit.log 2>&1 &
git commit -m 'testing file to system' > /tmp/mygit.log 2>&1 &



