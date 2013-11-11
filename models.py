from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	text = models.TextField()
	slug = models.SlugField(max_length=40, unique=True)
	author = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

	class Meta:
	    ordering = ["-pub_date"]

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

class CategoryToEntry(models.Model):
    entry = models.ForeignKey(Entry)
    category = models.ForeignKey(Category)