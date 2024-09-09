import os
from imgurpython import ImgurClient
from dotenv import load_dotenv

class ImgurUploader:
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("IMGUR_CLIENT_ID")
        self.client_secret = os.getenv("IMGUR_CLIENT_SECRET")
        self.client = ImgurClient(self.client_id, self.client_secret)

    def upload_to_imgur(self, image_path):
        try:
            # Upload image to Imgur
            image = self.client.upload_from_path(image_path, anon=True)
            # Return the URL of the uploaded image
            return image['link']
        except Exception as e:
            print("Error uploading image to Imgur:", e)
            return None

if __name__ == "__main__":
    imgur_uploader = ImgurUploader()
    local_image_path = "./abc.jpg"  # Replace with the actual path

    public_image_url = imgur_uploader.upload_to_imgur(local_image_path)
    if public_image_url:
        print("Public Image URL:", public_image_url)
    else:
        print("Failed to upload image.")
