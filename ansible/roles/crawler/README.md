# Ansible crawler role

> `crawler` is an [Ansible](http://www.ansible.com) role which:
>
> * Install pip and pip packages
> * Run crawler script
> * Generate ssl certificate
> * Deploy nginx configuration

:warning: This playbook assume that openssl is already installed since it is installed by default on most of the distros

## How to use

```bash
ansible-playbook main.yml
```

When the playbook using the role have finished, you can access to the content downloaded on your web browser at: https://localhost

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