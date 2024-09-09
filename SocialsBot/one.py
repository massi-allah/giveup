from .X.main import X
from .Telegram.main import Telegram
from .Meta.MetaClient import MetaClient

message = "Hello World!"


def combine_job_descriptions(job_versions):
    # Combined content with dynamic values
    job_fa = job_versions[0]
    job_ps = job_versions[1]
    job_en = job_versions[2]
    # Combine all job descriptions into one string
    combined_content = "\n".join([job_fa.strip(), job_ps.strip(), job_en.strip()])
    return combined_content



def send_to_the_world(message, image):

    if message == None or image == None:
        print("Message or Image is None")
        return False
    else:
        combined_message = combine_job_descriptions(message)

        f = MetaClient()
        f.post_image_to_facebook(image, combined_message)
        f.post_image_to_instagram(image, combined_message)

        x_com = X()
        job_fa, job_ps, job_en = message
        x_com.tweet_thread(job_fa.strip(), job_ps.strip(), job_en.strip())

        telegram_obj = Telegram()
        telegram_obj.sendMessage(combined_message)

        print(f"The World Knows About {combined_message}")
        return True
    
