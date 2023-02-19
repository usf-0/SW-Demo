from jinja2 import Environment, Template

def import_template(template_string):
    # Create the template object from the string
    with open(template_string, 'r') as f:
        template = Template(f.read())
    return template


temp = import_template("template.txt")

config = temp.render(hotel_code="H0000")

with open("config", 'w') as f:
    f.write(config)
