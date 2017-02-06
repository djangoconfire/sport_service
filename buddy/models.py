from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Assignment(models.Model):
    status = models.IntegerField(default = 1)
    buddy  = models.ForeignKey(User, related_name="buddy")



class BuddyDetail(models.Model):
	buddy_id		=models.IntegerField(unique=True)
	batch_id		=models.IntegerField(unique=True)
	batch_name		=models.CharField(max_length=200)
	batch_day		=models.CharField(max_length=100)
	batch_time		=models.TimeField(blank=True,null=True,help_text="Time format is :HH:MM:SS")
	assignements	=models.ManyToManyField(Assignment,blank=True,null=True) 
	

	def __unicode__(self):
		return self.buddy_id



class Task(models.Model):
    title 			= models.CharField(max_length=50, default="")
    description 	= models.CharField(max_length=500)
    # A Task can have many assignements
    assignments 	= models.ManyToManyField(Assignment, related_name="assignments")
    manager 		= models.ForeignKey(User, related_name="owner")
    created_time 	= models.DateTimeField(editable=False, auto_now= True)
    modified_time 	= models.DateTimeField(null=True, blank=True)

    # This method is for updating created and modified times on Saving an object
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Task, self).save(*args, **kwargs)

