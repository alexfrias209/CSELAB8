from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment
from .forms import EnrollmentForm
from django.forms import modelformset_factory

#collection of forms to be submitted together with the same form class
EnrollmentFormSet = modelformset_factory(Enrollment, form=EnrollmentForm, extra=0)

@login_required(login_url='login')
def editGrade(request, course_id):
    course = Course.objects.get(id=course_id)
    enrollments = Enrollment.objects.filter(course=course)
    if request.method == 'POST':
        formset = EnrollmentFormSet(request.POST, queryset=enrollments)
        if formset.is_valid():
            formset.save()
            return redirect('home')
        else:
            print(formset.errors)
    else:
        formset = EnrollmentFormSet(queryset=enrollments)
    context = {'enrollments': enrollments, 'formset': formset, 'course': course}
    return render(request, 'base/editing.html', context)

def loginPage(request):
    page = 'login'
    form = UserCreationForm()
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect')
    context = {'page':page, 'form':form}
    return render(request, 'base/login.html',context)

@login_required(login_url='login')
def home(request):
    user = request.user
    if hasattr(user, 'student'):
        # get all courses in the database
        courses = Course.objects.all()
        # get all courses that the student is enrolled in
        student = user.student
        enrolled_courses = student.courses.all()
        context = {'enrolled_courses': enrolled_courses, 'all_courses': courses}
        return render(request,'base/home.html', context)
    elif hasattr(user, 'teacher'):
        # get all courses that the teacher teaches
        teacher = user.teacher
        courses = teacher.courses.all()
        context = {'teacher': teacher, 'courses': courses}
        return render(request,'base/home.html', context)
    else:
        return render(request,'base/home.html',{})


@login_required(login_url='login')
def addcourse(request, course_id):
    course = Course.objects.get(id=course_id)
    student = request.user.student
    course.students.add(student)
    Enrollment.objects.create(student=student, course=course)
    messages.success(request, f"You have successfully enrolled in {course.course}")
    return redirect('home')


@login_required(login_url='login')
def removecourse(request, course_id):
    course = Course.objects.get(id=course_id)
    student = request.user.student
    course.students.remove(student)
    enrollment = Enrollment.objects.get(student=student, course=course)
    enrollment.delete()
    messages.success(request, f"You have successfully unenrolled from {course.course}")
    return redirect('home')


    
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')



    