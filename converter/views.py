from django.shortcuts import render
from django.http import HttpResponse
from converter.functions import handle_uploaded_file #function.py
from converter.forms import StudentForm #forms.py

# Create your views here.
def index(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            model_instance = student.save(commit=False)
            model_instance.save()
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render (request, "index.html",{'form':student})
