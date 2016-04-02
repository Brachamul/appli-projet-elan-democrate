from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

	'''Build user urls with username instead of pk so that people
	can be found with /users/username/ rather than /users/5/ '''

	url = serializers.HyperlinkedIdentityField(
		view_name='user-detail',
		lookup_field='username'
	)

	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')