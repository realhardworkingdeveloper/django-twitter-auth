from django.db import models
import re

class User(models.Model):
	username = models.CharField(max_length=40)
	email = models.EmailField()
	oauth_token = models.CharField(max_length=200)
	oauth_token_secret = models.CharField(max_length=200)

	def validate(self):
		errors = []
		if self.username and not re.compile('^[a-zA-Z0-9_]{1,40}$').match( \
			self.username):
			errors += ['username']
		if self.email and not re.compile( \
			'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$').match( \
			self.email):
			errors += ['email']
		return errors
