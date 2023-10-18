import subprocess

# function for rendering puml script to UML daiagram
def generate_uml_diagram(puml):
    tempuml='app/templates/puml.txt'
    try:
        with open(tempuml, 'w') as file:
            file.write(puml)
        print(f"File '{tempuml}' saved successfully.")
   
    except Exception as e:
        print(f"Error: {e}")

    
    try:
       
        result = subprocess.run('cd app/templates & python -m plantuml puml.txt', shell=True, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error while running the command: {e}")
        return e.returncode    
