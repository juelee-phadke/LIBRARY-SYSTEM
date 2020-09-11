from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def voted(request, question_id):
	if request.method=='POST':
		qstobj=Question.objects.get(pk=question_id)
		try:
			choiceobj=get_object_or_404(Choice,pk=request.POST['vote'])
		except:
			return HttpResponse("Please select an option")
		else:
			choiceobj.votes+=1
			choiceobj.save()
			return render(request,'polls/detail.html',{'question':qstobj})
	return render(request,'polls/detail.html')

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
