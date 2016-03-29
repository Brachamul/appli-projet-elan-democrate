from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

	def retrieve(self, request, pk=None):
		if pk == 'i':
			return Response(UserSerializer(request.user,
				context={'request':request}).data)
		return super(UserViewSet, self).retrieve(request, pk)

@api_view(['GET'])
def me(request):
	''' Gets the current user info '''
	return Response(UserSerializer(request.user, context={'request':request}).data)