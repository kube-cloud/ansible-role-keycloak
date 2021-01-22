# Ansible Linux based Docker role

![Python](https://img.shields.io/pypi/pyversions/testinfra.svg?style=flat)
![Licence](https://img.shields.io/github/license/kube-cloud/ansible-role-keycloak.svg?style=flat)
[![Travis Build](https://img.shields.io/travis/kube-cloud/ansible-role-keycloak.svg?style=flat)](https://travis-ci.com/kube-cloud/ansible-role-keycloak)
[![Galaxy Role Downloads](https://img.shields.io/ansible/role/d/42855.svg?style=flat)](https://galaxy.ansible.com/jetune/keycloak)

Ansible role used to install RedHat Keycloak IDP on Linux based Operating System.

<a href="https://www.kube-cloud.com/"><img width="300" src="https://kube-cloud.com/images/branding/logo/kubecloud-logo-single_writing_horizontal_color_300x112px.png" /></a>
<a href="https://www.redhat.com/fr/technologies/management/ansible"><img width="200" src="https://getvectorlogo.com/wp-content/uploads/2019/01/red-hat-ansible-vector-logo.png" /></a>
<a href="https://www.keycloak.org/documentation"><img width="250" src="https://design.jboss.org/keycloak/logo/images/keycloak_logo_600px.png" /></a>

# Supported Version

| Component | Version |
| ------ | ------ |
| Keycloak Version  | 8.0.0, + |

# Supported OS

| OS Distribution | OS Version |
| ------ | ------ |
| CentOS | 7, + |
| Ubuntu | Xenial, Bionic, + |

# Role variables

| Variable | Description | Default value |
| ------ | ------ | ------ |
| install_community | Flag that specify whether install Community version or Not. If false, Enterprise version wil be installed | true |
| docker_version | Docker version to install. | lastest |
| docker_gpg_key | Docker Repository GPG Key URL (for Ubuntu). | https://download.docker.com/linux/ubuntu/gpg |
| docker_gpg_key_fingerpring | Docker Repository GPG Key Fingerprint (for Ubuntu). | 9DC858229FC7DD38854AE2D88D81803C0EBFCD88 |
| docker_repository_baseurl | Docker Repository Base URL (for Ubuntu). | https://download.docker.com/linux/ubuntu |
| docker_repository_file | Docker Repository File URL (for CentOS). | https://download.docker.com/linux/centos/docker-ce.repo |
| docker_packages | Docker Package to install. | [docker-ce, docker-ce-cli, containerd.io] |
| install_compose | Flag that specify whether install Docker Compose or Not. | true |
| compose_version | Docker Compose version to install  (required if install_compose is true)| - |

See next section for all variables

# Usage

* Install Role ``` ansible-galaxy install jetune.docker ```
* Use in your playbook : case of install from repository
```
---
- name: Converge
  hosts: all
  vars_files:
   - "test-vars-ce-{{ ansible_distribution }}-{{ ansible_distribution_major_version }}.yml"

  roles:
   - role: jetune.docker
      
```
* Sample playbook vars file for Ubuntu Bionic
```
---

# Docker version
docker_version: "5:19.03.1~3-0~ubuntu-bionic"

# Install docker community
docker_install_community: true

# System architecture
docker_os_architecture: "{{ ansible_architecture | replace('amd64', 'x86_64') }}"

# Docker authorized users
docker_authorized_users:
 - jetune
 - hmefoo
 - ltchatch

# Install compose
docker_install_compose: true

# Docker compose version
docker_compose_version: "1.24.1"

# Docker compose URL
docker_compose_url: "{{ 'https://github.com/docker/compose/releases/download/'\
+ docker_compose_version + '/docker-compose-' + ansible_system + '-' + docker_os_architecture }}"

# Docker compose checksum
docker_compose_checksum: "sha256:cfb3439956216b1248308141f7193776fcf4b9c9b49cbbe2fb07885678e2bb8a"

# Docker datas
docker_data_dir: "/kis/docker/datas"

# Docker security directory
docker_security_dir: "{{ docker_data_dir }}/security"

# Docker scripts directory
docker_scripts_dir: "{{ docker_data_dir }}/scripts"

# Docker scripts assets to upload (in the scripts directory)
docker_scripts_assets_dir: "scripts"

# Docker security assets to upload (in the security directory)
docker_security_assets_dir: "security"

# Docker Host adrdesses
docker_hosts:
 - "0.0.0.0:2373"
 - "0.0.0.0:2374"
 - "0.0.0.0:2375"
 - "0.0.0.0:2376"

# Extras Options
docker_extras_options:
 - "--log-level debug"
 - "--label TEST=true"
 - "--icc"
 - "--registry-mirror https://images.lab.kube-cloud.be"

# Docker role post script (for some initialization like plugin install & configuration)
# This file will be find in the scripts dir "{{ docker_scripts_dir }}"
docker_post_install_script: "post-install.sh"

# Docker post script parameters
docker_post_install_script_parameters:
 - "param1"
 - "param2"
 - "param3"
 - "param4"

```
