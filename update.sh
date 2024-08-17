#!/bin/bash
echo "Starting to update .."

git stash
git pull
git stash pop

echo "Done"