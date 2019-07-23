from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from server.core.models import Link
from server.core.serializers import LinkSerializer


def get_metadata(url):
    return {
        'url': url,
        'category': 'software',
        'title': 'Github - augustogoulart/involved',
        'description': 'Learn modern web development on Instagram while '
                       'building an app for online communities'
    }


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
