# Website crawler

The goal was to write a script to download the html content of a given website with varying dependency

## Description

The exercise was split in 3 parts:
* Write the script to download the html content
* Write the nginx.conf to serve the previously downloaded content
* Write an ansible role to automate the run of the script and the installation of the nginx.conf

## How to use

```bash
    cd ansible
    ansible-playbook main.yml # for more info see ansible/README.md
```

You can directly use the script running:

```bash
    python3 script/crawler.py [valid_url] [depth]
```

## License
Copyright (c) We Are Interactive under the MIT license.