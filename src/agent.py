import random


class RandomAgent:

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, state):
        return random.choice(self.action_space)

    def log_results(self, state, action, reward, done, info):
        print("Made action {} in state {} and received reward {} Terminal state - {}".format(action, state, reward, done))
