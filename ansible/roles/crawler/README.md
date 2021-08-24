# Ansible crawler role

> `crawler` is an [Ansible](http://www.ansible.com) role which:
>
> * Install pip and pip packages
> * Run crawler script
> * Generate ssl certificate
> * Deploy nginx configuration

## How to use

```bash
ansible-playbook main.yml
```

## Variables

Here is a list of all the default variables for this role, which are also available in `defaults/main.yml`.

```yaml
---
# The pip package to use (here for python3)
pip_package: python3-pip
pip_executable: "{{ 'pip3' if pip_package.startswith('python3') else 'pip' }}"
# The packages to install
pip_install_packages: [bs4, requests]
# The url to use
crawl_script_url: www.orchestra.eu
# The depth to go on the links on the given website
crawl_script_depth: 2
```

## Usage

This is an example playbook:

```yaml
---
- hosts: localhost
  roles:
    - role: 'roles/crawler'
      become: yes
```

## License
Copyright (c) We Are Interactive under the MIT license.