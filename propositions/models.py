import uuid

from django.db import models

from django.contrib.auth.models import User

from autoslug.fields import AutoSlugField

PROPOSITION_STATUSES = [
	('NEW', 'nouvelle proposition'),
	('REMOVED', 'proposition supprimée'),
	('LOCKED', 'proposition verrouillée'),
	('EXPIRED', 'proposition expirée'),
	('VOTING', 'proposition soumise au vote'),
	('ACCEPTED', 'proposition adoptée'),
	('DENIED', 'proposition retoquée'),
	]

class Proposition(models.Model):
	title = models.CharField(max_length=120)
	author = models.ForeignKey(User)
	content = models.CharField(max_length=5120)
#	tags ?
	slug = AutoSlugField(
		primary_key=True, populate_from=('title'),
		unique=True, editable=True, max_length=120
		)
	status = models.CharField(
		max_length=24, choices=PROPOSITION_STATUSES, default="NEW"
		)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title