from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
	#student_id = models.IntegerField()
	student_id = models.CharField(max_length=200,primary_key=True)
	max_limit = models.IntegerField()
	total_fine = models.IntegerField()
	password = models.CharField(max_length=32)
    
	

class Book(models.Model):
	isbn = models.CharField(max_length=17, primary_key=True)
	name = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	status = models.CharField(max_length=200)
	def __str__(self):
		return self.isbn
class Borrow(models.Model):
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
	due_date = models.DateTimeField(datetime.date.today() + datetime.timedelta(days=15))
    
class Staff(models.Model):
	staff_id = models.CharField(max_length=200,primary_key=True)
	password = models.CharField(max_length=32)
	name = models.CharField(max_length=200)
	designation = models.CharField(max_length=100)
