import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


POLYCHROMATIC_BINARY = '/usr/bin/polychromatic-controller'
POLYCHROMATIC_PACKAGE = 'polychromatic'
WHICH = 'which polychromatic-controller'


def test_polychromatic_package_installed(host):
    host.package("POLYCHROMATIC_PACKAGE").is_installed


def test_polychromatic_binary_exists(host):
    host.file('POLYCHROMATIC_BINARY_PATH').exists


def test_polychromatic_binary_file(host):
    host.file('POLYCHROMATIC_BINARY_PATH').is_file


def test_polychromatic_binary_which(host):
    host.check_output('which polychromatic-controller') == POLYCHROMATIC_BINARY
