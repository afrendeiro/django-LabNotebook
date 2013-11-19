from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Notebook(models.Model):
	"""Notebook in which entries are.
		Ideally corresponds to a project"""
	title = models.CharField(max_length=200)
	start_date = models.DateTimeField()
	description = models.TextField(max_length=1000)
	slug = models.SlugField(max_length=40, unique=True)
	author = models.ForeignKey(User)

	class Meta:
		verbose_name_plural = "Notebooks"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/%s/" % self.slug


class Entry(models.Model):
	""" Labnotebook entry"""
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	text = models.TextField()
	slug = models.SlugField(max_length=40, unique=True)
	author = models.ForeignKey(User)
	notebook = models.ForeignKey(Notebook)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/%s/%s/%s/%s/" % (self.notebook, self.pub_date.year, self.pub_date.month, self.slug)

	class Meta:
		ordering = ["-pub_date"]
		verbose_name = _('Entry')
		verbose_name_plural = _('Entries')

class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=40, unique=True)
	description = models.TextField()

	class Meta:
		verbose_name_plural = "Categories"

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/categories/%s/" % self.slug