from django.shortcuts import render

from django.contrib.auth.decorators  import login_required
from .form import ContactModelForm
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactModelForm()

    return render(request, 'contact/contact.html', {'form': form})