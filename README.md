<div align="center">
    <h1>Ansible Playbooks</h1>

</div>

## Contents

1. [Details](#details)
1. [Deploy](#deploy)

## Details - UBUNTU OS

- **main.yml**: Run this to install docker and kali
- **cronschedule.yml**: This will schedule the update playbook to run in cron
- **twingateupdate.yml**: just that but in docker
- **update.yml**: Updates docker, and os packages, includes a reboot

## Deploy
```bash
ansible-playbook main.yml -l {destination} -u {user}
```
