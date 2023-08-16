from django.shortcuts import render
from django.http import HttpResponse
from app.findEntity import findEntity
from app.generateUmlCode import generate_usecase_diagram
from app.renderDiagram import generate_uml_diagram
from app.requirement_predictor import predict_requirement
import nltk
nltk.download('punkt') 
from nltk.tokenize import sent_tokenize
from app.sentenceSimplifier import reformat

# Create your views here.

def home(request):

    if request.method =='POST':
        sentences= request.POST['textArea1']
        sentences_tokenized=sent_tokenize(sentences)
        actors=[]
        usecases=[]
        for inptext in sentences_tokenized:

            if predict_requirement(inptext) in [True,False]:# change to true

                inptext=reformat(inptext)[2:] #using davinchi

                actor, usecase= findEntity(inptext)
                if(actor[0] and usecase[0]):
                    actors.append(actor)
                    usecases.append(usecase)



        if actors==[]:

            return HttpResponse('<h1>ERROR</h1>')

        
        puml=generate_usecase_diagram(actors,usecases)
        generate_uml_diagram(puml)
        #response_text = f'<h1>{actors}{usecases}</h1>'
        #return HttpResponse(response_text)
        return render(request, 'output.html', {})
            



            # else:
            #     return HttpResponse(f'<h1>not req</h1>')


    else:
        return render(request, 'home.html', {})
    
def diag(request):
    
    image_file_path='app/templates/puml.png'

    with open(image_file_path, 'rb') as image_file:
        image_data = image_file.read()
    return HttpResponse(image_data, content_type="image/png")
