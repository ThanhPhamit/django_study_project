from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View


# def handler404(request, exception):
#     return HttpResponseNotFound("404: Page not found!")

class MyView(View):
    def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        return HttpResponse("Hello async world!")

    def handler404(request, exception):
        return HttpResponseNotFound("404: Page not found!")
