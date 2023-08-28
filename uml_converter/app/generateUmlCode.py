def replace_characters(input_string):
    
    replacements = {'.': '', '-': '_', ' ': '',',':'_','/':'_or_'}
    
    for original, replacement in replacements.items():
        input_string = input_string.replace(original, replacement)
    
    return input_string

def generate_usecase_diagram(actors_, usecases_):
    puml_code = "@startuml\n"
    puml_code += "left to right direction\n"

    actors=[]
    usecases=[]

    act = set()
    use = set()

    for actor in actors_:
        a=[replace_characters(str(actor))]
        act.update(a)
        actors.append(a)

    for usecase in usecases_:
        u=[replace_characters(str(usecase))]
        use.update(u)
        usecases.append(u)
    

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