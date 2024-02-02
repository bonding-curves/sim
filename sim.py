import numpy as np
import param as pm


class Agent(pm.Parameterized):
    credit = pm.Number(default=0, bounds=(-100, None))
    dollars = pm.Number(default=0, bounds=(0, None))

    def transfer(self, amount, to):
        if self.credit - amount < self.param["credit"].bounds[0]:
            return False
        else:
            self.credit -= amount
            to.credit += amount
            return True


class Sim:
    agents = [Agent() for _ in range(100)]

    def step(self):
        for agent in self.agents:
            if np.random.choice([0, 1]):
                amount = np.random.rand() * (agent.credit + 100)
                to = np.random.choice(self.agents)
                print(f"Transferring {amount} from {agent} to {to}")
                agent.transfer(
                    amount,
                    to,
                )

    def distribution(self):
        return sorted([agent.credit for agent in self.agents], reverse=True)


class SAMM(Agent):
    dollars = pm.Number(default=1, bounds=(1, None))
    credits = pm.Number(default=1, bounds=(1, None))

    def buy_credits(self, amount, agent):
        pass

    def sell_credits(self, amount, agent):
        pass


class PAMM(Agent):
    dollars = pm.Number(default=1, bounds=(1, None))
    credits = pm.Number(default=1, bounds=(1, None))

    def mint_credits(self, amount, agent):
        pass

    def burn_credits(self, amount, agent):
        pass


s = Sim()
s.step()
