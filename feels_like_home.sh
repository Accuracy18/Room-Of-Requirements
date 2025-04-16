sudo apt update
sudo apt install gcc-avr curl ranger git python3-twisted avr-libc bpytop avrdude tmux tmuxinator resolvconf python3-pip micro nmap iproute2 npm -y

cp config/tmux.conf $HOME/.tmux.conf
tmux source $HOME/.tmux.conf

cp config/casual.sh $HOME/.casual.sh
echo 'source $HOME/.casual.sh' >> $HOME/.bashrc
source $HOME/.bashrc
echo 'export EDITOR=micro' >> $HOME/.bashrc
