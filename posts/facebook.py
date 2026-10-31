import requests
from django.conf import settings

GRAPH_URL = 'https://graph.facebook.com'
POST_FIELDS = 'id,message,created_time,permalink_url,full_picture,status_type'


class FacebookError(Exception):
    pass


def get_all_page_posts(max_posts=None):
    """Fetch every post on the page, following Graph API pagination."""
    if not settings.FACEBOOK_PAGE_ID or not settings.FACEBOOK_PAGE_ACCESS_TOKEN:
        raise FacebookError('FACEBOOK_PAGE_ID and FACEBOOK_PAGE_ACCESS_TOKEN must be set in .env')

    url = f'{GRAPH_URL}/{settings.FACEBOOK_GRAPH_VERSION}/{settings.FACEBOOK_PAGE_ID}/posts'
    params = {
        'fields': POST_FIELDS,
        'limit': 100,
        'access_token': settings.FACEBOOK_PAGE_ACCESS_TOKEN,
    }
    posts = []

    while url:
        response = requests.get(url, params=params, timeout=30)
        data = response.json()
        if 'error' in data:
            raise FacebookError(data['error'].get('message', 'Unknown Graph API error'))

        posts.extend(data.get('data', []))
        if max_posts and len(posts) >= max_posts:
            return posts[:max_posts]

        # The "next" URL already contains all query params, including the token.
        url = data.get('paging', {}).get('next')
        params = None

    return posts
