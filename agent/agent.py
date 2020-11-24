import json
import os
import random

from .state import State


class Q_State(State):
    '''Augments the game state with Q-learning information'''

    def __init__(self, string):
        super().__init__(string)

        # key stores the state's key string (see notes in _compute_key())
        self.key = self._compute_key()

    def _compute_key(self):
        '''
        Returns a key used to index this state.

        The key should reduce the entire game state to something much smaller
        that can be used for learning. When implementing a Q table as a
        dictionary, this key is used for accessing the Q values for this
        state within the dictionary.
        '''

        #//# ===== ===== ==== = === = === = ==== ===== ===== #\\#
        #//# ===== = = == === ORIGINAL CODE === == = = ===== #\\#
        #//# ===== ===== ==== = === = === = ==== ===== ===== #\\#
        # this simple key uses the 3 object characters above the frog
        # and combines them into a key string
        # return ''.join([
        #     self.get(self.frog_x - 1, self.frog_y - 1) or '_',  # up 1, left 1
        #     self.get(self.frog_x, self.frog_y - 1) or '_',      # up 1
        #     self.get(self.frog_x + 1, self.frog_y - 1) or '_',  # up 1, right 1
        # ])
        #//# ===== ===== ==== = === = === = ==== ===== ===== #\\#
        #//# ===== = = == === ************* === == = = ===== #\\#
        #//# ===== ===== ==== = === = === = ==== ===== ===== #\\#
        


        ## ===== ===== = ===== ===== ##
        ## === == Frog Vision == === ##
        ## ===== ===== = ===== ===== ##

        # Original code is q2




        # q3
        #     -
        #   - - -
        # - - F - -

        # return ''.join([
        #     self.get(self.frog_x - 2, self.frog_y) or '_',  # left 2
        #     self.get(self.frog_x - 1, self.frog_y) or '_',  # left 1
        #     self.get(self.frog_x + 1, self.frog_y) or '_',  # right 1
        #     self.get(self.frog_x + 2, self.frog_y) or '_',  # right 2

        #     self.get(self.frog_x - 1, self.frog_y - 1) or '_',  # up 1, left 1
        #     self.get(self.frog_x, self.frog_y - 1) or '_',      # up 1
        #     self.get(self.frog_x + 1, self.frog_y - 1) or '_',  # up 1, right 1

        #     self.get(self.frog_x, self.frog_y - 2) or '_',  # up 2
        # ])




        # q4
        # - - - - - 
        #   - - -
        #     F

        # Considers logs and grasshoppers
        # return ''.join([
        #     self.get(self.frog_x - 1, self.frog_y - 1) or '_',  # up 1, left 1
        #     self.get(self.frog_x, self.frog_y - 1) or '_',      # up 1
        #     self.get(self.frog_x + 1, self.frog_y - 1) or '_',  # up 1, right 1

        #     self.get(self.frog_x - 2, self.frog_y - 2) or '_',  # up 2, left 2
        #     self.get(self.frog_x - 1, self.frog_y - 2) or '_',  # up 2, left 1
        #     self.get(self.frog_x, self.frog_y - 2) or '_',  # up 2
        #     self.get(self.frog_x + 1, self.frog_y - 2) or '_',  # up 2, right 1
        #     self.get(self.frog_x + 2, self.frog_y - 2) or '_',  # up 2, right 2
        # ])



        # q3.1
        #     -
        #   - - -
        # - - F - -

        # return ''.join([
        #     self.get(self.frog_x - 2, self.frog_y) or '_',  # left 2
        #     self.get(self.frog_x - 1, self.frog_y) or '_',  # left 1
        #     self.get(self.frog_x + 1, self.frog_y) or '_',  # right 1
        #     self.get(self.frog_x + 2, self.frog_y) or '_',  # right 2

        #     self.get(self.frog_x - 1, self.frog_y - 1) or '_',  # up 1, left 1
        #     self.get(self.frog_x, self.frog_y - 1) or '_',      # up 1
        #     self.get(self.frog_x + 1, self.frog_y - 1) or '_',  # up 1, right 1

        #     self.get(self.frog_x, self.frog_y - 2) or '_',  # up 2
        # ])




        # q5
        #   - - -
        #   - - -
        # - - F - -

        # return ''.join([
        #     self.get(self.frog_x - 2, self.frog_y) or '_',  # left 2
        #     self.get(self.frog_x - 1, self.frog_y) or '_',  # left 1
        #     self.get(self.frog_x + 1, self.frog_y) or '_',  # right 1
        #     self.get(self.frog_x + 2, self.frog_y) or '_',  # right 2

        #     self.get(self.frog_x - 1, self.frog_y - 1) or '_',  # up 1, left 1
        #     self.get(self.frog_x, self.frog_y - 1) or '_',      # up 1
        #     self.get(self.frog_x + 1, self.frog_y - 1) or '_',  # up 1, right 1

        #     self.get(self.frog_x - 1, self.frog_y - 2) or '_',  # up 2, left 1
        #     self.get(self.frog_x, self.frog_y - 2) or '_',      # up 2
        #     self.get(self.frog_x + 1, self.frog_y - 2) or '_',  # up 2, right 1
        # ])




        # q6
        # - - - - -
        # - - - - -
        # - - F - -

        # return ''.join([
        #     self.get(self.frog_x - 2, self.frog_y) or '_',  # left 2
        #     self.get(self.frog_x - 1, self.frog_y) or '_',  # left 1
        #     self.get(self.frog_x + 1, self.frog_y) or '_',  # right 1
        #     self.get(self.frog_x + 2, self.frog_y) or '_',  # right 2

        #     self.get(self.frog_x - 2, self.frog_y - 1) or '_',  # up 1, left 2
        #     self.get(self.frog_x - 1, self.frog_y - 1) or '_',  # up 1, left 1
        #     self.get(self.frog_x, self.frog_y - 1) or '_',      # up 1
        #     self.get(self.frog_x + 1, self.frog_y - 1) or '_',  # up 1, right 1
        #     self.get(self.frog_x + 2, self.frog_y - 1) or '_',  # up 1, right 2

        #     self.get(self.frog_x - 2, self.frog_y - 2) or '_',  # up 2, left 2
        #     self.get(self.frog_x - 1, self.frog_y - 2) or '_',  # up 2, left 1
        #     self.get(self.frog_x, self.frog_y - 2) or '_',      # up 2
        #     self.get(self.frog_x + 1, self.frog_y - 2) or '_',  # up 2, right 1
        #     self.get(self.frog_x + 2, self.frog_y - 2) or '_',  # up 2, right 2
        # ])



        # q8
        #   - - -
        #   - F -
        #   - - -

        # return ''.join([
        #     self.get(self.frog_x - 1, self.frog_y + 1) or '_',  # down 1, left 1
        #     self.get(self.frog_x, self.frog_y + 1) or '_',      # down 1
        #     self.get(self.frog_x + 1, self.frog_y + 1) or '_',  # down 1, right 1

        #     self.get(self.frog_x - 1, self.frog_y) or '_',  # left 1
        #     self.get(self.frog_x + 1, self.frog_y) or '_',  # right 1

        #     self.get(self.frog_x - 1, self.frog_y - 1) or '_',  # up 1, left 1
        #     self.get(self.frog_x, self.frog_y - 1) or '_',      # up 1
        #     self.get(self.frog_x + 1, self.frog_y - 1) or '_',  # up 1, right 1
        # ])


        # q9
        #   - - -
        #   - F -
        #   - - -

        return ''.join([
            self.get(self.frog_x - 1, self.frog_y + 1) or '_',  # down 1, left 1
            self.get(self.frog_x, self.frog_y + 1) or '_',      # down 1
            self.get(self.frog_x + 1, self.frog_y + 1) or '_',  # down 1, right 1

            self.get(self.frog_x - 1, self.frog_y) or '_',  # left 1
            self.get(self.frog_x + 1, self.frog_y) or '_',  # right 1

            self.get(self.frog_x - 1, self.frog_y - 1) or '_',  # up 1, left 1
            self.get(self.frog_x, self.frog_y - 1) or '_',      # up 1
            self.get(self.frog_x + 1, self.frog_y - 1) or '_',  # up 1, right 1
        ])




        ## ===== ===== = ===== ===== ##
        ## === == =========== == === ##
        ## ===== ===== = ===== ===== ##
    
    def reward(self, prev_distance_to_goal=None):
        '''Returns a reward value for the state.'''

        if self.at_goal:
            return self.score
        elif self.is_done:
            return -10
        else:
            # Test the Frog's change in position from the goal.
            if not prev_distance_to_goal:
                return 0
            elif self.frog_y == prev_distance_to_goal:
                return 0
            elif self.frog_y < prev_distance_to_goal:
                return 1
            else:
                return -1


