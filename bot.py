import praw
import re
import random
import os
import threading

#TODO find blacklisted sites, test, change 'crypto_cust_service' to submission.author and comment.author.name, test

def comment_loop():
    for comment in subreddit.stream.comments():
        for blink in blacklist:
            normalized_comment = comment.body.lower()
            normalized_link = blink.lower()
            if normalized_link in normalized_comment:
                if comment.author in warned_users:
                    print("comment ban")
                    print(normalized_comment)
                    print("----------------------------------------------------------")
                    #ban
                    #reddit.redditor('crypto_cust_service').message('Ban for linking a blacklisted website', 'You have posted a link to a blacklisted website, and this is not your first offence.  You have been banned for X.')
                else:
                    print("comment warning")
                    print(normalized_comment)
                    print("----------------------------------------------------------")
                    with open("warned_users.txt", "a") as f:
                        f.write(comment.author.name + "\n")
                    warned_users.append(comment.author.name)
                    #reddit.redditor('crypto_cust_service').message('Blacklisted link warning', 'This is your one and only warning for posting links to blacklisted websites on r/cryptocurrency.  You can find a list of blacklisted websites here.  Another violation of this rule will result in a ban.')


        # if re.search("Blacklisted sites", comment.body, re.IGNORECASE):
        #     if comment.author.name in warned_users:
        #         #ban
        #         reddit.redditor('crypto_cust_service').message('Ban for linking a blacklisted website', 'You have posted a link to a blacklisted website, and this is not your first offence.  You have been banned for X.')
            # else:
            #     with open("warned_users.txt", "a") as f:
            #         f.write(comment.author.name + "\n")
            #     warned_users.append(comment.author.name)
            #     reddit.redditor('crypto_cust_service').message('Blacklisted link warning', 'This is your one and only warning for posting links to blacklisted websites on r/cryptocurrency.  You can find a list of blacklisted websites here.  Another violation of this rule will result in a ban.'

def submision_loop():
    for submission in subreddit.stream.submissions():
        for blink in blacklist:
            normalized_submission_body = submission.selftext.lower()
            normalized_submission_title = submission.title.lower()
            normalized_link = blink.lower()
            if normalized_link in normalized_submission_body:
                if submission.author in warned_users:
                    print("submission ban")
                    print(normalized_submission_body)
                    print("----------------------------------------------------------")
                    #ban
                    #reddit.redditor('crypto_cust_service').message('Ban for linking a blacklisted website', 'You have posted a link to a blacklisted website, and this is not your first offence.  You have been banned for X.')
                else:
                    print("submission warning")
                    print(normalized_submission_body)
                    print("----------------------------------------------------------")
                    with open("warned_users.txt", "a") as f:
                        f.write(comment.author.name + "\n")
                    warned_users.append(comment.author.name)
                    #reddit.redditor('crypto_cust_service').message('Blacklisted link warning', 'This is your one and only warning for posting links to blacklisted websites on r/cryptocurrency.  You can find a list of blacklisted websites here.  Another violation of this rule will result in a ban.')
            if normalized_link in normalized_submission_title:
                if submission.author in warned_users:
                    print("submission ban")
                    print(normalized_submission_title)
                    print("----------------------------------------------------------")
                    #ban
                    #reddit.redditor('crypto_cust_service').message('Ban for linking a blacklisted website', 'You have posted a link to a blacklisted website, and this is not your first offence.  You have been banned for X.')
                else:
                    print("submission warning")
                    print(normalized_submission_title)
                    print("----------------------------------------------------------")
                    with open("warned_users.txt", "a") as f:
                        f.write(comment.author.name + "\n")
                    warned_users.append(comment.author.name)
                    #reddit.redditor('crypto_cust_service').message('Blacklisted link warning', 'This is your one and only warning for posting links to blacklisted websites on r/cryptocurrency.  You can find a list of blacklisted websites here.  Another violation of this rule will result in a ban.')


            # if submission.author in warned_users:
            #     #ban
            #     reddit.redditor('crypto_cust_service').message('Ban for linking a blacklisted website', 'You have posted a link to a blacklisted website, and this is not your first offence.  You have been banned for X.')
            # else:
            #     with open("warned_users.txt", "a") as f:
            #         f.write(submission.author + "\n")
            #     warned_users.append(submission.author)
            #     reddit.redditor('crypto_cust_service').message('Blacklisted link warning', 'This is your one and only warning for posting links to blacklisted websites on r/cryptocurrency.  You can find a list of blacklisted websites here.  Another violation of this rule will result in a ban.'

reddit = praw.Reddit('TESTBOT')
subreddit = reddit.subreddit("cryptocurrency")
#add blacklist to list
if not os.path.isfile("warned_users.txt"):
    warned_users = []
else:
    with open("warned_users.txt", "r") as f:
        warned_users = f.read()
        warned_users = warned_users.split("\n")
        warned_users = list(filter(None, warned_users))

with open("blacklisted_sites.txt", "r") as f:
    blacklist = f.read()
    blacklist = blacklist.split("\n")
    blacklist = list(filter(None, blacklist))

p1 = threading.Thread(target=comment_loop)
p2 = threading.Thread(target=submision_loop)

p1.start()
p2.start()
