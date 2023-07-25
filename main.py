from mako.template import Template

from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import input_dialog, radiolist_dialog

import os

template = Template(filename="feels_like_home.sh")

def install_wireguard_client(action):
    wireguard_client = radiolist_dialog(
        title="WireGuard",
        text="Choose something",
        values=[
            ("linux_home", "Linux Home"),
            ("raspi_guy", "Raspberry Pi")
        ]
    )

    os.system( template.get_def("install_wireguard_client").render(action, wireguard_client) )
    
def install_docker():
    os.system( template.get_def("install_docker").render("DOCKER_CONFIG:$HOME/.docker") )

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

    os.system( template.get_def("environment").render(api_key, ps_design) )

def main_gate():
    main = radiolist_dialog(
        title="Mainz",
        text="...",
        values=[
            ("docker", "Install Docker"),
            ("wireguard-install", "Set Wireguard Client"),
            ("wireguard-uninstall", "Remove Wireguard Client"),
            ("api-key", "Set OpenAI API Key"),
            ("quit", "Quit")
        ]
    )

    if main == 'docker':
        install_docker()
        
    elif main == 'wireguard-install':
        install_wireguard_client("install")

    elif main == 'wireguard-uninstall':
        install_wireguard_client("uninstall")

    elif main == 'api-key':
        environment()

    else:
        print('done')

main_gate()

# match main:
    # case 'docker':
        # install_docker()
# 
    # case 'wireguard':
        # install_wireguard_client()
        # 