from rest_framework import serializers

from .models import Proposition
from users.serializers import UserSerializer


class PropositionSerializer(serializers.HyperlinkedModelSerializer):

	author = UserSerializer()

	class Meta:
		model = Proposition
		fields = (
			'slug', 'title', 'author', 'content',
			'status', 'date_created', 'url'
			)
		read_only_fields = ('slug', 'author', 'status', 'date_created')