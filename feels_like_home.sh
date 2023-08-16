
<%def name="general()">
sudo apt update
sudo apt install gcc-avr curl ranger  avr-libc avrdude tmux tmuxinator wireguard resolvconf python3-pip micro nmap ncat iproute2 npm -y

npm install cncjs
pip3 install octoprint kivy twisted shell_gpt bpytop pyqt mako

#### 	Creality Fix for Octoprint
pip3 install "https://github.com/RomainOdeval/OctoPrint-CrealityTemperature/releases/latest/download/master.zip"
pip3 install "https://github.com/SimplyPrint/OctoPrint-Creality2xTemperatureReportingFix/archive/master.zip"
</%def>

<%def name="install_docker(x)">
### 		Configure Docker
sudo apt install docker.io -y

sudo addgroup docker
sudo usermod -aG docker $USER
newgrp docker

DOCKER_CONFIG=${x}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose</%def>

### 	Environments
<%def name="environment(api_key, ps)">

echo 'export EDITOR=micro' >> $HOME/.bashrc
echo 'export PS1=$(cat $HOME/Room-Of-Requirements/ps1-design/${ps}.txt)' >> $HOME/.bashrc
echo 'export OPENAI_API_KEY=${api_key}' >> $HOME/.bashrc

tmux config tmux.conf
</%def>
