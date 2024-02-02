import numpy as np
import param as pm


class Agent(pm.Parameterized):
    credit = pm.Number(default=0, bounds=(-100, None))

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


s = Sim()
s.step()
