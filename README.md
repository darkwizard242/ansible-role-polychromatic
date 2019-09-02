Ansible Role: polychromatic
=========

Role to install (_by default_) `polychromatic` package  or uninstall (_if  passed as var_)  on **Ubuntu** systems. [Polychromatic](https://github.com/polychromatic/polychromatic) is a frontend for customizing the functionality of Razer peripherials under GNU/Linux.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below (located in  `defaults/main.yml`):

```yaml
polychromatic_repo: 'ppa:polychromatic/stable'
polychromatic_repo_desired_state: present
polychromatic_repo_filename: polychromatic
polychromatic_app: polychromatic-meta
polychromatic_package_desired_state: present
```

Variable `polychromatic_repo`: Refers to the ppa repo to add.

Variable `polychromatic_repo_desired_state`: Defined to dynamically chose whether to add/keep (i.e. `present`) or remove (i.e. `absent`) the repository file list from `/etc/apt/sources.list.d`.

Variable `polychromatic_repo_filename`: Defined to set th repository file name for saving in `/etc/apt/sources.list.d`

Variable `polychromatic_app`: Defines the app to install i.e. **polychromatic-meta**

Variable `polychromatic_package_desired_state`: Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package.

Dependencies
------------

None

Example Playbook
----------------

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
         
License
-------

[MIT](https://github.com/darkwizard242/ansible-role-polychromatic/blob/master/LICENSE)

Author Information
------------------

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
