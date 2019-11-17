from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from polls.models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views import  generic

#from  django.template import loader
# Create your views here.
'''def index(request):
	lastest_question_list=Question.objects.order_by('-pub_date')[:5]
	template='polls/index.html'
	#loader.get_template('polls/index.html')
	context={
	'lastest_question_list':lastest_question_list,
	}
	return render(request,template,context)
	#HttpResponse(template.render(context,request))

def detail(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
	#return HttpResponse("你真再看問題%s的投票結果"%question_id)
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/results.html',{'question':question})
'''
class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='lastest_question_list'
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'
class ResultsView(generic.DetailView):
	model=Question
	template_name='polls/results.html'



def vote(request,question_id):
	#return HttpResponse("你正在對問題%s投票"%question_id)
	question=get_object_or_404(Question,pk=question_id) 
	#爲何在get_object_or_404函數中的question_id參數傳入int實參，會被抛出TypeError錯誤？直接使用以下get函數無錯誤
	#question=Question.objects.get(pk=question_id)
	
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,choice.DoesNotExist):
		return render(request,'polls/detali.html',{'question':question,'error_message':"Your didn't select a choice"},)
	else:
		#selected_choice.votes+=1
		selected_choice.votes=F('votes')+1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,))
		)


