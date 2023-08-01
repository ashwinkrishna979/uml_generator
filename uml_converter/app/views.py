from django.shortcuts import render
from django.http import HttpResponse
from app.findEntity import findEntity

# Create your views here.

def home(request):

    if request.method =='POST':
        inptext= request.POST['textArea1']
        output= findEntity(inptext)
        response_text = f'<h1>{output}</h1>'





        return HttpResponse(response_text)

    

    else:
        return render(request, 'home.html', {})
