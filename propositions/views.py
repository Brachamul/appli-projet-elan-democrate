from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions

from .models import Proposition
from .serializers import PropositionSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class PropositionViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows propositions to be viewed or edited.
	"""
	
	def perform_create(self, serializer):
		serializer.save(author=self.request.user, status="NEW")

	queryset = Proposition.objects.all().order_by('-date_created')
	serializer_class = PropositionSerializer
	permission_classes = (
		permissions.IsAuthenticatedOrReadOnly,
		IsAuthorOrReadOnly,
		)