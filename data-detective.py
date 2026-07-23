import csv
import sys
import os
import time


def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)

    return raw_tweets


def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Check for missing text, and replace empty likes/retweets with 0.
    Return a clean list of tweets.
    """
    clean_tweets = []
    removed = 0
    fixed = 0

    for tweet in tweets:
        if tweet["Text"] is None or tweet["Text"].strip() == "":
            removed = removed + 1
            continue

        if tweet["Likes"] is None or tweet["Likes"].strip() == "":
            tweet["Likes"] = 0
            fixed = fixed + 1

        if tweet["Retweets"] is None or tweet["Retweets"].strip() == "":
            tweet["Retweets"] = 0
            fixed = fixed + 1

        tweet["Likes"] = int(tweet["Likes"])
        tweet["Retweets"] = int(tweet["Retweets"])
        clean_tweets.append(tweet)

    print("Data cleaning is being done.....:")
    time.sleep(2)
    print(f"     Removed {removed} tweets with no text.")
    print(f"     Fixed {fixed} blank Likes or Retweets values.\n\n")
    return clean_tweets


def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    """
    if len(tweets) == 0:
        print("No tweets to check.")
        return

    most_liked_tweet = tweets[0]
    for tweet in tweets:
        if tweet["Likes"] > most_liked_tweet["Likes"]:
            most_liked_tweet = tweet

    print("Most viral tweet:")
    print(f"  Username: {most_liked_tweet['Username']}")
    print(f"  Likes: {most_liked_tweet['Likes']}")
    well_indented = most_liked_tweet['Text'].replace("\n", "\n    ")
    print(f"  Text:\n    {well_indented}\n\n")


def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list
    by 'Likes' in descending order. NO .sort() allowed!
    """
    sorted_tweets = []
    for tweet in tweets:
        sorted_tweets.append(tweet)

    total_tweets = len(sorted_tweets)
    for position in range(total_tweets):
        most_likes_position = position
        for next_position in range(position + 1, total_tweets):
            if sorted_tweets[next_position]["Likes"] > sorted_tweets[most_likes_position]["Likes"]:
                most_likes_position = next_position
        sorted_tweets[position], sorted_tweets[most_likes_position] = sorted_tweets[most_likes_position], sorted_tweets[position]

    return sorted_tweets


def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    matching_tweets = []
    for tweet in tweets:
        if keyword.lower() in tweet["Text"].lower():
            matching_tweets.append(tweet)

    time.sleep(2)
    if len(matching_tweets) == 1:
        print(f'Found 1 tweet containing "{keyword}":')
    else:
        print(f'Found {len(matching_tweets)} tweets containing the word "{keyword}":')
    for tweet in matching_tweets:
        print(f"By @{tweet['Username']}\n{tweet['Text']}")
        print("______________________________________________________________\n")
    return matching_tweets


if __name__ == "__main__":
    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")

    if len(dataset) == 0:
        print("The file is empty. Nothing to analyze.")
        sys.exit(0)

    print("          QUEST 1          ")
    print("____________________________\n")
    clean_dataset = clean_data(dataset)

    print("          QUEST 2          ")
    print("____________________________\n")
    find_viral_tweet(clean_dataset)

    print("          QUEST 3          ")
    print("____________________________\n")
    print("Sorting to get top 10 most liked tweets.....")
    sorted_dataset = custom_sort_by_likes(clean_dataset)
    top_ten = sorted_dataset[0:10]
    position = 1
    for tweet in top_ten:
        print(f"{position}. {tweet['Likes']} likes - @{tweet['Username']}")
        position = position + 1
    print("\n\n")

    print("          QUEST 4          ")
    print("____________________________\n")
    keyword = input("Enter a word to search for: ")
    print("Searching for your word..........:\n")
    search_tweets(clean_dataset, keyword)
