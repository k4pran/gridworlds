from src.environment import Env
from src.grid import Grid
from src.agent import RandomAgent

EPISODES = 100




if __name__ == "__main__":
    grid = Grid.generate(5, 5)
    env = Env(grid)
    agent = RandomAgent(env.get_action_space())

    for episode in range(EPISODES):

        done = False
        state = env.get_state()
        while not done:
            action = agent.act(state)
            next_state, reward, done, info = env.step(action)

            agent.log_results(state, action, reward, done, info)

            state = next_state
