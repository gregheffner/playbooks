<div align="center">
    <h1>Ansible Playbooks</h1>
</div>

## Playbook Details

### 1. **`cronschedule.yml`**
- **Purpose**: Configures a cron job to set an update schedule.
- **Key Tasks**:
  - Creates or updates a cron job to automate system updates.

### 2. **`macbackground.yml`**
- **Purpose**: Sets a background image on macOS.
- **Key Tasks**:
  - Copies a specified image file to the system.
  - Updates macOS settings to apply the new background.

### 3. **`macupdate.yml`**
- **Purpose**: Updates macOS packages and applications.
- **Key Tasks**:
  - Runs `brew update` to update Homebrew.
  - Upgrades all installed Homebrew packages.

### 4. **`main.yml`**
- **Purpose**: Installs Docker and Kali Linux.
- **Key Tasks**:
  - Installs Docker on the target system.
  - Sets up Kali Linux as a Docker container.

### 5. **`Twingateupdate.yml`**
- **Purpose**: Updates Twingate Docker images.
- **Key Tasks**:
  - Pulls the latest Twingate Docker images.
  - Restarts the Twingate containers.

### 6. **`update.yml`**
- **Purpose**: Updates Linux systems, restarts Docker containers, and logs update details.
- **Key Tasks**:
  - Updates all APT packages (Debian-based systems).
  - Performs a distribution upgrade.
  - Restarts all running Docker containers.
  - Updates Homebrew and upgrades packages (if on macOS).
  - Logs update details to a file.
  - Reboots the system.

### 7. **`wifijoin.yml`**
- **Purpose**: Configures a system to join a specified Wi-Fi network.
- **Key Tasks**:
  - Sets up Wi-Fi credentials.
  - Ensures the system connects to the specified network.

### 8. **`win_disk.yml`**
- **Purpose**: Retrieves disk information for Windows systems.
- **Key Tasks**:
  - Runs PowerShell commands to gather disk usage and partition details.

### 9. **`winpeas.yml`**
- **Purpose**: A Windows equivalent of LinPEAS for privilege escalation auditing.
- **Key Tasks**:
  - Executes a script to gather system information for security auditing.

### 10. **`winupdate.yml`**
- **Purpose**: Runs Windows updates remotely.
- **Key Tasks**:
  - Initiates Windows Update.
  - Installs available updates.

### 11. **`docker_cleanup.yml`**
- **Purpose**: Cleans up unused Docker resources.
- **Key Tasks**:
  - Removes unused Docker images, containers, and volumes.
  - Frees up disk space on the system.

### 12. **`network_scan.yml`**
- **Purpose**: Performs a network scan to identify active devices.
- **Key Tasks**:
  - Uses tools like `nmap` to scan the local network.
  - Generates a report of active devices and their IP addresses.

### 13. **`service_restart.yml`**
- **Purpose**: Restarts specified services on the target system.
- **Key Tasks**:
  - Checks the status of specified services.
  - Restarts services if they are not running.

### 14. **`cloudflaredupdate.yml`**
- **Purpose**: Installs and updates Cloudflare Tunnel on Ubuntu systems.
- **Key Tasks**:
  - Downloads the latest Cloudflare Tunnel package.
  - Installs the package using APT.
  - Restarts the `cloudflared` service using `systemctl`.

### 15. **`piholeupdate.yml`**
- **Purpose**: Updates Pi-hole to the latest version.
- **Key Tasks**:
  - Runs the `pihole -up` command to update Pi-hole.
  - Displays the result of the update process.

---

## How to Deploy

Run the following command to execute a playbook:

```bash
ansible-playbook {playbook} -l {destination}
```

Replace `{playbook}` with the name of the playbook and `{destination}` with the target host or group.

---

Let me know if you need further refinements or additional details!
