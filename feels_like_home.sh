sudo apt update
sudo apt install gcc-avr curl ranger git python3-twisted avr-libc bpytop avrdude tmux tmuxinator resolvconf python3-pip micro nmap iproute2 npm -y

# Install Brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo "export PATH=$PATH:/home/linuxbrew/.linuxbrew/bin" >> $HOME/.bashrc

# curl -fsSL https://ollama.com/install.sh | sh

cp config/tmux.conf $HOME/.tmux.conf
tmux source $HOME/.tmux.conf

cp config/casual.sh $HOME/.casual.sh
echo 'source $HOME/.casual.sh' >> $HOME/.bashrc

source $HOME/.bashrc
echo 'export EDITOR=micro' >> $HOME/.bashrc

# Install Docker
sudo snap install docker
sudo addgroup docker
sudo usermod -aG docker $USER
newgrp docker
sudo snap disable docker
sudo snap enable docker

# Prepare Git clones
git config --global user.email "tadesco18@gmail.com"
git config --global user.name "Accuracy18"
git clone git@github.com:Accuracy18/Services.git

# All TUIs
brew install ducker bpytop
