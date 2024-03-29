from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
	question_text=models.CharField("问题描述",max_length=200)
	pub_date = models.DateTimeField('发布时间')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		#return self.pub_date>=timezone.now()-datetime.timedelta(days=1)
		now=timezone.now()
		return now-datetime.timedelta(days=1)<=self.pub_date<=now
	was_published_recently.admin_order_field='pub_date'
	was_published_recently.boolean=True
	was_published_recently.short_description='最近发布了吗？'

class Choice(models.Model):
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField("选项描述",max_length=200)
	votes=models.IntegerField("票数",default=0)
	def __str__(self):
		return self.choice_text

