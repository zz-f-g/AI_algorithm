import numpy as np

# It defines a Markov Decision Process (MDP) with a 7-state grid world, where the agent can move left
# or right, and the reward is 5 for reaching the leftmost state and 10 for reaching the rightmost
# state.
class Mdp:
    def __init__(self):
        """
        The function initializes the size of the grid, the discount factor, the probability of action, the
        transition matrix, and the reward matrix
        """
        self.size = 7
        self.gamma = 0.5
        self.p_a = (1,)
        self.P = (
            np.array(
                [
                    [0.5, 0.5, 0, 0, 0, 0, 0],
                    [0.5, 0, 0.5, 0, 0, 0, 0],
                    [0, 0.5, 0, 0.5, 0, 0, 0],
                    [0, 0, 0.5, 0, 0.5, 0, 0],
                    [0, 0, 0, 0.5, 0, 0.5, 0],
                    [0, 0, 0, 0, 0.5, 0, 0.5],
                    [0, 0, 0, 0, 0, 0.5, 0.5]
                ]
            ),
        )
        self.R = np.array([5, 0, 0, 0, 0, 0, 10], dtype=float)
    def iter(self, V):
        """
        For each action, multiply the probability of that action by the sum of the reward for that action
        and the discounted value of the next state.
        
        :param V: the value function
        :return: The value function for each state.
        """
        V_ = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)
        for i in range(len(self.p_a)):
            V_ += self.p_a[i] * (self.R + self.gamma * np.dot(self.P[i], V))
        return V_

if __name__ == '__main__':
    mdp = Mdp()
    V = mdp.R
    for i in range(100):
        V = mdp.iter(V)
    print(V)
