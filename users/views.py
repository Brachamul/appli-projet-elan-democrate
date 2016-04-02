from django.contrib.auth.models import User

from rest_framework import viewsets, renderers
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, detail_route, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	lookup_field = 'username' # get users by username instead of pk

@api_view(['GET'])
@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def me(request):
	''' Gets the current user info '''
	return Response(UserSerializer(request.user, context={'request':request}).data)