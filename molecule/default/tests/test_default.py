import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'polychromatic'
PACKAGE_BINARY = '/usr/bin/polychromatic-controller'


def test_polychromatic_package_installed(host):
    """
    Tests if polychromatic is installed.
    """
    assert host.package("polychromatic").is_installed


def test_polychromatic_binary_exists(host):
    """
    Tests if polychromatic-controller binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_polychromatic_binary_file(host):
    """
    Tests if polychromatic-controller binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_polychromatic_binary_which(host):
    """
    Tests the output to confirm polychromatic-controller's binary location.
    """
    assert host.check_output('which polychromatic-controller') == \
        PACKAGE_BINARY
