import pathos

import dotdot
from neuromodel import Offers, Model, ReplicatedModel, run_model


ΔA, ΔB, n = 10, 20, 4000
offers = Offers(ΔA=ΔA, ΔB=ΔB, n=n, random_seed=0
                range_A=(0, 10), range_B=(0, 20))
assert range_A == (0, 10)

def compute_fig7_data(model_class=Model, w_p=1.82):
    model = model_class(n=n, ΔA=ΔA, ΔB=ΔB, random_seed=1, w_p=1.82,
                        range_A=offers.range_A, range_B=offers.range_B,
                        hysteresis=True)

    filename_suffix = '_replicate' if model_class is ReplicatedModel else ''
    filename='data/fig7_{}[{}]{}.pickle'.format(w_p, n, filename_suffix)
    return run_model(model, offers, history_keys=('r_ovb', 'r_2', 'r_I'), filename=filename)


if __name__ == '__main__':
    pool = pathos.multiprocessing.Pool()
    pool.map(compute_fig7_data, [Model, ReplicatedModel])
