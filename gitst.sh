#!/bin/bash

argc=$#

lines=$(git status | awk -F ':'  '/\.[php|css|js|jpg|jpeg|html|htm|png|swf|gif]/{print $2}')
#echo $lines
for line in $lines
	do  echo $lines;git add $line;
done

if [$argc > 0]; then
	git commit -m $1
fi
git status

