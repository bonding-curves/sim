import pytest

from mutual_credit.sim import PAMM, SAMM, Agent, Sim


# Define the mutual credit simulation fixture
@pytest.fixture(scope="module")
def sim_fixture():
    sim: Sim = Sim(name="Mutual Credit V0.1.0")
    return sim


@pytest.fixture(scope="module")
def alice_fixture():
    alice: Agent = Agent(dollars=25, credit=100, name="Alice")
    return alice


@pytest.fixture(scope="module")
def bob_fixture():
    bob: Agent = Agent(dollars=100, credit=25, name="Bob")
    return bob


@pytest.fixture(scope="module")
def PAMM_fixture():
    bonding_curve: PAMM = PAMM()
    return bonding_curve


@pytest.fixture(scope="module")
def SAMM_fixture():
    dex: SAMM = SAMM()
    return dex


def test_mutual_credit_sim(sim_fixture):
    sim: Sim = sim_fixture
    print(sim)
    sim.step()
    distribution: list = sim.distribution()
    assert type(distribution) == list
    agents: list = sim.agents
    assert type(agents) == list


def test_agent(alice_fixture):
    alice: Agent = alice_fixture
    print(alice)


def test_transfer(alice_fixture, bob_fixture):
    alice: Agent = alice_fixture
    print(alice)
    bob: Agent = bob_fixture
    print(bob)
    print("Alice transferring 25 credits to Bob")
    print(alice.transfer(25, bob))
    print(alice)
    print(bob)


def test_credit_limit(alice_fixture, bob_fixture):
    alice: Agent = alice_fixture
    print(alice)
    bob: Agent = bob_fixture
    print(bob)
    print("Alice transferring 200 credits to Bob")
    print(alice.transfer(200, bob))
    print(alice)
    print(bob)


def test_PAMM(PAMM_fixture, alice_fixture):
    bonding_curve: PAMM = PAMM_fixture
    alice: Agent = alice_fixture
    bonding_curve_credits_initial = bonding_curve.credits
    print(bonding_curve)
    print(alice)

    print("Alice mints 25 credits")
    bonding_curve.mint_credits(25, alice)
    print(bonding_curve)
    print(alice)
    assert bonding_curve.credits == bonding_curve_credits_initial + 25

    print("Alice burns 25 credits")
    bonding_curve.burn_credits(25, alice)
    print(bonding_curve)
    print(alice)
    assert bonding_curve.credits == bonding_curve_credits_initial


def test_SAMM(SAMM_fixture, bob_fixture):
    dex: SAMM = SAMM_fixture
    bob: Agent = bob_fixture
    dex_credits_initial = dex.credits
    print(dex)
    print(bob)

    print("Bob buys 25 credits")
    dex.buy_credits(25, bob)
    print(dex)
    print(bob)
    assert dex.credits == dex_credits_initial + 25

    print("Bob sells 25 credits")
    dex.sell_credits(25, bob)
    print(dex)
    print(bob)
    assert dex.credits == dex_credits_initial
