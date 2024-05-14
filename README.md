[![build-test](https://github.com/darkwizard242/ansible-role-polychromatic/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-polychromatic/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-polychromatic/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-polychromatic/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/polychromatic) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-polychromatic&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-polychromatic) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-polychromatic&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-polychromatic) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-polychromatic&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-polychromatic) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-polychromatic?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-polychromatic?color=orange&style=flat-square)

# Ansible Role: polychromatic

Role to install (_by default_) polychromatic package or uninstall (_if passed as var_) on **Ubuntu** systems. [Polychromatic](https://polychromatic.app) is a frontend applicationfor customizing the functionality of Razer peripherials under GNU/Linux.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
polychromatic_repo: 'ppa:polychromatic/stable'
polychromatic_repo_desired_state: present
polychromatic_repo_filename: polychromatic
polychromatic_app: polychromatic-meta
polychromatic_package_desired_state: present
```

### Variables table:

Variable                            | Description
----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------
polychromatic_repo                  | Refers to the ppa repo to add.
polychromatic_repo_desired_state    | Defined to dynamically chose whether to add/keep (i.e. `present`) or remove (i.e. `absent`) the repository file list from `/etc/apt/sources.list.d`.
polychromatic_repo_filename         | Defined to set the repository file name for saving in `/etc/apt/sources.list.d`
polychromatic_app                   | Defines the app to install i.e. **polychromatic-meta**
polychromatic_package_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default is set to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **polychromatic** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.polychromatic
```

For customizing behavior of role (i.e. installation of latest **polychromatic** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.polychromatic
  vars:
    polychromatic_package_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **polychromatic** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.polychromatic
  vars:
    polychromatic_package_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-polychromatic/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
