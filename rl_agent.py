# rl_agent.py

import numpy as np

class RLAgent:
    def __init__(self, config):
        self.config = config
        self.q_table = np.zeros((config.state_dim, config.action_dim))  # Initialize Q-table

    def select_action(self, state):
    # Ensure state is properly formatted
        if isinstance(state, list):
        # If state is a list, extract the first element
            state = state[0]

    # Convert state to an integer
        try:
            state = int(state)
        except TypeError:
            pass  # If state cannot be converted to an integer, leave it unchanged

        # Return the selected action
        action = np.argmax(self.q_table[state])
        return action

        
        # Explore or exploit based on epsilon-greedy strategy
        if np.random.rand() < self.config.epsilon:
            # Explore: choose a random action
            action = np.random.randint(self.config.action_dim)
        else:
            # Exploit: choose the action with the highest Q-value for the given state
            action = np.argmax(self.q_table[state])  # Fix the indexing here
        return action

    def update_q_table(self, state, action, reward, next_state):
        # Convert state to an integer if it's a list
        if isinstance(state, list):
            state = state[0]

        # Convert next_state to an integer if it's a list
        if isinstance(next_state, list):
            next_state = next_state[0]

        # Update Q-table
        old_q_value = self.q_table[state, action]
        next_max = np.max(self.q_table[next_state])
        new_q_value = (1 - self.learning_rate) * old_q_value + self.learning_rate * (reward + self.gamma * next_max)
        self.q_table[state, action] = new_q_value


    def save_model(self):
        # Placeholder for saving the trained model
        pass
