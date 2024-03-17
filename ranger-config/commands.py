from ranger.api.commands import Command
from kubernetes import client, config
import subprocess

class KubernetesApply(Command):
    def execute(self):
    
        for item in self.fm.thistab.get_selection():
            try:
                subprocess.run(f'kubectl apply -f {item}'.split(), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                self.fm.notify(e)

class OpenK9S(Command):
    def execute(self):
        subprocess.run(['k9s'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
