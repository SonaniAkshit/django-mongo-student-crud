# student/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        enrolment_no = request.POST.get('enrolment_no')
        department = request.POST.get('department')
        stream = request.POST.get('stream')

        Student.objects.create(
            name=name,
            enrolment_no=enrolment_no,
            department=department,
            stream=stream
        )
        return redirect('student_list')
    return render(request, 'student/student_create.html')

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.enrolment_no = request.POST.get('enrolment_no')
        student.department = request.POST.get('department')
        student.stream = request.POST.get('stream')
        student.save()
        return redirect('student_list')
    return render(request, 'student/student_update.html', {'student': student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student/student_confirm_delete.html', {'student': student})
