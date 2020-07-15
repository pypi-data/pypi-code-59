import numpy as np


def __bernoulli_sim(x, simulations: int = 100):
    """Convenience function for performing bernoulli trial.

    Parameters
    ----------
    x : array-like
        A list of each guest's probability of attending.
    simulations : int, optional
        Number of simulations to run, by default 100

    Returns
    -------
    array
        [description]
    """
    return np.random.binomial(n=1, p=x, size=simulations)


def simulate(guest_probability: list, simulations: int = 100):
    """Simulate the number of attendees of an event based on a list of probabilities.

    Each guest's attendance is modelled as a Bernoulli random variable. Bernoulli
    trials are repeated multiple times for each guest based on the number of
    simulations specified (default is 100 simulations).

    Parameters
    ----------
    guest_probability : list
        List of the probability of each guest attending the event. Must be between 0 and 1.
    simulations : int, optional
        Number of simulations to run, by default 100

    Returns
    -------
    [type]
        [description]
    """
    return np.apply_along_axis(
        __bernoulli_sim, 0, np.atleast_2d(guest_probability), simulations=simulations
    ).sum(axis=1)
