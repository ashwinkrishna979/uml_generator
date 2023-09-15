from app.models import Entity


def replace_characters(input_string):
    
    replacements = {'.': '', '-': '_', ' ': '',',':'_','/':'_or_','*':'_',':':'_'}
    
    for original, replacement in replacements.items():
        input_string = input_string.replace(original, replacement)
    
    return input_string

def generate_usecase_diagram(actors_, usecases_,text_=None):
    Entity.objects.all().delete() #clear database


    puml_code = "@startuml\n"
    puml_code += "left to right direction\n"

    actors=[]
    usecases=[]

    act = set()
    use = set()

    # for actor in actors_:
    #     a=[replace_characters(str(actor))]
    #     act.update(a)
    #     actors.append(a)

    # for usecase in usecases_:
    #     u=[replace_characters(str(usecase))]
    #     use.update(u)
    #     usecases.append(u)


    if text_ !=None:

        for actor,usecase,text in zip(actors_,usecases_,text_):
            a=[replace_characters(str(actor))]
            u=[replace_characters(str(usecase))]
            act.update(a)
            use.update(u)
            actors.append(a)
            usecases.append(u)
            new_entity = Entity(actor=''.join(a),usecase=''.join(u),sentence=text)
            new_entity.save()

    else:
        for actor,usecase in zip(actors_,usecases_):
            a=[replace_characters(str(actor))]
            u=[replace_characters(str(usecase))]
            act.update(a)
            use.update(u)
            actors.append(a)
            usecases.append(u)
            new_entity = Entity(actor=''.join(a),usecase=''.join(u),sentence='sentence tracing is not possible for this model')
            new_entity.save()




    act2index = {word: index for index, word in enumerate(act)}
    use2index = {word: index for index, word in enumerate(use)}

    for actor in act:
        puml_code += f"actor {''.join(actor)} as f{act2index.get(actor)}\n"
    
    puml_code += 'rectangle {\n'

    for usecase in use:
        puml_code += f"usecase {''.join(usecase)} as u{use2index.get(usecase)}\n"

    puml_code += '}\n'

    for actor, usecase in zip(actors, usecases):
        for a in actor:
            for u in usecase:
                puml_code += f"f{act2index.get(a)} --> u{use2index.get(u)}\n"

    puml_code += "@enduml"
    return puml_code