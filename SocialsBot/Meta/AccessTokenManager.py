import requests
from dotenv import load_dotenv, set_key
import os

class FacebookTokenManager:
    def __init__(self):
        load_dotenv()
        self.app_id = os.getenv("APP_ID")
        self.app_secret = os.getenv('APP_SECRET')
        self.short_lived_access_token = os.getenv('PAGE_ACCESS_TOKEN')
    
    def get_long_lived_access_token(self):
        url = 'https://graph.facebook.com/v20.0/oauth/access_token'
        params = {
            'grant_type': 'fb_exchange_token',
            'client_id': self.app_id,
            'client_secret': self.app_secret,
            'fb_exchange_token': self.short_lived_access_token
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Response content: {response.content}")  # Print full response content for debugging
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        return None

    def update_env_file(self, key, value):
        try:
            set_key(self.env_file, key, value)
            print(f"Updated {key} in {self.env_file}")
        except Exception as e:
            print(f"Failed to update .env file: {e}")

    def refresh_access_token(self):
        long_lived_token_response = self.get_long_lived_access_token()
        if long_lived_token_response and 'access_token' in long_lived_token_response:
            new_long_lived_token = long_lived_token_response['access_token']
            # Update the .env file with the new token
            self.update_env_file('PAGE_ACCESS_TOKEN', new_long_lived_token)
            print('Updated Long-Lived Access Token')
        else:
            print('Error obtaining long-lived access token')


if __name__ == "__main__":
    # Example usage:
    token_manager = FacebookTokenManager()
    token_manager.refresh_access_token()
