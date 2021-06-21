from django.core import validators 
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
	name = models.CharField(max_length=80)
	code = models.CharField(max_length=2)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Countries'

class Address(models.Model):
	street = models.CharField(max_length=100)
	pincode = models.CharField(max_length=100)
	city = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.city} {self.street} {self.pincode}'

	class Meta:
		verbose_name_plural = 'Address Entries'

class Author(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class Book(models.Model):
	title = models.CharField(max_length=50)
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
	is_bestselling = models.BooleanField(default=False)
	slug = models.SlugField(default='', blank=True, null=False)
	published_countries = models.ManyToManyField(Country, null=False, related_name="books")

	def get_absolute_url(self):
		return reverse('book_info', args=[self.slug])

	def __str__(self):
		return f'{self.title} ({self.rating})'
	