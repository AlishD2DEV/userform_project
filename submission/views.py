from django.shortcuts import render, redirect
from .forms import SubmissionForm

def submit_form(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('form_submitted')
    else:
        form = SubmissionForm()
    return render(request, 'submission/submit_form.html', {'form': form})

def form_submitted(request):
    return render(request, 'submission/form_submitted.html')
