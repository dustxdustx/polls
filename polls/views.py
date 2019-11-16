from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from  django.template import loader
# Create your views here.
def index(request):
	lastest_question_list=Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template('polls/index.html')
	context={
	'lastest_question_list':lastest_question_list,
	}
	return HttpResponse(template.render(context,request))

def detail(request,question_id):
	return HttpResponse("你正在看問題及選項 %s" %question_id)
def results(request,question_id):
	return HttpResponse("你真再看問題%s的投票結果"%question_id)
def vote(request,question_id):
	return HttpResponse("你正在對問題%s投票"%question_id)


