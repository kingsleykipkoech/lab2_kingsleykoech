#!/bin/bash

if [ ! -f "twitter_dataset.csv" ]; then
    echo "Error: twitter_dataset.csv is not in this folder."
    exit 1
fi

echo "     TOP 5 MOST ACTIVE USERS     "
echo "_________________________________"
echo ""
echo "Counting the tweets of every user....."
sleep 2

grep -E '^[0-9]+,' twitter_dataset.csv | cut -d',' -f2 | sort | uniq -c | sort -nr | head -n 5
