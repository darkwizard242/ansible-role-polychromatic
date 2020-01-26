import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_polychromatic_package_installed(host):
    assert host.package("polychromatic").is_installed


def test_polychromatic_binary_exists(host):
    assert host.file('/usr/bin/polychromatic-controller').exists


def test_polychromatic_binary_file(host):
    assert host.file('/usr/bin/polychromatic-controller').is_file


def test_polychromatic_binary_which(host):
    assert host.check_output('which polychromatic-controller') == \
      '/usr/bin/polychromatic-controller'
