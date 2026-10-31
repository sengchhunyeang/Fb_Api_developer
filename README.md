# Fb_Api_developer

Django project that gets all posts from a Facebook Page with the Graph API and shows them on a web page and as a JSON API.

## Quick start

```
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
copy .env.example .env      # then fill in your Page ID and Page token
.venv\Scripts\python manage.py migrate
.venv\Scripts\python manage.py runserver
```

- UI: http://127.0.0.1:8000/
- API: http://127.0.0.1:8000/api/posts/ (`?limit=20` for the newest 20)

## Setup guide

Step-by-step guide for creating the Facebook app and getting a Page token that never expires:
[docs/facebook-posts-setup.html](docs/facebook-posts-setup.html)

Khmer version (ភាសាខ្មែរ): [docs/facebook-posts-setup-km.html](docs/facebook-posts-setup-km.html)
