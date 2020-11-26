from django.db import models

# Create your models here.

class Tetel(models.Model):
	"""docstring for Tetel"""
	def __init__(self, arg):
		super(Tetel, self).__init__()
		self.arg = arg
	
	tenev = models.CharField(max_length=100)

class Tanulo(models.Model):
	"""docstring for Tanulo"""
	def __init__(self, arg):
		super(Tanulo, self).__init__()
		self.arg = arg
	tanev = models.CharField(max_length=100)
	jelszo = models.CharField(max_length=20)


class Valasztott(models.Model):
	"""docstring for Valasztott"""
	def __init__(self, arg):
		super(Valasztott, self).__init__()
		self.arg = arg
	tetelid = models.ForeignKey(Tetel, on_delete=models.CASCADE, blank = True, null = True)
	tanuloid = models.ForeignKey(Tanulo, on_delete=models.CASCADE, blank = True, null = True)
