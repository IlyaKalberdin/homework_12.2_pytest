from utils import dicts


def test_get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "mps", "Python") == "Python"
    assert dicts.get_val({"vcs": "mercurial"}, "mps") == "git"
    assert dicts.get_val({"vcs": "mercurial"}, 5) == "git"
    assert dicts.get_val({"vcs": "mercurial"}, [5, 6, 1]) == "git"
    assert dicts.get_val({"vcs": "mercurial"}, {"vcs": "mercurial"}) == "git"
