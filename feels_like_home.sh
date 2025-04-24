sudo apt update
sudo apt install gcc-avr curl ranger git python3-twisted avr-libc bpytop avrdude tmux tmuxinator resolvconf python3-pip micro nmap iproute2 npm -y

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
mv kubectl ~/.local/bin

curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind ~/.local/bin

curl -fsSL https://ollama.com/install.sh | sh

cp config/tmux.conf $HOME/.tmux.conf
tmux source $HOME/.tmux.conf

cp config/casual.sh $HOME/.casual.sh
echo 'source $HOME/.casual.sh' >> $HOME/.bashrc
source $HOME/.bashrc
echo 'export EDITOR=micro' >> $HOME/.bashrc
# source ai/bin/activate