class Agent:
    DEFAULT_E_INTERVAL = 1000
    INITIAL_EPSILON = 1

    def __init__(self, train=None):

        # train is either a string denoting the name of the saved
        # Q-table file, or None if running without training
        self.train = train

        # q is the dictionary representing the Q-table
        self.q = {}

        # name is the Q-table filename
        # (you likely don't need to use or change this)
        self.name = train or 'q'

        # path is the path to the Q-table file
        # (you likely don't need to use or change this)
        self.path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), 'train', self.name + '.json')

        self.load()

        self.prev_qstate = None
        self.prev_action = None
        self.epsilon = Agent.INITIAL_EPSILON # Epsilon determines if agent will explore or exploit.
        self.e_decrement = 0.1 # Value to decrement epsilon after an interval.
        self.e_interval = Agent.DEFAULT_E_INTERVAL # Number of choices before decrementing epsilon.
        self.alpha = 0.1 # 1 means we completely abandon the old value.
        self.prev_distance_to_goal = None
        self.episode_num = 1
        self.episode_rewards = [0]

    def load(self):
        '''Loads the Q-table from the JSON file'''
        try:
            with open(self.path, 'r') as f:
                self.q = json.load(f)
            if self.train:
                print('Training {}'.format(self.path))
            else:
                print('Loaded {}'.format(self.path))
        except IOError:
            if self.train:
                print('Training {}'.format(self.path))
            else:
                raise Exception('File does not exist: {}'.format(self.path))
        return self

    def save(self):
        '''Saves the Q-table to the JSON file'''
        with open(self.path, 'w') as f:
            json.dump(self.q, f)
        return self

    def choose_action(self, state_string):
        '''
        Returns the action to perform.

        This is the main method that interacts with the game interface:
        given a state string, it should return the action to be taken
        by the agent.

        The initial implementation of this method is simply a random
        choice among the possible actions. You will need to augment
        the code to implement Q-learning within the agent.
        '''
        # return random.choice(State.ACTIONS)

        # Construct internal Q-State using given state string.
        qstate = Q_State(state_string)

        if self.train:
            # Train the Q-table.
            action = self.train_qtable(qstate)
            self.save()
        else:
            try:
                # Get the optimal next action.
                action = self.optimal_next_action(qstate)
            except KeyError:
                # Q-state is not in Q-table, choose random action.
                action = random.choice(State.ACTIONS)

        self.prev_distance_to_goal = qstate.frog_y

        return action

    def train_qtable(self, qstate):
        
        # Test if Q-state does not already exist in Q-table.
        if qstate.key not in self.q:
            self.initialize_qstate(qstate)
        
        # Use epsilon to decide if agent will Explore or Exploit.
        if self.epsilon > 0:
            self.decrement_epsilon_interval()
            next_action = (self.optimal_next_action(qstate)
                if random.random() > self.epsilon
                else random.choice(State.ACTIONS))
        else:
            next_action = self.optimal_next_action(qstate)
        
        if self.prev_qstate and self.prev_action:
            reward = self.update_qtable(qstate, next_action)
            self.episode_rewards[self.episode_num] += reward
        
        # Update previous Q-state and action.
        self.prev_qstate = qstate
        self.prev_action = next_action

        return next_action

    def decrement_epsilon_interval(self):
        '''Decrement the epsilon interval value by 1. If the interval drops to 
        zero, then decrement the epsilon value and reset the interval.'''
        # Take care of epsilon (Explore/Exploit) factor.
        # Decrement epsilon by e_decrement after e_interal.
        self.e_interval = round(self.e_interval - 1, 1)
        # Test if new episode beginning.
        if self.e_interval <= 0:
            self.epsilon = round(self.epsilon - self.e_decrement, 1)
            self.e_interval = Agent.DEFAULT_E_INTERVAL
            self.episode_rewards.append(0)
            self.episode_num += 1

    def update_qtable(self, qstate, next_action):
        '''Update the Q-value for the previous state-action pair in the Q-table.'''
        old_qval = self.qval(self.prev_qstate, self.prev_action) # If no previous state, then returns 0.
        reward = qstate.reward(self.prev_distance_to_goal) # The reward received for taking the previous action.

        optimal_qval = self.qval(qstate, next_action)
        
        # Formulate the new Q-value for the previous action.
        new_qval = ((1 - self.alpha) * old_qval) + (self.alpha * (reward + optimal_qval))
        self.set_new_qval(new_qval)
        return reward

    def optimal_next_action(self, qstate):
        '''optimal_next_action() -> optimal next action
        Determine the optimal next action at the given state.'''
        action_dict = self.q[qstate.key] # { 'd': 0, 'u': 0, 'r': 0, ... }
        action_keys = list(action_dict.keys()) # [ 'd', 'u', 'r', 'l', '_' ]
        action_vals = list(action_dict.values()) # [ 0, 0, 0, ... ]

        # Find the optimal action which maximizes the Q-value.
        max_val_index = action_vals.index(max(action_vals))
        optimal_action = action_keys[max_val_index]

        # # Initialize the optimal action and Q-value.
        # optimal_action = action_keys[0]
        # optimal_qval = action_dict[optimal_action]

        # # Find the real optimal action and Q-value.
        # for i in range(1, len(action_keys)):
        #     this_qval = action_dict[action_keys[i]]
        #     # Test if this action's Q-value is greater than the optimal.
        #     if this_qval > optimal_qval:
        #         optimal_action = action_keys[i]
        #         optimal_qval = this_qval

        return optimal_action

    def qval(self, qstate, action):
        '''Return the Q-value for the given action on the given state.'''
        return self.q[qstate.key][action] if qstate and action else 0

    def set_new_qval(self, qvalue):
        '''Set the given Q value for the given action at the given state.'''
        self.q[self.prev_qstate.key][self.prev_action] = qvalue

    def initialize_qstate(self, qstate):
        '''Initialize the Q-state as a key to a dictionary of actions within
        the Q-table.'''
        if qstate.key not in self.q:
            self.q[qstate.key] = {}
            for s in State.ACTIONS:
                self.q[qstate.key][s] = 0
