from rest_framework.decorators import api_view
from rest_framework.response import Response
from portfolio.models.services_models import Service
from portfolio.Serializer.services_serializers import ServiceSerializer

@api_view(['GET'])
def service_list(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)