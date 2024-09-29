<div align="center">
    <h1>Ansible Playbooks</h1>

</div>

## Details - 

- **cronschedule.yml**: Sets update schedule
- **macbackground.yml**: Sets a background image on a mac from a local location (change the file name)
- **macupdate.yml**: Runs macupdate
- **main.yml**: Run this to install docker and kali
- **Twingateupdate.yml**: Updates twingate docker images
- **update.yml**: Linux update script
- **win_disk.yml**: Provides disk information for windows
- **winpeas.yml**: Like linpeas but windows hehe
- **winupdate.yml**: Runs windows update remotely

## Deploy
```bash
ansible-playbook {playbook} -l {destination}
```
