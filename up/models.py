from django.db import models

class Database(models.Model):
	user=models.CharField(max_length=99)
	introduction=models.CharField(max_length=255)
	files=models.FileField(upload_to='templates/files/')
	time=models.DateTimeField('Date Upload')
