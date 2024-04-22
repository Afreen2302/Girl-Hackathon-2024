import os
from config import Config
from simulator import Simulator
from rl_agent import RLAgent
import numpy as np
import matplotlib.pyplot as plt

class Config:
    def __init__(self):
        self.num_episodes = 100  # Set the default number of episodes for the simulation
        self.state_dim = 10  # State dimension
        self.action_dim = 5  # Action dimension
        self.learning_rate = 0.001  # Learning rate
        self.gamma = 0.99  # Discount factor
        self.epsilon = 0.1  # Exploration rate

def main():
    # Initialize configuration
    config = Config()

    # Initialize simulator
    simulator = Simulator()

    # Initialize RL agent
    rl_agent = RLAgent(config)

    # Lists to store results
    episode_rewards = []

    # Run simulation
    for episode in range(config.num_episodes):
        # Specify buffer ID for state representation
        buffer_id = 1  # Example buffer ID
        agent_type = 'CPU'

        # Get current state
        state = simulator.get_state(buffer_id, agent_type)
        done = False
        total_reward = 0

        while not done:
            # Select action based on current state
            action = rl_agent.select_action(state)

            # Perform action and get next state, reward, and done status
            next_state, reward, done = simulator.step(action)

            # Update Q-table
            rl_agent.update_q_table(state, action, reward, next_state)

            # Update total reward
            total_reward += reward

            # Update state
            state = next_state

        # Save episode reward
        episode_rewards.append(total_reward)

        # Log episode results
        print(f"Episode {episode + 1}: Total Reward = {total_reward}")

    # Save trained model
    rl_agent.save_model()

    # Plot episode rewards
    plot_rewards(episode_rewards)

    # Create logs directory if it doesn't exist
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Write episode rewards to a log file
    with open(os.path.join(logs_dir, "episode_rewards.txt"), "w") as f:
        for i, reward in enumerate(episode_rewards):
            f.write(f"Episode {i + 1}: Total Reward = {reward}\n")

def plot_rewards(rewards):
    plt.plot(rewards)
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.title('Episode Rewards')
    plt.show()

if __name__ == "__main__":
    main()