from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .facebook import FacebookError, get_all_page_posts


@require_GET
def index(request):
    return render(request, 'posts/index.html')


@require_GET
def page_posts(request):
    limit = request.GET.get('limit')
    try:
        max_posts = int(limit) if limit else None
    except ValueError:
        return JsonResponse({'error': 'limit must be an integer'}, status=400)

    try:
        posts = get_all_page_posts(max_posts=max_posts)
    except FacebookError as exc:
        return JsonResponse({'error': str(exc)}, status=502)

    return JsonResponse({'count': len(posts), 'posts': posts})
