from utils.dicts import get_val
import pytest


@pytest.fixture
def data_fixture():
    return {"vcs1": "mercurial", "vcs2": "git", "vcs3": "bazaar"}


@pytest.fixture
def data_none_fixture():
    return {}


def test_get_val(data_fixture, data_none_fixture):
    assert get_val(data_fixture, "vcs1") == 'mercurial'
    assert get_val(data_none_fixture, "vcs", "git") == 'git'
    assert get_val(data_fixture, "vcs3", "mercurial") == 'bazaar'
    assert get_val(data_none_fixture, "vcs2", "bazaar") == 'bazaar'
    assert get_val(data_none_fixture, "vcs1") == 'git'
