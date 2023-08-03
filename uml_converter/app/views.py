from django.shortcuts import render
from django.http import HttpResponse
from app.findEntity import findEntity
from app.generateUmlCode import generate_usecase_diagram
from app.renderDiagram import generate_uml_diagram


# Create your views here.

def home(request):

    if request.method =='POST':
        inptext= request.POST['textArea1']
        actor, usecase= findEntity(inptext)
        puml=generate_usecase_diagram(actor,usecase)
        generate_uml_diagram(puml)




        #response_text = f'<h1>{puml}</h1>'
        #return HttpResponse(response_text)
        return render(request, 'output.html', {})

    else:
        return render(request, 'home.html', {})
    
def diag(request):
    
    image_file_path='app/templates/puml.png'

    with open(image_file_path, 'rb') as image_file:
        image_data = image_file.read()
    return HttpResponse(image_data, content_type="image/png")
