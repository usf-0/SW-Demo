from jinja2 import Template
import os

# Load the template file
with open('template.txt', 'r') as f:
    template = Template(f.read())

# Define variables
iso_code = input('please enter ISO code: ')
hotel_code = input('please enter hotel code: ')
sw_number = input('please enter switch number: ')
os.system('cmd /c "cls"')
ip_address = input('please enter ip address of the Switch: ')
default_ip = input('please enter default Gateway: ')

# Replace placeholder values in the template with the desired values
config = template.render(
    iso_code=iso_code, 
    hotel_code=hotel_code, 
    sw_number=sw_number, 
    vlan_name='Admin', 
    vlan_id='42',
    ip_address=ip_address,
    default_ip= default_ip
    )

# Write the generated configuration to a new file
file_name = iso_code+('-')+hotel_code+('-SW-')+sw_number+('.txt')

with open(file_name, 'w') as f:
    f.write(config)
