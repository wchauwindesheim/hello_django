from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

@require_http_methods(['GET', 'POST'])
def UpdateServerView(request):
    if request.method == 'POST':
        # Do something here to update the server
        return HttpResponse('Server updated successfully')
    else:
        return HttpResponse('Method not allowed')
    