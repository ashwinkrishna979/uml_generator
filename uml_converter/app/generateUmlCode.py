def generate_usecase_diagram(actor,usecase):
    puml_code = "@startuml\n"

    i=0
    for act, use in zip(actor,usecase):
        puml_code += f"actor {act} as f{i}\n"
        puml_code += f"usecase {use} as u{i}\n"
        i+=1

    i=0
    for act, use in zip(actor,usecase):
    
        puml_code += f"f{i} --> u{i}\n"
        i+=1
        

    puml_code += "@enduml"
    print(puml_code)

    return puml_code