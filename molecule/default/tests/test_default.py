import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_installed(host):

    # Docker expected version major
    expected_major = '19'

    # Docker expected version minor
    expected_minor = '03'

    # Expected Docker command path
    docker_command_path = '/usr/bin/docker'

    # Check that docker command exists
    assert host.file(docker_command_path).exists

    # Execute docker command and get result
    docker_command_run = host.run(docker_command_path + ' --version')

    # Assert that run is OK
    assert docker_command_run.rc == 0

    # Get the running docker major version
    major_version = docker_command_run.stdout\
                                      .split('\n')[0]\
                                      .split(' ')[2]\
                                      .split('.')[0]

    # Get the running docker minor version
    minor_version = docker_command_run.stdout\
                                      .split('\n')[0]\
                                      .split(' ')[2]\
                                      .split('.')[1]

    # Assert on the excepected major version
    assert expected_major == major_version

    # Assert on the excepected minor version
    assert expected_minor == minor_version

    # Get docker service handler
    service = host.service('docker')

    # Check that service is enabled
    service.is_enabled is True

    # Check that service is started
    assert service.is_running is True


def test_compose_installed(host):

    # Compose expected version major
    expected_major = '1'

    # Compose expected version minor
    expected_minor = '24'

    # Installed Compose command path
    installed_path = '/usr/local/bin/docker-compose'

    # Expected Docker Compose command path
    linked_path = '/usr/bin/docker-compose'

    # Check that Compose installed command exists
    assert host.file(installed_path).exists

    # Check that Compose command is file
    assert host.file(installed_path).is_file

    # Check that Compose command exists
    assert host.file(linked_path).exists

    # Check that Compose command is symlink
    assert host.file(linked_path).is_symlink

    # Check that Compose symlink target
    assert host.file(linked_path).linked_to == installed_path

    # Assert on command file mode
    assert oct(host.file(installed_path).mode) == '0o755'

    # Execute Compose command and get result
    compose_command_run = host.run(linked_path + ' --version')

    # Assert that run is OK
    assert compose_command_run.rc == 0

    # Get the running docker major version
    major_version = compose_command_run.stdout\
                                       .split('\n')[0]\
                                       .split(' ')[2]\
                                       .split('.')[0]

    # Get the running docker minor version
    minor_version = compose_command_run.stdout\
                                       .split('\n')[0]\
                                       .split(' ')[2]\
                                       .split('.')[1]

    # Assert on the excepected major version
    assert expected_major == major_version

    # Assert on the excepected minor version
    assert expected_minor == minor_version
