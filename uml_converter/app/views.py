from django.shortcuts import render
from django.http import HttpResponse
from app.findEntity import findEntity
from app.generateUmlCode import generate_usecase_diagram
from app.renderDiagram import generate_uml_diagram
from app.requirement_predictor import predict_requirement
import nltk
nltk.download('punkt') 
from nltk.tokenize import sent_tokenize, word_tokenize
from app.sentenceSimplifier import reformat
from app.flanUsecaseEntityDetector import getUsecaseEntity
from app.models import Entity
from django.http import JsonResponse
import os
from django.conf import settings
import json
from nltk.stem import PorterStemmer

# Define the home view function
def home(request):

    # Check if the request method is POST
    if request.method =='POST':
        # Get the action and requirement text from the request
        action = request.POST.get('action')
        requirement = request.POST['textArea1']

        # If the action is 'make', process the requirement (creating UML diagram based on requirement)
        if action == 'make': 
            selected_option = request.POST.get('selection', None)
            if selected_option == 'knn': # Entity Detector 1 pipeline
                # Tokenize the requirement text into sentences
                sentences_tokenized = sent_tokenize(requirement)
                actors = []
                usecases = []
                text = []  # to store sentences for semi-automatic function

                # Iterate through the sentences to process and extract entities
                for inptext in sentences_tokenized:
                    # Check if the requirement is predicted to be valid and contains space
                    if predict_requirement(inptext) in [True] and ' ' in inptext:
                        text.append(inptext)
                        # Use reformat function to preprocess the sentence
                        inptext = reformat(inptext)[2:]
                        print(inptext)
                        # Extract actor and usecase entities from the sentence
                        actor, usecase = findEntity(inptext)
                        print(actor)
                        ps = PorterStemmer()
                        # If both actor and usecase are extracted, add them to respective lists
                        if actor and usecase:
                            actors.append(actor)
                            usecases.append(usecase)
                        else:
                            text.pop()

                # If no actors are extracted, return an error response
                if not actors:
                    return HttpResponse('<h1>ERROR</h1>')

                # Generate a PlantUML diagram and save it
                puml = generate_usecase_diagram(actors, usecases, text)
                generate_uml_diagram(puml)
                # Retrieve all entities from the database
                entity = Entity.objects.all()
                # Render the output template with the entities and input requirement text
                return render(request, 'output.html', {'items': entity, 'input_txt': requirement})

            elif selected_option == 'use_case_llm': # Entity Detector 2 pipeline
                # Tokenize the requirement text into sentences
                sentences = sent_tokenize(requirement)
                actors = []
                usecases = []
                text = []

                # Iterate through the sentences to process and extract entities
                for inptext in sentences:
                    # Check if the requirement is predicted to be valid and contains space
                    if predict_requirement(inptext) in [True] and ' ' in inptext:
                        text.append(inptext)
                        # Extract actor and usecase entities using the getUsecaseEntity function
                        actor, usecase = getUsecaseEntity(inptext)
                        # If both actor and usecase are extracted, add them to respective lists
                        if actor[0] and usecase[0]:
                            actors.append(actor)
                            usecases.append(usecase)
                        else:
                            text.pop()

                # If no actors are extracted, return an error response
                if not actors:
                    return HttpResponse('<h1>ERROR</h1>')

                # Generate a PlantUML diagram and save it
                puml = generate_usecase_diagram(actors, usecases, text)
                generate_uml_diagram(puml)
                # Retrieve all entities from the database
                entity = Entity.objects.all()
                # Render the output template with the entities and input requirement text
                return render(request, 'output.html', {'items': entity, 'input_txt': requirement})

        # If the action is 'correct', update entities with user-provided corrections
        elif action == 'correct': 
            actors = []
            usecases = []
            texts = []
            for entity in Entity.objects.all():
                # Get actor, usecase, and sentence data from the user's input
                actor = request.POST.get(f'actor_{entity.id}')
                usecase = request.POST.get(f'usecase_{entity.id}')
                sentence = request.POST.get(f'sentence_{entity.id}')
                actors.append(actor)
                usecases.append(usecase)
                texts.append(sentence)
                print(actor)
                print(sentence)

            # Generate a PlantUML diagram with corrected entities and text
            puml = generate_usecase_diagram(actors, usecases, texts)
            generate_uml_diagram(puml)
            # Retrieve all entities from the database
            entity = Entity.objects.all()
            # Render the output template with the entities and input requirement text
            return render(request, 'output.html', {'items': entity, 'input_txt': requirement})

        # If the action is 'download', provide the PlantUML diagram for download
        elif action == 'download':
            file_path = os.path.join(settings.TEMPLATES_, 'puml.png')
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="image/png")
                    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                    return response

    # If the request method is not POST or no specific action is specified, render the home template
    else:
        return render(request, 'home.html', {})

# Define a view to serve the PlantUML diagram image
def diag(request):
    image_file_path = os.path.join(settings.TEMPLATES_, 'puml.png')

    with open(image_file_path, 'rb') as image_file:
        image_data = image_file.read()
    return HttpResponse(image_data, content_type="image/png")

# Define a view to delete an entity item
def delete_item(request, item_id):
    try:
        item = Entity.objects.get(pk=item_id)
        item.delete()
        return JsonResponse({'success': True})
    except Entity.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'})

# Define a function to check if the request is an AJAX request
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Define a view to add a new entity item
def add_item(request):
    if request.method == 'POST' and is_ajax(request):
        try:
            json_data = json.loads(request.body)
            new_actor = json_data.get('new_actor')
            new_usecase = json_data.get('new_usecase')
            new_sentence = json_data.get('new_sentence')
            
            # Create a new Entity instance and save it to the database
            new_item = Entity(actor=new_actor, usecase=new_usecase, sentence=new_sentence)
            new_item.save()

            # Retrieve all entities from the database
            entity = Entity.objects.all()
            entity_list = list(entity.values())
            print(entity_list)

            return JsonResponse({'success': True, 'items': entity_list})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})
