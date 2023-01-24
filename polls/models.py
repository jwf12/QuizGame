from django.db import models

class Category(models.Model):
    category_text = models.CharField(max_length=200)

    def __str__(self):
        return self.category_text

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null= True, related_name='questions') 
    question_text= models.CharField(max_length=200)
    pub_date= models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=200)
    votes = models.IntegerField(default= 0)

    def __str__(self):
        return self.choice_text

class Answer2(models.Model):
   choice= models.ForeignKey(Question, on_delete=models.CASCADE)
   answer_text= models.CharField(max_length=200)

   def __str__(self):
    return self.answer_text
    