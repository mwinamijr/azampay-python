from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests

from decouple import config

@api_view(['GET'])
def generate_token(request):
    baseUrl = config('BASE_URL')
    appName = config('APP_NAME')
    clientId = config('CLIENT_ID')
    clientSecret = config('CLIENT_SECRET')
    response = requests.post(baseUrl, {appName: appName, clientId: clientId, clientSecret: clientSecret})
    
    return Response(response)