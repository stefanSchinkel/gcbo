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

def test_add_repo_to_tempyt(tmpdir):
    """Test default new start"""
    # Arange
    cfg = tmpdir.mkdir("sub").join("empty.json")
    new_repo = "foo.bar/foobar"

    # Act
    rm = gcbo.RepoManager(repo="foo.bar/baz", cfg=cfg)
    rm.save("foorepo")

    # Assert
    with open(cfg) as fp:
        data = json.load(cfg)
    print(data)
    assert 1 == 1
