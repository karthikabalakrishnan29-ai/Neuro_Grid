import random

class RLAgent:
    def __init__(self, state_size=4, action_size=3):
        self.state_size = state_size
        self.action_size = action_size # 0: Idle, 1: Charge, 2: Discharge
        self.epsilon = 0.1 # Exploration rate

    def get_action(self, state):
        """Epsilon-greedy policy for decision making"""
        if random.random() < self.epsilon:
            return random.randint(0, self.action_size - 1)
        
        # In a real scenario, use a neural network (PyTorch/TF) to predict
        # Current State: [Solar, Wind, Load, SOC]
        return 1 if state[3] < 30 else 2 if state[3] > 80 else 0

    def compute_reward(self, imbalance, soc):
        """Reward function: Kuraivana imbalance-ku high reward"""
        reward = -abs(imbalance) 
        if 40 <= soc <= 70:
            reward += 10 # Healthy SOC reward
        return reward