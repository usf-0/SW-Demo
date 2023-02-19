from jinja2 import Template
import os

def import_template(template_string):
    # Create the template object from the string
    with open(template_string, 'r') as f:
        template = Template(f.read())
    return template

r = input("you're switch is a cisco or HP?\n")
os.system('cmd /c "cls"')
if r == "cisco" or r == "CISCO" or r == "Cisco":
    model = int(input ('''ciscowhat it the model of youe Switch: 
       1: CBS 250
       2: CBS 350
       3: catalys 9200 L
       4: other  
    '''))
    os.system('cmd /c "cls"')
    if model == 1:
        template = import_template("template\cisco\CSB350.txt")
        # Replace placeholder values in the template with the desired values
        config = template.render(hotel_code="h0000")

        with open("output\config.txt", 'w') as f:
            f.write(config)