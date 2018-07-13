import pytest


@pytest.mark.bashcomp(
    cmd="munin-node-configure",
)
class TestMuninNodeConfigure(object):

    @pytest.mark.complete("munin-node-configure --libdir ")
    def test_1(self, completion):
        assert completion.list
