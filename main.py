
import os
os.system("sudo apt update")
os.system("sudo apt install python3-pip")
os.system("pip3 install mako prompt_toolkit")

from mako.template import Template

from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import input_dialog, radiolist_dialog

template = Template(filename="feels_like_home.sh")
    
def install_docker():
    os.system( template.get_def("install_docker").render("DOCKER_CONFIG:-$HOME/.docker") )

def environment():
    ps_design = radiolist_dialog(
        title="PS Design",
        text="Choose something",
        values=[
            ("claro", "claro"),
            ("casual", "casual")
        ]
    )

    api_key = input_dialog(
        title='Open AI Key',
        text='Please type your api key:')

    os.system( template.get_def("environment").render(api_key.run(), ps_design.run()) )

def main_gate():
    main = radiolist_dialog(
        title="Mainz",
        text="...",
        values=[
            ("general", "General Setup"),
            ("docker", "Install Docker"),
            ("environment", "Environmental Setup"),
            ("quit", "Quit")
        ]
    )

    return main.run()

match main_gate():
    case 'general':
        os.system( template.get_def("general").render() )
        
    case 'docker':
        install_docker()
        
    case 'environment':
        environment()
