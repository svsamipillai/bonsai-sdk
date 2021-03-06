import sys
import logging
from bonsai_ai import Brain, Config
from bonsai_gym import GymSimulator

log = logging.getLogger('gym_simulator')
log.setLevel(logging.DEBUG)


class Acrobot(GymSimulator):
    # Environment name, from openai-gym
    environment_name = 'Acrobot-v1'

    # simulator name from Inkling
    simulator_name = 'acrobot_simulator'

    # convert openai gym observation to our state schema
    def gym_to_state(self, observation):
        state = {"cos_theta0": observation[0],
                 "sin_theta0": observation[1],
                 "cos_theta1": observation[2],
                 "sin_theta1": observation[3],
                 "theta0_dot": observation[4],
                 "theta1_dot": observation[5]}
        return state

    # convert our action schema into openai gym action
    def action_to_gym(self, action):
        return action['command']


if __name__ == '__main__':
    # create a brain, openai-gym environment, and simulator
    config = Config(sys.argv)
    print(config)

    brain = Brain(config)
    sim = Acrobot(brain, iteration_limit=500)
    sim.run_gym()
