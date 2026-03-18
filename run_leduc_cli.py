import rlcard
from rlcard.agents import RandomAgent
from rlcard.agents.human_agents.leduc_holdem_human_agent import HumanAgent

env = rlcard.make('leduc-holdem')

human_agent = HumanAgent(num_actions=env.num_actions)
ai_agent = RandomAgent(num_actions=env.num_actions)

env.set_agents([human_agent, ai_agent])

trajectories, payoffs = env.run(is_training=False)

print("Game finished.")
print("Payoffs:", payoffs)