import sys

import gym
import gym_marioai
from gym_marioai import levels

from agents import qlearning_agent
from logger import Logger


if __name__ == '__main__':

    result_name = 'easyLevel_5x5'

    if len(sys.argv) == 2:
        result_name = sys.argv[1]
    elif len(sys.argv) == 3:
        result_name = sys.argv[1]
        level_name = sys.argv[2]

    logger = Logger(result_name, load_existing=True)

    # possible levels are: flatLevel.lvl, easyLevel.lvl, hardLevel.lvl or None for seed-based selection
    env = gym.make('Marioai-v0', render=True,
                   level_path=levels.easy_level,
                   rf_width=7, rf_height=5)

    agent = qlearning_agent.Agent(env, epsilon_start=0)
    agent.Q = logger.load_model()

    # run the demonstration
    while True:
        done = False
        state = env.reset().tobytes()
        steps = 0
        total_reward = 0

        while not done:
            env.render()
            action = agent.select_action(state)
            state, reward, done, info = env.step(action)
            state = state.tobytes()
            total_reward += reward
            steps += 1

        print(f'reward: {total_reward}, steps: {steps}, success: {info["win"]}')






