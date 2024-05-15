<div align="center">
    <h1>Ansible Playbooks</h1>

</div>

## Contents

1. [Details](#details)
1. [Deploy](#deploy)

## Details

- **main.yml**: Run this to install docker and kali
- **Docker.yml**: centOS Docker installer with Brew
- **kaliDockerBuild.yml**: Kali image with mapped drive and rdp via xrdp
- **update.yml**: Updates docker, brew, and os packages. Schedules next run for the 16th of each month at 1am. 
- **upgrade.yml**: upgrade instead of update

## Deploy
```bash
ansible-playbook main.yml -l {destination} -u {user}
```