import gym
import jericho

from gym.utils import seeding
import numpy as np
from gym import Space

class NaturalLanguage(Space):
    def __init__(self, max_words=None):
        if max_words is not None:
            self.max_words = max_words
        else:
            self.max_words = 500

    def sample(self):
        raise "dummy string!"

    def contains(self, x):
        return (type(x) == str)


class JerichoFrotzEnv(gym.Env):
    def __init__(self, rom_path, seed):
        self.jericho_env = jericho.FrotzEnv(rom_path, seed)
        self.action_space = NaturalLanguage(max_words=4)
        self.observation_space = NaturalLanguage()
        
        self.high = None
        self.low = None

        self.seed(seed)
        self.vocabulary = self.jericho_env.get_dictionary()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))        
        obs, rew, done, info = self.jericho_env.step(action)

        return obs, rew, done, info

    def reset(self):
        obs, _ = self.jericho_env.reset()
        return obs       
    
class Zork1JerichoEnv(JerichoFrotzEnv):
    def __init__(self):
        super(Zork1JerichoEnv, self).__init__('envs/jericho-game-suite/zork1.z5', seed=11)

class Zork2JerichoEnv(JerichoFrotzEnv):
    def __init__(self):
        super(Zork2JerichoEnv, self).__init__('envs/jericho-game-suite/zork2.z5', seed=11)
    
class Zork3JerichoEnv(JerichoFrotzEnv):
    def __init__(self):
        super(Zork3JerichoEnv, self).__init__('envs/jericho-game-suite/zork3.z5', seed=11)

class Nine05JerichoEnv(JerichoFrotzEnv):
    def __init__(self):
        super(Nine05JerichoEnv, self).__init__('envs/jericho-game-suite/905.z5', seed=11)

class AcornCourtJerichoEnv(JerichoFrotzEnv):
    def __init__(self):
        super(AcornCourtJerichoEnv, self).__init__('envs/jericho-game-suite/acorncourt.z5', seed=11)

class AdventJerichoEnv(JerichoFrotzEnv):
    def __init__(self):
        super(AdventJerichoEnv, self).__init__('envs/jericho-game-suite/advent.z5', seed=11)

class AdventureLandJerichoEnv(JerichoFrotzEnv):
    def __init__(self):
        super(AdventureLandJerichoEnv, self).__init__('envs/jericho-game-suite/adventureland.z5', seed=11)

class AfflictedJerichoEnv(JerichoFrotzEnv):
    def __init__(self):
        super(AfflictedJerichoEnv, self).__init__('envs/jericho-game-suite/afflicted.z8', seed=11)

class AnchorJerichoEnv(JerichoFrotzEnv):
    def __init__(self):
        super(AnchorJerichoEnv, self).__init__('envs/jericho-game-suite/anchor.z8', seed=11)

class AwakenJerichoEnv(JerichoFrotzEnv):
    def __init__(self):
        super(AwakenJerichoEnv, self).__init__('envs/jericho-game-suite/awaken.z5', seed=11)
    