<div align="center">
    <h1>Ansible Playbooks</h1>

</div>

## Contents

1. [Details](#details)
1. [Deploy](#deploy)

## Details

- **main.yml**: main playbook with nested plpaybooks in it
- **Docker.yml**: centOS Docker installer
- **kaliDockerBuild.yml**: build new kali docker image with updates and mapped drives for scripts

## Deploy
```bash
ansible-playbook main.yml -l {destination} -u {user}
```