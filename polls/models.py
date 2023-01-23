from django.db import models

class Category(models.Model):
    category_text = models.CharField(max_length=200)

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null= True) 
    question_text= models.CharField(max_length=200)
    pub_date= models.DateTimeField(auto_now= True)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=200)
    votes = models.IntegerField(default= 0)

class Answer2(models.Model):
   choice= models.ForeignKey(Question, on_delete=models.CASCADE)
   answer_text= models.CharField(max_length=200)
    