from django.db import models
from django.utils import timezone

class Repeate_type(models.Model):
    Repeate_type = models.TextField()

    def __str__(self):
        return '<Reeate Type: {}>'.format(self.Repeate_type)

class Task(models.Model):
    task_title = models.TextField()
    task_description = models.TextField()
    due_date = models.DateTimeField()
    repeate_type_id = models.ForeignKey(Repeate_type, on_delete=models.CASCADE)
    complete = models.BooleanField()

    def __str__(self):
        return '<Task: {}, Task Description: {}, Due Date: {}, Repeate Type: {}, Is Completed: {}>'.format(self.task_title , self.task_description, self.due_date, self.repeate_type_id.Repeate_type, self.complete)


class User(models.Model):
    user_name = models.TextField()
    user_email = models.EmailField()
    user_password = models.TextField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return '<UserName: {}, Email:{}, Password: {}, Task: {}>'.format(self.user_name, self.user_email, self.user_password, self.task_id.task_description)

class Task_item(models.Model):
    task_id = models.ForeignKey(Task,on_delete=models.CASCADE)
    item = models.TextField()
    in_order = models.BooleanField()
    complete = models.BooleanField()
    
    def __str__(self):
        return '<ID: {}, Item: {}, Is Ordered: {}, Completed: {}>'.format(self.id, self.item, self.in_order, self.complete)


