from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student,Staff,Book,Borrow
from django.core.exceptions import ObjectDoesNotExist
import datetime
# Create your views here.
def index(request):
     return render(request,'library_system/index.html')
     #return HttpResponse("Welcome to Online Library Portal")

def role(request):
     if request.method=='POST':
          if request.POST.get('roletype')=='1':
               return render(request,'library_system/studentlogin.html')
          else:
               return render(request,'library_system/stafflogin.html')
     return render(request,'library_system/index.html')

def stafflogin(request):
     if request.method=='POST':
          staffid=request.POST.get('staffID')
          staffpwd=request.POST.get('staffPwd')
          try:
               staffobj=Staff.objects.get(staff_id=staffid,password=staffpwd)
               return render(request,'library_system/staffOptions.html')
          except ObjectDoesNotExist:
               return render(request,'library_system/loginerror.html')

def studentlogin(request):
     if request.method=='POST':
          studentid=request.POST.get('studentID')
          studentpwd=request.POST.get('studentPwd')
          try:
               studentobjobj=Student.objects.get(student_id=studentid,password=studentpwd)
               return render(request,'library_system/studentOptions.html',{'studentID':studentid})
          except ObjectDoesNotExist:
               return render(request,'library_system/loginerror.html')

def staffactions(request):
     if request.method=='POST':
         if request.POST.get('staffchoice')=='viewbooks':
              booklist=Book.objects.all()
              return render(request,'library_system/booklist.html',{'booklist':booklist})
         
         if request.POST.get('staffchoice')=='addBook':
              isbn=request.POST.get('bookisbn')
              name=request.POST.get('bookname')
              author=request.POST.get('bookauthor')
              status="AVAILABLE"
              book_obj=Book(isbn=isbn,name=name,author=author,status=status)
              book_obj.save()
              message="Book Added Successfully"
              return render(request,'library_system/message.html',{'message':message})
         if request.POST.get('staffchoice')== 'deletebook':
               isbn=request.POST.get('bookdelisbn')
               book_obj=Book.objects.get(isbn=isbn)
               if book_obj.status == "BORROWED":
                    message="Currently Borrowed by Student,Deletion unsuccessful"
                    return render(request,'library_system/message.html',{'message':message})
               else:
                    book_obj.delete()
                    message="Deletion Successful"
                    return render(request,'library_system/message.html',{'message':message})

def studentactions(request,studentID):
     if request.method=='POST':
          if request.POST.get('studentchoice')=='viewbooks':
               booklist=Book.objects.all()
               return render(request,'library_system/booklist.html',{'booklist':booklist})
          
          if request.POST.get('studentchoice')=='borrowBook':
               booklist=Book.objects.all().filter(status='AVAILABLE')
               return render(request,'library_system/borrowedBooks.html',{'booklist':booklist,'studentID':studentID})

          if request.POST.get('studentchoice')=='returnbook':
               booklist=Borrow.objects.all().filter(student_id=studentID)
               #booklist = Book.objects.filter(isbn = Borrow.objects.filter(student_id=studentID))
               return render(request,'library_system/returnBooks.html',{'booklist':booklist,'studentID':studentID})

def borrowbook(request, studentID):
     if request.method=='POST':
          book_isbn = request.POST.get('bookchoice') 

          try:
              book_obj = Borrow(isbn=Book.objects.get(isbn= book_isbn), student_id=Student.objects.get(student_id=studentID), due_date = (datetime.date.today() + datetime.timedelta(days=15))) 
              book_obj.save()

              book_obj2 = Book.objects.get(isbn= book_isbn)
              book_obj2.status = "BORROWED"
              book_obj2.save()
              message="Book Issued!"
              return render(request,'library_system/message.html',{'message':message})

          except ObjectDoesNotExist:
              return render(request,'library_system/loginerror.html')
          
def returnbook(request, studentID):
     if request.method=='POST':
          book_isbn = request.POST.get('bookchoice') 

          try:
              
              borrow_obj = Borrow.objects.get(isbn=Book.objects.get(isbn=book_isbn))       
              borrow_obj.delete()

              book = Book.objects.get(isbn=book_isbn)
              book.status = "AVAILABLE"
              book.save()
              message="Book Returned"
              return render(request,'library_system/message.html',{'message':message})      
          except ObjectDoesNotExist:
              return render(request,'library_system/loginerror.html')