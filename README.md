# Lab 2: The Social Media Data Detective

This project analyzes a dataset of 10,000 tweets. The Python script cleans the data, finds the most liked tweet, sorts the top 10 tweets by likes and searches tweets by a keyword. The Bash script shows the top 5 most active users.

## Files

- `data-detective.py` - the Python program with the 4 quests
- `feed-analyzer.sh` - the Bash script for the top 5 most active users
- `twitter_dataset.csv` - the dataset of tweets

## How to run the Python program

Make sure `twitter_dataset.csv` is in the same folder, then run:

```
python3 data-detective.py
```

The program runs Quest 1 to 3 on its own, then asks you to type a word for the search in Quest 4. You can also search a phrase like `dog where`.

## How to run the Bash script

First make it executable (only needed once), then run it:

```
chmod +x feed-analyzer.sh
./feed-analyzer.sh
```

## How my sorting algorithm works

I used Selection Sort. It goes through every position of the list, finds the tweet with the most likes among the remaining unsorted tweets, and swaps it into the current position. It repeats this until the whole list is arranged from the most liked to the least liked tweet.
