<div align="center">
    <h1>Ansible Playbooks</h1>

</div>

## Contents

1. [Details](#details)
1. [Deploy](#deploy)

## Details - UBUNUTU OS

- **main.yml**: Run this to install docker and kali
- **Docker.yml**: Docker installer with Brew
- **kaliDockerBuild.yml**: Kali image with mapped drive and rdp via xrdp. This will take 20 minutes to run and update all packages. 
- **update.yml**: Updates docker, and os packages, includes a reboot

## Deploy
```bash
ansible-playbook main.yml -l {destination} -u {user}
```
