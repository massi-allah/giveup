import requests
import os
from dotenv import load_dotenv
from .AccessTokenManager import FacebookTokenManager
from .ImgurClient import ImgurUploader

class MetaClient:
    def __init__(self) -> None:
        # Refreshing the Access token
        token_manager = FacebookTokenManager()
        token_manager.refresh_access_token()

        load_dotenv()
        # Page access token and page ID
        self.page_access_token = os.getenv("PAGE_ACCESS_TOKEN")
        self.page_id = os.getenv("PAGE_ID")
        self.insta_page_id = os.getenv("INSTA_PAGE_ID")

    def make_post_to_facebook(self, message):
        # The endpoint to post a message to the feed
        url = f'https://graph.facebook.com/{self.page_id}/feed'

        # Parameters for the POST request
        params = {
            'access_token': self.page_access_token,
            'message': message
        }

        try:
            # Make the POST request to publish the content
            response = requests.post(url, params=params)
            # Print the response
            print("Facebook Post Made.")
            print(response.json())
        except Exception as e:
            print(e)

    def post_image_to_facebook(self, image_path, caption):
        # The endpoint to post an image
        url = f'https://graph.facebook.com/{self.page_id}/photos'

        # Open the image file
        with open(image_path, 'rb') as image_file:
            files = {
                'file': image_file
            }
            # Parameters for the POST request
            params = {
                'access_token': self.page_access_token,
                'caption': caption
            }

            try:
                # Make the POST request to publish the image
                response = requests.post(url, files=files, data=params)
                # Print the response
                print("Facebook Image Post Made.")
                print(response.json())

            except Exception as e:
                print(e)


    def post_image_to_instagram(self, img, caption):
        imgurImgs = ImgurUploader()
        image_url = imgurImgs.upload_to_imgur(img)
        if img:
            # Step 1: Upload the image to Instagram
            url = f'https://graph.facebook.com/v20.0/{self.insta_page_id}/media'
            params = {
                'access_token': self.page_access_token,
                'image_url': image_url,
                'caption': caption
            }

            try:
                response = requests.post(url, params=params)
                result = response.json()
                print("Instagram Image Upload Response:")
                print(result)
                
                # Step 2: Publish the uploaded image
                if 'id' in result:
                    creation_id = result['id']
                    publish_url = f'https://graph.facebook.com/v20.0/{self.insta_page_id}/media_publish'
                    publish_params = {
                        'creation_id': creation_id,
                        'access_token': self.page_access_token
                    }
                    publish_response = requests.post(publish_url, data=publish_params)
                    publish_result = publish_response.json()
                    print("Instagram Image Post Made.")
                    print(publish_result)
                    
                    # Save the link of the image after publishing to self.image_post
                    self.image_post = f"https://www.instagram.com/p/{publish_result.get('id')}/"
                    print("Image URL:", self.image_post)
                else:
                    print("Failed to upload image to Instagram:", result)
            except Exception as e:
                print(e)
        else:
            print("Provide Image!!")


if __name__ == "__main__":
    f = MetaClient()
    # Post a message
    # f.make_post("The Best Animal in the world is Called Deer!")
    # Post an image with a caption
    # f.post_image_to_facebook("./abc.jpg", "This is an amazing art!")

    # imgurImgs = ImgurUploader()  # instagram api require the image to be in a public library // does not support direct upload
    # img = imgurImgs.upload_to_imgur("./abc.jpg")
    # if img:
    #     f.post_image_to_instagram(img, "This is an amazing art!")
