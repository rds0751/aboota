from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return render(request, 'meeting/index.html', {})

@login_required
def join(request):
	return render(request, 'meeting/meeting.html', {})