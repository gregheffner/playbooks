
# Ansible Playbooks Collection

Welcome! This repository contains a set of ready-to-use Ansible playbooks for automating common tasks across macOS, Linux, and Windows systems.

---

## Quick Start

To run a playbook:

```bash
ansible-playbook <playbook.yml> -l <destination>
```

Replace `<playbook.yml>` with the playbook you want to run, and `<destination>` with your target host or group.

---

## Playbook Overview

Below is a summary of the available playbooks and what they do:

| Playbook                | Platform      | Purpose / Main Actions                                      |
|-------------------------|--------------|-------------------------------------------------------------|
| cronschedule.yml        | Linux/macOS   | Set up or update cron jobs for scheduled updates             |
| macbackground.yml       | macOS         | Change desktop background image                              |
| macupdate.yml           | macOS         | Update Homebrew and all installed packages                   |
| main.yml                | Linux         | Install Docker and set up Kali Linux container               |
| twingateupdate.yml      | Linux         | Update and restart Twingate Docker containers                |
| update.yml              | Linux/macOS   | System updates, Docker restarts, logging, and reboot         |
| wifijoin.yml            | Linux/macOS   | Configure Wi-Fi credentials and connect to network           |
| win_disk.yml            | Windows       | Get disk usage and partition info via PowerShell             |
| winpeas.yml             | Windows       | Run WinPEAS for privilege escalation auditing                |
| winupdate.yml           | Windows       | Run Windows Update and install available updates             |
| docker_cleanup.yml      | Linux         | Remove unused Docker images, containers, and volumes         |
| network_scan.yml        | Linux         | Scan local network for active devices (nmap)                 |
| service_restart.yml     | Linux         | Check and restart specified services                         |
| cloudflaredupdate.yml   | Linux         | Install/update Cloudflare Tunnel and restart service         |
| piholeupdate.yml        | Linux         | Update Pi-hole to latest version                             |

---


## More Playbooks & Tasks

You’ll also find additional playbooks and task files in the `tasks/` folder, including:

- Docker management
- Cloudflare Tunnel updates
- Pi-hole updates
- Fail2Ban configuration
- Kali Linux Docker builds
- Service restarts and more

Check the folder structure for more examples and reusable roles.

---

## Contributing & Notes

- Playbooks are written for clarity and easy customization.
- Most playbooks are self-contained, but some may require variables (see `group_vars/`).
- For questions or improvements, feel free to open an issue or PR.

---

## License

See repository for license details.

---

Happy automating!

## How to Deploy

Run the following command to execute a playbook:

```bash
ansible-playbook {playbook} -l {destination}
```

Replace `{playbook}` with the name of the playbook and `{destination}` with the target host or group.

---

Let me know if you need further refinements or additional details!
