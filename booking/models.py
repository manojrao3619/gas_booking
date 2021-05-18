from django.db import models

class Booking(models.Model):
	consumer_name = models.CharField(max_length = 30)
	consumer_no   = models.CharField(max_length = 20)
	phone_no      = models.CharField(max_length = 10)
	date          = models.DateField(null = True)
	time          = models.TimeField(null = True)
	status        = models.CharField(null = True ,max_length = 20)

	def __str__(self):
		return self.consumer_no

