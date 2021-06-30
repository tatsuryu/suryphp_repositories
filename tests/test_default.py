"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_php_sourcelist_exists(host):
    f = host.file("/etc/apt/sources.list.d/php.list")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
