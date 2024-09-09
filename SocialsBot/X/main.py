import tweepy
from dotenv import load_dotenv
import os


class X:
    def __init__(self) -> None:
        # Authenticate to Twitter (X)
        load_dotenv()
        self.client = tweepy.Client(
            consumer_key=os.getenv("CONSUMER_KEY"),
            consumer_secret=os.getenv("CONSUMER_KEY_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
        )

    def tweet(self, tweet, reply_to_tweet_id=None):
        """
        Post a tweet on X (Twitter). If `reply_to_tweet_id` is provided,
        the tweet will be posted as a reply to that tweet, forming a thread.
        """
        try:
            response = self.client.create_tweet(text=tweet, in_reply_to_tweet_id=reply_to_tweet_id)
            tweet_id = response.data['id']
            print(f"Tweet made successfully with ID {tweet_id}: {tweet[:30]}...")
            return tweet_id  # Return the ID of the tweet for threading
        except Exception as e:
            print(f"Error occurred while tweeting: {e}")
            return None

    def tweet_thread(self, job_fa, job_ps, job_en):
        """
        Create a thread of tweets with three job descriptions in different languages.
        """
        # Start the thread with the first tweet (Persian job description)
        fa_tweet_id = self.tweet(job_fa)
        if not fa_tweet_id:
            return  # Exit if the first tweet fails

        # Tweet the Pashto job description as a reply to the Persian tweet
        ps_tweet_id = self.tweet(job_ps, reply_to_tweet_id=fa_tweet_id)
        if not ps_tweet_id:
            return  # Exit if the second tweet fails

        # Tweet the English job description as a reply to the Pashto tweet
        self.tweet(job_en, reply_to_tweet_id=ps_tweet_id)




# use for reference to add new job
def get_job_descriptions():
    """
    Returns job descriptions in Persian (FA), Pashto (PS), and English (EN) languages.
    Replace placeholders with actual dynamic values.
    """
    job_fa = """
    🌟 اعلان کاریابی 🌟

    📢 فرصت شغلی: مدیر پروژه  
    🏢 سازمان: شرکت XYZ  
    📍 مکان: تهران  
    🗓️ آخرین مهلت درخواست: 30 سپتامبر  
    🚀 همین حالا اقدام کنید!
    """

    job_ps = """
    🌟 دندې فرصت 🌟

    📢 دندې فرصت: د پروژې مدیر  
    🏢 اداره: XYZ شرکت  
    📍 ځای: کابل  
    🗓️ د غوښتنلیک وروستۍ نېټه: ۳۰ سپتمبر  
    🚀 همدا اوس غوښتنه وکړئ!
    """

    job_en = """
    🌟 Job Opportunity 🌟

    📢 Job Opportunity: Project Manager  
    🏢 Organization: XYZ Company  
    📍 Location: New York  
    🗓️ Application Deadline: September 30  
    🚀 Apply now to make a difference!
    """

    return job_fa.strip(), job_ps.strip(), job_en.strip()


if __name__ == "__main__":
    x = X()
    job_fa, job_ps, job_en = get_job_descriptions()
    x.tweet_thread(job_fa, job_ps, job_en)
