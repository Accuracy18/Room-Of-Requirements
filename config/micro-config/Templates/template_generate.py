#! /usr/bin/python3

from mako.template import Template
import argparse

parser = argparse.ArgumentParser(description='This is a script to do something.')
parser.add_argument('-f', '--file', help='The input file.', required=True)
args = parser.parse_args()

path = '/home/controller/.config/micro/plug/Templates'
template_names = {'tcp-server': f'{path}/tcp_server.py', 'udp-server': '{path}/udp_server.py', 'html': f'{path}/template.html'}

template = Template(filename=template_names.get(args.file))

# Render the template with some variables
data = {"protocolName": "SomeBulshit", "port": 4005, "service_type": "Reconnecting", "is_ssl": True}
output = template.render(**data)

# Print the rendered template
print(output)
