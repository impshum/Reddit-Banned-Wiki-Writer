import praw
import schedule
from time import sleep


client_id = 'XXXX'
client_secret = 'XXXX'
reddit_user = 'XXXX'
reddit_pass = 'XXXX'
user_agent = 'Banned wiki writer (by /u/impshum)'

target_subreddit = 'XXXX'
wiki_page = 'XXXX'
wiki_page_title = 'XXXX'


def post_to_wiki(sub, banned):
    new_wiki = '\n'.join(banned)
    new_wiki = f'### {wiki_page_title}\n{new_wiki}'
    sub.wiki[wiki_page].edit(new_wiki)
    print('Updated wiki')


def reddit_conn():
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent,
                         username=reddit_user,
                         password=reddit_pass)
    return reddit.subreddit(target_subreddit)


def main():
    banned = []
    sub = reddit_conn()

    for ban in sub.banned():
        banned.append(f'* u/{ban}: {ban.note}')

    post_to_wiki(sub, banned)


schedule.every().day.at('00:00').do(main)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every(5).to(10).days.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

main()

while True:
    schedule.run_pending()
    sleep(1)

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every(5).to(10).days.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
