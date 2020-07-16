"""Various helper functions to compute and plot metrics."""
import itertools

import matplotlib.pyplot as plt
import numpy as np
import typing
import feyn.losses
import feyn.metrics

from ._set_style import abzu_mplstyle

abzu_mplstyle()

def plot_confusion_matrix(y_true: typing.Iterable,
                          y_pred: typing.Iterable,
                          labels: typing.Iterable=None,
                          title:str='Confusion matrix',
                          color_map="abzu-partial") -> None:
    """
    Compute and plot a Confusion Matrix.

    Arguments:
        y_true -- Expected values (Truth)
        y_pred -- Predicted values
        labels -- List of labels to index the matrix
        color_map -- Color map from matplotlib to use for the matrix

    Returns:
        [plot] -- matplotlib confusion matrix
    """
    if labels is None:
        labels = np.union1d(y_pred,y_true)

    cm = feyn.metrics.confusion_matrix(y_true, y_pred)

    plt.title(title)
    tick_marks = range(len(labels))
    plt.xticks(tick_marks, labels, rotation=45)
    plt.yticks(tick_marks, labels)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], 'd'),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('Expected')
    plt.xlabel('Predicted')

    plt.imshow(cm, interpolation='nearest', cmap=color_map)
    plt.colorbar()
    plt.tight_layout()
    return plt.show()


def plot_regression_metrics(y_true: typing.Iterable, y_pred: typing.Iterable, title:str="Regression metrics") -> None:
    """
    Plot metrics for a regression problem.

    The y-axis is the range of values in y_true and y_pred.

    The x-axis is all the samples, sorted in the order of the y_true.

    With this, you are able to see how much your prediction deviates from expected in the different prediction ranges.

    So, a good metric plot, would have the predicted line close and smooth around the predicted line.

    Normally you will see areas, where the predicted line jitter a lot scores worse against the test data there.


    Arguments:
        y_true -- Expected values (Truth).
        y_pred -- Predicted values.
        title -- Title of the plot.

    Raises:
        ValueError: When y_true and y_pred do not have same shape
    """
    if type(y_true).__name__ == "Series":
        y_true = y_true.values

    if type(y_pred).__name__ == "Series":
        y_pred = y_pred.values

    if (len(y_true) != len(y_pred)):
        raise ValueError('Size of expected and predicted are different!')

    sort_index = np.argsort(y_true)
    expected = y_true[sort_index]
    predicted = y_pred[sort_index]

    plt.title(title)
    plt.plot(expected, label='Expected')
    plt.plot(predicted, label='Predicted')
    plt.xticks([])
    plt.legend()


def plot_segmented_loss(graph: feyn.Graph, data:typing.Iterable, by:typing.Optional[str] = None, loss_function="squared_error") -> None:
    """
    Plot the loss by segment of a dataset.

    This plot is useful to evaluate how a model performs on different subsets of the data.

    Example:
    > qg = qlattice.get_qgraph(["age","smoker","heartrate"], output="heartrate")
    > qg.fit(data)
    > best = qg[0]
    > feyn.plots.plot_segmented_loss(best, data, by="smoker")

    This will plot a histogram of the model loss for smokers and non-smokers separately, which can help evaluate wheter the model has better performance for euther of the smoker sub-populations.

    You can use any column in the dataset as the `by` parameter. If you use a numerical column, the data will be binned automatically.

    Arguments:
        graph -- The graph to plot.
        data -- The dataset to measure the loss on.
        by: -- The column in the dataset to segment by.
    """

    if by is None:
        by=graph[-1].name

    bins, cnts, statistic = feyn.metrics.segmented_loss(graph, data, by, loss_function)

    fig, ax1 = plt.subplots()
    plt.xlabel("Segmented by "+by)
    plt.ylabel("Number of samples")

    if type(bins[0]) == tuple: 
        bins = [(e[0]+e[1])/2 for e in bins]
        w = .8 * (bins[1]-bins[0])
        ax1.bar(bins, height=cnts, width=w)
    else:
        ax1.bar(bins, height=cnts)
        
    ax2 = ax1.twinx()
    plt.ylabel("Loss")
    ax2.plot(bins,statistic,c="#f00", marker="o")
    ax2.set_ylim(bottom=0)


