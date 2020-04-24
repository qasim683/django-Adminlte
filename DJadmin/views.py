from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def userhome(request):
    return render(request, "userhome.html", {})
