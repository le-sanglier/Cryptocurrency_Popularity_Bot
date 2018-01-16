import re
import random
import os
import threading
import codecs
import csv
import praw
import copy

def comment_loop():
    for comment in subreddit.stream.comments():
        for coin in cryptos:
            normalized_comment = comment.body.lower()
            normalized_coin = coin.lower()
            normalized_coin = ''.join(e for e in normalized_coin if e.isalnum())
            normalized_coin = " " + normalized_coin + " "
            if normalized_coin in normalized_comment:
                index = cryptos.index(coin)
                index = int(index/2)
                coins_count[index] = (coins_count[index][0], coins_count[index][1] + 1)
                print("comment")
                # print(coin.lower())
                # print(comment.body)
                print("----------------------------------------------------------")
                sorted_coins = copy.copy(coins_count)
                sorted_coins = sorted(sorted_coins, key=lambda x: x[1])
                sorted_coins.reverse()
                #print(sorted_coins)
                with open("top_10.txt", "w") as f:
                    f.write(str(sorted_coins[0:19]))


def submision_loop():
    for submission in subreddit.stream.submissions():
        for coin in cryptos:
            normalized_submission_body = submission.selftext.lower()
            normalized_submission_title = submission.title.lower()
            normalized_coin = coin.lower()
            normalized_coin = ''.join(e for e in normalized_coin if e.isalnum())
            normalized_coin = " " + normalized_coin + " "
            if normalized_coin in normalized_submission_body:
                index = cryptos.index(coin)
                index = int(index/2)
                coins_count[index] = (coins_count[index][0], coins_count[index][1] + 10)
                print("post body")
                #print(coin.lower())
                #print(normalized_submission_body)
                print("----------------------------------------------------------")
                sorted_coins = copy.copy(coins_count)
                sorted_coins = sorted(sorted_coins, key=lambda x: x[1])
                sorted_coins.reverse()
                #print(sorted_coins)
                with open("top_10.txt", "w") as f:
                    f.write(str(sorted_coins[0:19]))
            if normalized_coin in normalized_submission_title:
                index = cryptos.index(coin)
                index = int(index/2)
                coins_count[index] = (coins_count[index][0], coins_count[index][1] + 10)
                print("post title")
                #print(coin.lower())
                #print(normalized_submission_title)
                print("----------------------------------------------------------")
                sorted_coins = copy.copy(coins_count)
                sorted_coins = sorted(sorted_coins, key=lambda x: x[1])
                sorted_coins.reverse()
                #print(sorted_coins)
                with open("top_10.txt", "w") as f:
                    f.write(str(sorted_coins[0:19]))



reddit = praw.Reddit('HYPE_BOT')
subreddit = reddit.subreddit("cryptocurrency")

cryptos = []
coins_count = []
top_10 = []

with codecs.open('coins.csv', 'r', encoding='utf-8') as inputcsvfile:              #pull in input data from csv
    csv_input = csv.reader(inputcsvfile, delimiter=",")
    for row in csv_input:
        cryptos.append(str(row))

for x in range(0, len(cryptos), 2):
    coins_helper = (cryptos[x], 0)
    coins_count.append(coins_helper)

p1 = threading.Thread(target=comment_loop)
p2 = threading.Thread(target=submision_loop)

p1.start()
p2.start()






# coins_abv[0] = (coins_abv[0][0], coins_abv[0][1], coins_abv[0][2] + 1)
# print(coins_abv[0][2])
# print(coins_abv[0])
