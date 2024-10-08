import gym
env = gym.make("CartPole-v1",render_mode = "human")
def Start_Music():
    for episodes in range(5):
        env.reset()
        for steps in range(500):
            env.render()
            action = env.action_space.sample()
            next_state,reward, terminate, _, info = env.step(action)
            print(steps, next_state,reward, terminate, _, info, action)
            if terminate:
                break
Start_Music()
env.close()