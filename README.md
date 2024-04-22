# Girl-Hackathon-2024
# NOC Optimization Using Reinforcement Learning

This repository contains code for optimizing the Network-on-Chip (NOC) design using Reinforcement Learning.

## Environment Setup:

1. Make sure you have Python installed on your system.
2. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```
3. Clone the repository:
   ```
   git clone https://github.com/username/NOC-RL-Optimization.git
   cd NOC-RL-Optimization
   ```

## Running the Code:

1. Navigate to the `src` directory:
   ```
   cd src
   ```
2. Run the main script to start the optimization process:
   ```
   python main.py
   ```
3. Follow the prompts to input parameters and configurations as needed.

## Additional Information:

- The `config.py` file contains configuration settings for the simulator and RL agent.
- The `simulator.py` file provides the interface to interact with the simulator.
- The `rl_agent.py` file contains the RL agent implementation.
- Results and logs are stored in the `logs` directory.

## Pseudocode to Measure Average Latency and Bandwidth:

```
initialize latency_sum = 0
initialize bandwidth_count = 0
initialize total_transactions = 0

for each line in interface_trace:
    if line[1] == "Rd" or line[1] == "Wr":
        total_transactions += 1
        if line[1] == "Rd":
            start_time = line[0]
        else:
            latency = line[0] - start_time
            latency_sum += latency
        bandwidth_count += 32  # Assuming fixed data width of 32B per transfer

average_latency = latency_sum / total_transactions
average_bandwidth = bandwidth_count / total_timestamp
```

This pseudocode efficiently calculates the average latency and bandwidth based on the provided interface trace.

---

## RL Framework:

For the second part, using Reinforcement Learning (RL) to optimize the NOC parameters, we can outline the RL framework as follows:

States/Behaviors: The states could represent different configurations of the NOC, such as buffer sizes, arbiter weights, and throttling status. Behaviors refer to the actions taken by the system, like adjusting buffer sizes, changing arbiter weights, or enabling/disabling throttling.

Actions: The actions represent the possible changes we can make to the NOC parameters. This could include increasing or decreasing buffer sizes, adjusting arbiter weights, or toggling throttling on/off.

Rewards: The rewards indicate how well the current configuration performs in terms of meeting the optimization criteria. For example, a reward could be based on how close the measured latency is to the minimum latency requirement, how close the measured bandwidth is to 95% of the maximum bandwidth, how close the buffer occupancy is to 90%, and how rarely throttling occurs.

RL Algorithm: Given the complexity of the problem and the continuous nature of the parameter space, a model-free RL algorithm like Deep Q-Networks (DQN) or Actor-Critic could be suitable. These algorithms can handle high-dimensional state and action spaces and learn to optimize the parameters over time.
