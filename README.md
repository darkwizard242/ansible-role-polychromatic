[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-polychromatic.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-polychromatic) ![Ansible Role](https://img.shields.io/ansible/role/43079?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43079?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43079?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-polychromatic&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-polychromatic) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-polychromatic?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-polychromatic?color=orange&style=flat-square)

# Ansible Role: polychromatic

Role to install (_by default_) `polychromatic` package or uninstall (_if passed as var_) on **Ubuntu** systems. [Polychromatic](https://github.com/polychromatic/polychromatic) is a frontend for customizing the functionality of Razer peripherials under GNU/Linux.

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

Variable                            | Value (default)            | Description
----------------------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------
polychromatic_repo                  | 'ppa:polychromatic/stable' | Refers to the ppa repo to add.
polychromatic_repo_desired_state    | present                    | Defined to dynamically chose whether to add/keep (i.e. `present`) or remove (i.e. `absent`) the repository file list from `/etc/apt/sources.list.d`.
polychromatic_repo_filename         | polychromatic              | Defined to set the repository file name for saving in `/etc/apt/sources.list.d`
polychromatic_app                   | polychromatic-meta         | Defines the app to install i.e. **polychromatic-meta**
polychromatic_package_desired_state | present                    | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default is set to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **polychromatic** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.polychromatic
```

For customizing behavior of role (i.e. installation of latest **polychromatic** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.polychromatic
      vars:
        polychromatic_package_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **polychromatic** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.polychromatic
      vars:
        polychromatic_package_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-polychromatic/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
