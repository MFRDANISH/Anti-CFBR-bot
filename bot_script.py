import praw

# Initialize the Reddit bot
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT'
)

# Define the subreddits you want the bot to operate on
subreddit_names = ['btechtards', 'BITSPilani']

# Monitor comments in the specified subreddits
for subreddit_name in subreddit_names:
    subreddit = reddit.subreddit(subreddit_name)
    for comment in subreddit.stream.comments():
        if 'Cfbr' in comment.body:
            reply_message = '''
            Alright, listen up, folks! We've got a real CFBR spammer on our hands in the Reddit comments, and it's driving me nuts. This sneaky little bugger tricks you into thinking they've got the answers to your burning questions, but guess what? Once you click on those juicy comments, all you get is a frickin' CFBR fest. Seriously, what a letdown! It's like expecting a delicious pizza and ending up with a stale slice of bread.

            I mean, come on! Can we have a little variety here? It's like this person thinks CFBR is the answer to everything in life. Newsflash, buddy, the world is more than just CFBR! Give us a break, and let us have some meaningful discussions without your CFBR spam polluting the comment section. It's like they've got a one-track mind and can't think beyond their precious CFBR obsession.

            So, to the CFBR spammer, here's a friendly suggestion: broaden your horizons, explore new topics, and for the love of all that's good, spare us from your CFBR overload. We want diverse conversations, not a CFBR monologue. So, go on, find something else worth talking about, and give us a break from your CFBR spam. Peace out!
            '''

            # Reply to the comment
            comment.reply(reply_message)



