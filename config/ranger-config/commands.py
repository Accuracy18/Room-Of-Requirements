from ranger.api.commands import Command
import subprocess, curses

class ZipCert(Command):
    def execute(self):
    
        for item in self.fm.thistab.get_selection():
            try:
                subprocess.run(f'zip unnamed.zip {item}'.split(), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                self.fm.notify(e)

class MakeCert(Command):
    def execute(self):
        name = user_input("Name: ")
        cmd = f"sh /home/ubuntu/.config/ranger/make_tak_cert.sh {name}"
        subprocess.run(cmd.split(), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def user_input(prompt):

    window = curses.initscr()
    rows, cols = [coord - 1 for coord in window.getmaxyx()]
    window.addstr(rows, 0, prompt)
    curses.echo()
    user_input_bytes = window.getstr(rows, len(prompt), cols)
    curses.noecho()
    window.addstr(rows, 0, " " * cols)
    curses.endwin()
    return user_input_bytes.decode(encoding="utf-8")
