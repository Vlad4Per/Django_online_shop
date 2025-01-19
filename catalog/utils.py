from django.contrib.postgres.search import SearchVector

from catalog.models import Product
from django.db.models import Q


def q_search(query):

    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))

    return Product.objects.annotate(search=SearchVector(
        "name", "description"
    )).filter(search=query)


    # tokens = list(filter(lambda x:len(x)>2,query.split()))
    #
    # qs = Q()
    # for token in tokens:
    #     qs |= Q(description__icontains=token)
    #     qs |= Q(name__icontains=token)
    # return Product.objects.filter(qs)