import requests
import json
import os
import random

def load_posts():
    with open('posts.json', 'r') as f:
        return json.load(f)

def post_to_facebook(message):
    page_id = os.getenv('FB_PAGE_ID')
    access_token = os.getenv('FB_PAGE_ACCESS_TOKEN')
    
    if not page_id or not access_token:
        print('Missing Facebook credentials in environment variables.')
        return False
    
    url = f'https://graph.facebook.com/v19.0/{page_id}/feed'
    params = {
        'message': message,
        'access_token': access_token
    }
    
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print('Post successful!')
        print(response.json())
        return True
    else:
        print('Failed to post:', response.text)
        return False

if __name__ == '__main__':
    posts = load_posts()
    selected = random.choice(posts)
    full_message = f"{selected['quote']}\n\n{selected['explanation']}\n\n#NEMT #MedicalTransport #CareOnWheels"
    post_to_facebook(full_message)