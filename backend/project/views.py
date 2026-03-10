from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Document
from .services import get_embedding
from .cache import get_cache, set_cache
from django.db.models import Q


# ----------------------------
# Keyword Search API
# ----------------------------
@api_view(["GET"])
def keyword_search(request):

    query = request.GET.get("q")

    cache_key = f"keyword:{query}"

    cached = get_cache(cache_key)


    if cached:
        return Response(cached)

    docs = Document.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
    )[:5]

    results = [
        {"title": d.title, "content": d.content}
        for d in docs
    ]

    set_cache(cache_key, results)

    return Response(results)


# ----------------------------
# Semantic Search API
# ----------------------------
@api_view(["GET"])
def semantic_search(request):

    query = request.GET.get("q")

    cache_key = f"semantic:{query}"

    cached = get_cache(cache_key)

    if cached:
        return Response(cached)

    query_embedding = get_embedding(query)

    docs = Document.objects.raw("""
        SELECT id, title, content,
        embedding <=> %s::vector AS distance
        FROM project_document
        ORDER BY distance
        LIMIT 5
    """, [query_embedding])

    results = []

    for d in docs:
        results.append({
            "title": d.title,
            "content": d.content,
            "score": 1 - d.distance
        })

    set_cache(cache_key, results)

    return Response(results)