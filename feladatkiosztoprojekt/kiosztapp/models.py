from django.db import models

# Create your models here.

class Tetel(models.Model):
	tenev = models.CharField(max_length=100)
	def __str__(self):
		return self.tenev

class Tanulo(models.Model):
	tanev = models.CharField(max_length=100)
	jelszo = models.CharField(max_length=20)
	def __str__(self):
		return f"{self.tanev} - {self.jelszo}"


class Valasztott(models.Model):
	tetelid = models.ForeignKey(Tetel, on_delete=models.CASCADE, blank = True, null = True)
	tanuloid = models.ForeignKey(Tanulo, on_delete=models.CASCADE, blank = True, null = True)
	def __str__(self):
		return f"{self.tetelid.tenev} ==> {self.tanuloid.tanev}"

