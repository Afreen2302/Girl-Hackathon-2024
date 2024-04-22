class Config:
    def __init__(self):
        # Simulator settings
        self.read_latency = 10  # Read latency in cycles
        self.write_latency = 5  # Write latency in cycles
        self.data_width = 32  # Data width in bytes
        self.max_buffer_size = 100  # Maximum buffer size
        self.max_arbiter_weight = 10  # Maximum arbiter weight
        self.power_threshold = 1000  # Power threshold
        self.throttle_percentage = 5  # Throttling percentage

        # RL agent settings
        self.state_dim = 10  # State dimension
        self.action_dim = 5  # Action dimension
        self.learning_rate = 0.001  # Learning rate
        self.gamma = 0.99  # Discount factor
        self.epsilon = 0.1  # Exploration rate
