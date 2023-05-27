from django.shortcuts import render,redirect
from .forms import CourseForm
from .models import Course,Lecture
from django.contrib.auth.decorators import user_passes_test
import subprocess
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

@user_passes_test(lambda u: u.is_authenticated and u.is_teacher,login_url='404')
def course_create_view(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.instance.save()
            form.instance.user.add(request.user)
            course_id = form.instance.id
            print("Created course ID:", course_id)
            return redirect('instructor-dashboard')
    else:
        form=CourseForm()
    return render(request, 'course/courseForm.html', {'form':form})


class CourseDetailView(DetailView):
    model=Course

class LectureDetailView(DetailView):
    model=Lecture



def start_model(request):
    command = ['python', 'C:/My Files/Projects/automation-face-attendance/model/face_detect.py']
    subprocess.run(command)

    return render(request,'course/modlePage.html')