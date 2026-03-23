import rlcard
from rlcard.agents import CFRAgent
from rlcard.agents.human_agents.leduc_holdem_human_agent import HumanAgent

env = rlcard.make('leduc-holdem')

print("Number of actions:", env.num_actions)

human_agent = HumanAgent(num_actions=env.num_actions)
ai_agent = CFRAgent(env)
ai_agent.load()

env.set_agents([human_agent, ai_agent])

while True:
    trajectories, payoffs = env.run(is_training=False)
    print("Game finished.")
    print("Payoffs:", payoffs)
