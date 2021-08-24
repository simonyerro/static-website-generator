# Ansible crawler role

> `crawler` is an [Ansible](http://www.ansible.com) role which:
>
> * Install pip and pip packages
> * Run crawler script
> * Generate ssl certificate
> * Deploy nginx configuration

:warning: This playbook assumed that openssl is installed already since it is installed by default in most of the distros

## How to use

```bash
ansible-playbook main.yml
```

## Variables

Here is a list of all the default variables for this role, which are also available in `defaults/main.yml`.

```yaml
---
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