Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/jammy64"
    config.vm.network "private_network", ip: "192.168.33.10"
    config.vm.hostname = "devops-final"
  
    # Provisión con un script de shell
    config.vm.provision "shell", inline: <<-SHELL
      # Actualiza los paquetes
      sudo apt-get update
      
      # Instala Ansible si no está instalado
      if ! command -v ansible >/dev/null 2>&1; then
        sudo apt-get install -y ansible
      fi
  
      # Ejecuta el playbook de Ansible
      cd /vagrant/ansible
      ansible-playbook -i ../hosts playbook.yml
    SHELL
  end
  