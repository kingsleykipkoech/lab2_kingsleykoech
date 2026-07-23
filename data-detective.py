import csv
import time

def load_tweets():
	tweets = []
	try:
		with open("twitter_dataset.csv", "r", encoding="utf-8") as file:
			reader = csv.DictReader(file)
			for row in reader:
				tweets.append(row)
	except FileNotFoundError:
		print("Error: could not find the file 'twitter_dataset.csv'.")
		print("Make sure twitter_dataset.csv is in this same folder.")
	return tweets

# Quest 1: drop tweets with no text, fill blank Likes and Retweets with 0
def clean_data(tweets):
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
    print("          QUEST 1          ")
    print("____________________________\n")
    print("Data cleaning  is being done.....:")
    time.sleep(2)
    print(f"     Removed {removed} tweets with no text.")
    print(f"     Fixed {fixed} blank Likes or Retweets values.\n \n")
    return clean_tweets


# Quest 2: find the single tweet with the most Likes
def find_most_liked(tweets):
    if len(tweets) == 0:
        print("No tweets to check.")
        return
    most_liked_tweet = tweets[0]
    for tweet in tweets:
        if tweet["Likes"] > most_liked_tweet["Likes"]:
            most_liked_tweet = tweet
    print("          QUEST 2          ")
    print("____________________________\n")
    print("Most viral tweet:")
    print(f"  Username:  {most_liked_tweet['Username']}")
    print(f"  Likes: {most_liked_tweet['Likes']}")
    well_indented = most_liked_tweet['Text'].replace("\n", "\n    ")
    print(f"Text:\n    {well_indented}\n\n")

    print("          QUEST 3           ")
    print("____________________________\n")
    print("Sorting to  get top 10 most liked tweets.....")
    

# Quest 3: Sorting to  get top 10 most liked tweet
def sort_by_likes(tweets):
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

# Quest 4: collect every tweet whose text contains the search word
def search_tweets(tweets, word):
    matching_tweets = []
    for tweet in tweets:
        if word.lower() in tweet["Text"].lower():
            matching_tweets.append(tweet)
    time.sleep(2)
    if len(matching_tweets) == 1:
        print(f'Found 1 tweet containing "{word}":')
    else:
        print(f'Found {len(matching_tweets)} tweets containing the word "{word}":')
    for tweet in matching_tweets:
        print(f"By @{tweet['Username']}\n{tweet['Text']}")
        print("______________________________________________________________\n")
    return matching_tweets


def main():
    tweets = load_tweets()
    if len(tweets) == 0:
        return  
    tweets = clean_data(tweets)
    find_most_liked(tweets)
    sorted_tweets = sort_by_likes(tweets)
    top_ten = sorted_tweets[0:10]
    position =1
    for tweet in top_ten:
        print(f"{position}. {tweet['Likes']} likes - @{tweet['Username']}")
        position =position +1
    print("\n\n")
    print("          QUEST 4          ")
    print("_____________________________\n")
    word = input("Enter a word to search for: ")
    print("Searching for your word..........:\n")
    search_tweets(tweets, word)
main()
