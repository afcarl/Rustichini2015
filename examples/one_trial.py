import dotdot
from neuromodel import Model

model = Model(range_A=[0, 20], range_B=[0, 20], random_seed=1)
model.one_trial(1, 0)
