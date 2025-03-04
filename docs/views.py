from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def app_docs(request):
    return render(request, 'document/index.html')