# Fail2Ban Jail Status Playbook

![Fail2Ban Overview](fail2ban-summary.png)

This Ansible playbook summarizes the status of Fail2Ban jails and banned IPs for each `nginx-web-*` pod in a Kubernetes namespace.

## Features

- Lists all pods starting with `nginx-web-` in the specified namespace.
- Parses Fail2Ban logs for each pod to count:
    - Number of jails created
    - Number of unique banned IPs
- Outputs a centered, formatted table summarizing the results.

## Usage

1. Place this playbook in your Ansible tasks directory.
2. Ensure you have access to the Kubernetes cluster and the necessary permissions.
3. Run the playbook:

     ```sh
     ansible-playbook -i <inventory> <playbook-file>.yml
     ```

4. The summary table will be printed in the output.

## Variables

- `namespace`: Kubernetes namespace to search pods in (default: `default`)
- `log_path`: Path to the Fail2Ban log file (default: `/var/log/fail2ban.log`)

## Requirements

- Ansible
- Access to Kubernetes cluster (`kubectl` configured)
- Fail2Ban running in the target pods


## Image

![Fail2Ban Jail Status Summary](fail2ban-summary.png)

The included `fail2ban-summary.png` provides a visual overview of the process.
