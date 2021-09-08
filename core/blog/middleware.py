from django.utils.decorators import sync_and_async_middleware
from .submodels.base import IpAdress
class SaveIpAdress:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
    # One-time configuration and initialization goes here.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        try :
            ip_address = IpAdress.objects.get(ip_address=ip)
        except IpAdress.DoesNotExist :
            ip_address = IpAdress(ip_address = ip)
            ip_address.save()
        request.user.ip_address = ip_address
        response = self.get_response(request)
        return response