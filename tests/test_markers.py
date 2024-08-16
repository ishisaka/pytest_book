import pytest


@pytest.mark.odd
@pytest.mark.all
def test_one():
    pass


@pytest.mark.all
def test_two():
    pass


@pytest.mark.odd
@pytest.mark.all
def test_three():
    pass


@pytest.mark.testclass
@pytest.mark.all
class TestClass:
    @pytest.mark.all
    def test_four(self):
        pass

    @pytest.mark.all
    @pytest.mark.odd
    def test_five(self):
        pass


@pytest.mark.parametrize("x", [6, 7])
@pytest.mark.all
def test_param(x):
    pass
