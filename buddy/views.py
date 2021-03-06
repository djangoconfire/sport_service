from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.shortcuts import render
from models import Task,Assignment,BuddyDetail

# Create your views here.   
class BuddyView(View):
    def post(self, request):
        buddy_id= request.POST.get("buddy_id")
        batch_id= request.POST.get("batch_id")
        batch_name= request.POST.get("batch_name")
        batch_time= request.POST.get("batch_time")
        batch_day= request.POST.get("batch_day")
        print buddy_id,batch_day
        user= request.user
        newBuddy = BuddyDetail(buddy_id=buddy_id,batch_id=batch_id,\
                        batch_name=batch_name,batch_day=batch_day,\
                        batch_time=batch_time)
        newBuddy.save()

        return JsonResponse({"message": "Successfully Saved!"})


class TaskView(View):
    def post(self, request):
        title = request.POST.get("name")
        description = request.POST.get("description")
        buddyID = request.POST.getlist("buddies[]")
        print title, description, buddyID
        # Create a new task
        user= request.user
        newTask = Task(title=title, description=description, manager= user)
        newTask.save()
        buddies = get_user_model().objects.filter(id__in=buddyID)

        # For assigned buddies create assignments
        for buddy in buddies:
            print buddy
            print '@@@@@@@@@@@'
            assignment = Assignment(buddy=buddy)
            assignment.save()
            newTask.assignments.add(assignment)
            newTask.save()
        return JsonResponse({"message": "Successfully Saved!"}) 

class AssignmentView(View):
    def post(self, request):
        assignmentID = request.POST.get("assignmentID")
        status = request.POST.get("status")
        assignment = Assignment.objects.get(id=int(assignmentID))
        assignment.status = int(status)
        assignment.save()
        return JsonResponse({"message": "Status Successfully Updated!"})      



