import pytest


@pytest.mark.bashcomp(
    cmd="gnome-mplayer",
)
class TestGnomeMplayer(object):

    @pytest.mark.complete("gnome-mplayer ")
    def test_1(self, completion):
        assert completion.list
