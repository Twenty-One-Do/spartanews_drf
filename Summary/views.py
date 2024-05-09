from django.http import JsonResponse
from .utils import fetch_webpage, parse_webpage
from .summarization import generate_summary

def summarize(request):
    url = request.GET.get('url')
    if not url:
        return JsonResponse({'error': 'No URL provided'}, status=400)

    html_content = fetch_webpage(url)
    if html_content:
        title, paragraphs = parse_webpage(html_content)
        full_text = ' '.join(paragraphs)
        summary = generate_summary(full_text)
        bullet_points = summary.split('. ')  # Assume each sentence ends with '.'
        return JsonResponse({'title': title, 'bullet_points': bullet_points})
    else:
        return JsonResponse({'error': 'Failed to fetch the webpage'}, status=500)
