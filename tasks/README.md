# Scripts in the Folder

This folder contains three scripts that perform different tasks. Below, you will find a brief description of each script along with instructions on how to use them.

## Script 1: `Docker.yml`

Description: This script installs Docker and needed packages

## Script 2: `k8reboot.yml`

Description: This script rebookts Kubernetes clusters without outage. Draining nodes before bounce. 


## Script 3: `kaliDockerBuild.yml`

Description: This script will run Kali with all packages installed on a docker image. Mounts local drive, enables RDP and sets up RDP. Generates default root:password for RDP session. 
PLEASE CHANGE PASSWORD ASAP



Here is the kaliDockerBuild script but run as aliases. 

```bash
alias BuildKali='ansible-playbook ~/playbooks/tasks/kaliDockerBuild.yml'
alias KillKali='docker stop kali_container && docker remove kali_container'
alias KaliCLI='docker exec -it kali_container /bin/bash'
```
<img width="1553" alt="IMG_3090" src="https://github.com/gregheffner/playbooks/assets/28818131/1d5c648e-cc27-4f38-8f2a-13520bb05883">
