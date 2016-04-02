from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from propositions.views import *
from users.views import *

router = routers.DefaultRouter()
router.register(r'propositions', PropositionViewSet)
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^me/$', me, name='me'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^obtain-auth-token/$', obtain_auth_token),
	url(r'^', include(router.urls)),
]

