from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def djf_validate(request):
    FO=NameForm()
    d={'FO':FO}
    if request.method=='POST':
        FD=NameForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))



    return render(request,'djf_validate.html',d) 
