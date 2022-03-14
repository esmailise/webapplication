from .models import AboutUs
def test_send(request):
    about_send = AboutUs.objects.all()
    return {'about':about_send}
    