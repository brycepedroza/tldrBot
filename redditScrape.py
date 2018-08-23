from newspaper import Article
import praw
import newspaper

reddit = praw.Reddit(client_id = 'VUBWeNzicck3aA', \
                     client_secret = 'IryoLwff-CUd13JgFHT8Ea8MGCg', \
                     user_agent = 'tldrBot', \
                     username = 'articleTldrBot', \
                     password = 'Bryc3R3dditBot')

subreddit = reddit.subreddit('politics')
for submission in subreddit.hot(limit = 10):
    if submission.stickied is False:
        print('\n', submission.url, '\tARTICLE START')
        url = submission.url
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        print(article.summary)
    else:
        print(submission.url, '\t Stickied')

# Maybe I want to check if an article has tweets in it?
# Get author and content of the tweet?

print(newspaper.hot())
