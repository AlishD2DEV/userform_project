from django.shortcuts import render, redirect
from .forms import UserSubmissionForm
from .models import UserSubmission

def submit_form(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('submitted_users')
    else:
        form = UserSubmissionForm()
    return render(request, 'submit_form.html', {'form': form})

def submitted_users(request):
    users = UserSubmission.objects.all().order_by('full_name')
    return render(request, 'submitted_users.html', {'users': users})
