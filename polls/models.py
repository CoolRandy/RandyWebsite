from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Poll(models.Model):
	"""docstring for ClassName"""

	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

	def __unicode__(self):
		return self.question
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg


class Choice(models.Model):
	"""docstring for ClassName"""
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg
						