#! /bin/bash

if [ $# -eq 0 ]; then
    DAY=$(date +%d)
else
    DAY=$1
fi

source ./aoc_venv/bin/activate

export AOC_SESSION=$(cat .session)

if [ -d $DAY ]; then
    echo "Day $DAY already exists"
    exit 1
else
    mkdir $DAY
    touch $DAY/problem1.py
    touch $DAY/problem2.py

    aocd $DAY > $DAY/input.txt
fi
