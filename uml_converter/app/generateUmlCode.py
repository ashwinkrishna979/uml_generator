def generate_usecase_diagram(actors, usecases):
    puml_code = "@startuml\n"



    act = set()
    use = set()

    for actor in actors:
        #actor.replace(" ", "")
        act.update(actor)

    for usecase in usecases:
       # usecase.replace(" ", "")
        use.update(usecase)

    act2index = {word: index for index, word in enumerate(act)}
    use2index = {word: index for index, word in enumerate(use)}

    for actor in act:
        puml_code += f"actor {actor} as f{act2index.get(actor)}\n"

    for usecase in use:
        puml_code += f"usecase {usecase} as u{use2index.get(usecase)}\n"

    for actor, usecase in zip(actors, usecases):
        for a in actor:
            for u in usecase:
                puml_code += f"f{act2index.get(a)} --> u{use2index.get(u)}\n"

    puml_code += "@enduml"
    return puml_code