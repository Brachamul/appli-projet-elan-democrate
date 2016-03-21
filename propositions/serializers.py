from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Proposition


class PropositionSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Proposition
		fields = (
			'title', 'author', 'content',
			'slug', 'status', 'date_created', 'url'
			)
		read_only_fields = ('id', 'slug', 'author', 'status')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')