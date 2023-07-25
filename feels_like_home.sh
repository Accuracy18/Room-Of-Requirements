sudo apt update
sudo apt install gcc-avr curl  avr-libc avrdude tmux tmuxinator wireguard resolvconf python3-pip micro nmap ncat iproute2 npm -y
pip3 install pyqt mako

<%def name="install_wireguard_client(action, conf_file)">

sudo chown -R $USER:root /etc/wireguard
mv $HOME/${conf_file}.conf /etc/wireguard

	####     Configure wireguard client

	% if action == "install":
sudo systemctl enable wg-quick@${conf_file}.service
sudo systemctl daemon-reload
sudo systemctl start wg-quick@${conf_file}

	% elif action == "remove":
sudo systemctl stop wg-quick@${conf_file}
sudo systemctl disable wg-quick@${conf_file}.service
sudo rm -i /etc/systemd/system/wg-quick@${conf_file}*
sudo systemctl daemon-reload
sudo systemctl reset-failed

	% else:
		<%
print("fashi")
		%>

	%endif

	% if conf_file == "linux_home":
npm install cncjs
pip3 install octoprint

#### 	Creality Fix for Octoprint
pip3 install "https://github.com/RomainOdeval/OctoPrint-CrealityTemperature/releases/latest/download/master.zip"
pip3 install "https://github.com/SimplyPrint/OctoPrint-Creality2xTemperatureReportingFix/archive/master.zip"
	%endif
	
</%def>

<%def name="install_docker(x)">
### 		Configure Docker
sudo apt install docker.io -y

sudo addgroup docker
sudo usermod -aG docker $USER
newgrp docker

DOCKER_CONFIG=${x}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
</%def>

### 	Environments
<%def name="environment(ps, api_key)">

echo 'export EDITOR=micro' >> $HOME/.bashrc
echo 'export PS1=$(cat $HOME/room_of_requirements/ps-design/.${ps}.txt)' >> $HOME/.bashrc
echo 'export OPENAI_API_KEY=${api_key}' >> $HOME/.bashrc

pip3 install octoprint kivy twisted shell_gpt bpytop

tmux config tmux.conf
</%def>