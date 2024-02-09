import pytest

from mutual_credit.sim import Sim


# Define the mutual credit simulation fixture
@pytest.fixture(scope="module")
def mutual_credit_sim():
    s = Sim()
    return s


def test_mutual_credit_sim(mutual_credit_sim):
    s = mutual_credit_sim
    s.step()
