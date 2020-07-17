import logging
import numpy as np
import scipy as sp
import scipy.stats
from matplotlib import pyplot as plt
from ngboost.manifold import manifold
from ngboost.distns import MultivariateNormal
from ngboost.distns import BivariateNormal
from ngboost.scores import MLE


def Y_join(T, E):
    col_event = 'Event'
    col_time = 'Time'
    y = np.empty(dtype=[(col_event, np.bool), (col_time, np.float64)],
                 shape=T.shape[0])
    y[col_event] = E
    y[col_time] = T
    return y


def gen_data(N, mu0, mu1, var0, var1, cor):
    mu = [mu0, mu1]
    S01 = cor*np.sqrt(var1)*np.sqrt(var0)
    S = [[var0, S01], [S01, var1]]
    R = sp.stats.multivariate_normal(mean=mu, cov=S)
    raw = np.array([R.rvs() for _ in range(N)])
    T = np.min(raw, axis=1)
    E = raw[:, 0] < raw[:, 1]

    print('Prevalence:', np.mean(E))
    print('mu_E:', mu0)
    print('Marginal Mean of E:', np.mean( T[np.where(E == 1)] ))
    print('mu_C:', mu1)
    print('Marginal Mean of C:', np.mean( T[np.where(E == 0)] ))
    
    Y = Y_join(T, E)
    return Y, raw


def plot(raw, label):
    
    E = raw[:,0][raw[:,0] < raw[:, 1]]
    C = raw[:,1][raw[:,0] > raw[:, 1]]
    
    plt.subplot(3,1,1)
    kde = sp.stats.gaussian_kde(E)
    x_axis = np.linspace(-5, 5, 200)
    plt.plot(x_axis, kde(x_axis), label=label)
    plt.title("Conditional Event Time")

    plt.subplot(3,1,2)
    kde = sp.stats.gaussian_kde(C)
    x_axis = np.linspace(-5, 5, 200)
    plt.plot(x_axis, kde(x_axis), label=label)
    plt.title("Conditional Censored Time")

    plt.subplot(3,1,3)
    plt.scatter(raw[:100,0], raw[:100,1], label=label)
    plt.xlim(-3, 7)
    plt.title("Joint Density")

    plt.legend()
    plt.tight_layout()


class SurvivalDistn(BivariateNormal):         # Creates a new dist class from a given dist. The new class has its implemented scores
    scores = BivariateNormal.censored_scores  # set to the censored versions of the scores implemented for dist
    def fit(Y):                    # and expects a {time, event} array as Y.
        return Dist.fit(Y["Time"])

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    N = 500
    Y, raw = gen_data(N, 1, 1, 1, 1, 0)

    lr = 1e-2
    niter = 1000
    params = np.array([[0, .1, .05, .1, 0.1]] * N).T
    breakpoint()
    loss = []

    Score = SurvivalDistn.implementation(MLE, SurvivalDistn.censored_scores)
    Manifold = manifold(Score, SurvivalDistn)

    for i in range(niter):
        M = Manifold(params)
        loss_curr = M.score(Y).mean()
        logger.info(f"{i}: {loss_curr:.2f}")
        grad = np.mean(M.d_score(Y).T, axis=1, keepdims=True)
        params = params - lr * grad
        if np.linalg.norm(grad) < 1e-4:
            break

    _, sample = gen_data(N, params[1,0], params[0,0],
                         np.exp(params[2,0])**2, np.exp(params[3,0])**2,
                         np.tanh(params[4,0]))

    print("Fitted Params")
    print("Mu0: {}".format(params[1,0]))
    print("Mu1: {}".format(params[0,0]))
    print("Var0: {}".format(np.exp(params[3,0])**2))
    print("Var1: {}".format(np.exp(params[2,0])**2))
    print("Cor: {}".format(np.tanh(params[4,0])))
    print("=======================")
    
    plot(raw, "truth")
    plot(sample, "fitted")
    plt.show()

