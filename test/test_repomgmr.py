"""Test for repo manager"""

import os
import json
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader

spec = spec_from_loader("gcbo", SourceFileLoader("gcbo", 'gcbo'))
gcbo = module_from_spec(spec)
spec.loader.exec_module(gcbo)

def test_tc():
    """Boilerplate test to verify toolchain"""
    assert 1 == 1


def test_with_no_cfg(tmp_path):
    """Test default new start"""
    # Arange
    cfg = os.path.join(tmp_path, "gcbo.json")

    # Act
    rm = gcbo.RepoManager(cfg=cfg)

    # Assert
    assert rm.has_cfg is False

def test_default_select():
    """Test select to return cli arg if passed"""
    # Arange
    REPO = "https://foo.bar/foobar"

    # Act
    rm = gcbo.RepoManager(REPO)

    # Assert
    assert rm.select() == REPO


def test_add_repo_to_empty(tmpdir):
    """Test adding repo to empty cfg"""
    # Arange
    cfg = tmpdir.mkdir("sub").join("empty.json")
    REPO = "foo.bar/foobar"
    NAME = "foorepo"
    # Act
    rm = gcbo.RepoManager(repo=REPO, cfg=cfg)
    rm.save(NAME)

    # Assert
    with open(cfg) as fp:
        data = json.load(cfg)
    assert data[NAME]["url"] == REPO
