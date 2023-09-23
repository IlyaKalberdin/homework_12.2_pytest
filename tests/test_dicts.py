import pytest
from utils import dicts


@pytest.fixture
def coll():
    return {"vcs": "mercurial"}


def test_get_val(coll):
    assert dicts.get_val(coll, "vcs") == "mercurial"
    assert dicts.get_val(coll, "mps", "Python") == "Python"
    assert dicts.get_val(coll, "mps") == "git"
    assert dicts.get_val(coll, 5) == "git"
    assert dicts.get_val(coll, [5, 6, 1]) == "git"
    assert dicts.get_val(coll, {"vcs": "mercurial"}) == "git"
