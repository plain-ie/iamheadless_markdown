import json

from django.shortcuts import HttpResponse
from django.template.loader import render_to_string
from django.views import views

from .conf import settings


class MarkdownRenderViewSet(View):

    template = f'{settings.APP_NAME}/base.html'

    def get(self, request):

        text = ''
        markdown_elements = settings.WIDGET_REGISTRY.parse(text)

        response_data = {
            'text': text,
            'html': render_to_string(self.temaplte, context={'elements': markdown_elements}),
        }

        return HttpResponse(
            json.dumps(response_data),
            status=200,
            content_type='application/json'
        )
