import pandas as pd
import numpy as np


# ======================= CUSTOM REGRESSORS ===================== ]

# __2.0__

def run_classifier(model, X, y, test_size=0.2, random_state=42, k=2, scaler=False, rd=4, plot=False):
    '''
    Author: Aru Raghuvanshi

    This Functions Fits a classification model with the Train Datasets and
    predicts on a Test Dataset and evaluates its various metrics.
    Also returns fittedmodel that can be used to predict on other test datasets.

    Arguments: estimator, predictor matrix, labels, test size, random state,
    Kfolds, rounding value of metrics and plot of scores
    ----------------------------------------------------------------------------------------------------

    Example usage:

    rr = RandomForestClassifier(n_estimators=100, max_depth=3, verbose=1)

    mod, y_pred = run_classifier(rr, X_train, X_test, y_train, y_test, k=5)

    score = accuracy_score(y_test, y_pred)

    y_pred2 = mod.predict(X_test2)
    conf_matrix = confusion_matrix(y_test2, y_pred2)
    ------------------------------------------------------------

    Returns: Fittedmodel, Predictions, Plot

    '''

    import warnings
    from warnings import filterwarnings
    from sklearn.model_selection import KFold, cross_val_score, train_test_split
    from sklearn.metrics import classification_report, confusion_matrix
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import StandardScaler
    import numpy as np
    import pandas as pd

    warnings.filterwarnings('ignore')
    sc = StandardScaler()

    xtr, xt, ytr, yt = train_test_split(X, y, test_size=test_size, random_state=random_state)

    if scaler == True:
        xtr = sc.fit_transform(xtr)
        xt = sc.transform(xt)

    fittedmodel = model.fit(xtr, ytr)

    pred = model.predict(xt)

    kf = KFold(n_splits=k, random_state=random_state)

    graphtr = cross_val_score(model, xtr, ytr, cv=kf, scoring='accuracy')
    graphte = cross_val_score(model, xt, yt, cv=kf, scoring='accuracy')

    tr = np.mean(cross_val_score(model, xtr, ytr, cv=kf, scoring='accuracy'))
    te = np.mean(cross_val_score(model, xt, yt, cv=kf, scoring='accuracy'))

    #     tepr = round(np.mean(cross_val_score(model, xt, yt, cv=kf, scoring='precision_weighted')), rd)
    #     tere = round(np.mean(cross_val_score(model, xt, yt, cv=kf, scoring='recall_weighted')), rd)
    #     tef1 = round(np.mean(cross_val_score(model, xt, yt, cv=kf, scoring='f1')), rd)
    tr = round(tr, rd)
    te = round(te, rd)

    if 1.1 > tr / te > 1.07:
        fit = 'Slight Over-Fit'
    elif 0.89 < tr / te < 0.93:
        fit = 'Slight Under-Fit'
    elif tr / te > 1.1:
        fit = 'Over-Fitted'
    elif tr / te < 0.89:
        fit = 'Under-Fitted'
    else:
        fit = 'Good Fit'

    cm = confusion_matrix(yt, pred)

    cr = classification_report(yt, pred, output_dict=True)
    cr = pd.DataFrame(cr).T

    for i in cr.columns:
        cr[i] = round(cr[i], rd)

    table = pd.DataFrame({
        'CV Training Score': [tr],
        'CV Test Score': [te],
        'Fit': [fit]
    }).T

    table.rename(columns={0: 'Accuracy Score'}, inplace=True)

    if plot == True:
        fig = plt.figure(figsize=(14, 5))
        plt.ylim(0, 1)
        plt.plot(range(1, k + 1), graphtr, label='Cross Validated Training Scores', color='navy',
                 marker='o', mfc='black', ls='dashed')
        plt.plot(range(1, k + 1), graphte, label='Cross Validated Test Scores', color='salmon',
                 marker='o', mfc='red')
        plt.xlabel('Cross Validation Iterations', fontsize=14)
        plt.ylabel('Model Scores', fontsize=14)
        plt.title('Train vs Test Scores', fontsize=16)
        plt.legend(fontsize=14)

    print('\n\t\t\033[1;30mClassification Report\033[0m')
    display(cr)
    display(table)
    print(f'\n\033[1;30mConfusion Matrix:\033[0m \n{cm}')

    return fittedmodel, pred


# ============================= FIT CLASSIFY ============================ ]


# __1.9__

def run_classifier(model, xtr, xt, ytr, yt, k=2):
    '''
    Author: Aru Raghuvanshi

    This Functions Fits a classification model with the Train Datasets and
    predicts on a Test Dataset and evaluates its various metrics.
    Also returns fittedmodel that can be used to predict on other test datasets.

    Arguments: estimator, X_train, X_test, y_train, y_test
    --------------------------------------------------------

    Example usage:

    rr = RandomForestClassifier(n_estimators=100, max_depth=3, verbose=1)

    mod, y_pred = run_classifier(rr, X_train, X_test, y_train, y_test, k=5)

    score = accuracy_score(y_test, y_pred)

    y_pred2 = mod.predict(X_test2)
    conf_matrix = confusion_matrix(y_test2, y_pred2)
    ------------------------------------------------------------



    Returns: Fittedmodel, Predictions, Plot

    '''

    import warnings
    from warnings import filterwarnings
    from sklearn.model_selection import KFold, cross_val_score
    from sklearn.metrics import classification_report
    import matplotlib.pyplot as plt

    warnings.filterwarnings('ignore')

    fittedmodel = model.fit(xtr, ytr)
    #     tr = model.score(xtr, ytr)
    #     te = model.score(xt, yt)
    #     global pred
    pred = model.predict(xt)

    kf = KFold(n_splits=k, random_state=22)

    graphtr = cross_val_score(model, xtr, ytr, cv=kf, scoring='accuracy')
    graphte = cross_val_score(model, xt, yt, cv=kf, scoring='accuracy')

    tr = np.mean(cross_val_score(model, xtr, ytr, cv=kf, scoring='accuracy'))
    te = np.mean(cross_val_score(model, xt, yt, cv=kf, scoring='accuracy'))

    tepr = np.mean(cross_val_score(model, xt, yt, cv=kf, scoring='precision_weighted'))
    tere = np.mean(cross_val_score(model, xt, yt, cv=kf, scoring='recall_weighted'))
    tef1 = np.mean(cross_val_score(model, xt, yt, cv=kf, scoring='f1'))
    tr = tr * 100
    te = te * 100

    if 1.1 > tr / te > 1.07:
        fit = 'Slight Over-Fit'
    elif 0.89 < tr / te < 0.93:
        fit = 'Slight Under-Fit'
    elif tr / te > 1.1:
        fit = 'Over-Fitted'
    elif tr / te < 0.89:
        fit = 'Under-Fitted'
    else:
        fit = 'Good Fit'

    table = pd.DataFrame({
        'CV Training Score': [tr],
        'CV Test Score': [te],
        'Precision': [tepr],
        'Recall': [tere],
        'F1-Score': [tef1],
        'Fit': [fit]
    }).T

    table.rename(columns={0: 'Score'}, inplace=True)

    fig = plt.figure(figsize=(14, 5))
    plt.ylim(0, 1)
    plt.plot(range(1, k + 1), graphtr, label='Cross Validated Training Scores', color='navy',
             marker='o', mfc='black', ls='dashed')
    plt.plot(range(1, k + 1), graphte, label='Cross Validated Test Scores', color='salmon',
             marker='o', mfc='red')
    plt.xlabel('Cross Validation Iterations', fontsize=14)
    plt.ylabel('Model Scores', fontsize=14)
    plt.title('Train vs Test Scores', fontsize=16)
    plt.legend(fontsize=14)


    display(table)

    return fittedmodel, pred





# ---------------------------------KMEANS K FINDER ------------------------------]


def kmeans_kfinder(dtf, lower=1, upper=9):

    '''
    Author: Aru Raghuvanshi

    Standardize (StandardScaler) data before feeding to function.
    This functions plots the Elbow Curve for KMeans Clustering
    to find the elbow value of K.

    Arguments: (dataframe, lower=1, upper=9)
    Returns: Plot

    Defaults of lower=0, upper=7
    Example: e = elbowplot(df, 0, 5)
    '''

    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt
    plt.style.use('seaborn')

    #     from scipy.spatial.distance import cdist
    k_range = range(lower, upper)
    sse = []
    for i in k_range:
        km = KMeans(n_clusters=i)
        km.fit(dtf)
        sse.append(km.inertia_)
    #       sse.append(sum(np.min(cdist(dtf, km.cluster_centers_, 'euclidean'), axis=1)) / dtf.shape[0]))

    plt.figure(figsize=(14, 6))
    plt.plot(k_range, sse, label='K vs SSE', color='g', lw=3, marker='o', mec='black')
    plt.xlabel('K', fontsize=18)
    plt.title('KMEANS ELBOW PLOT - K vs Sum of Square Error', fontsize=16)
    plt.legend()
    plt.show()



# ----------------------------- KNN K FINDER --------------------------------]


def knn_kfinder(xtr, xt, ytr, yt, lower=1, upper=30):

    '''
    Author: Aru Raghuvanshi

    This function plots the KNN elbow plot to figure out
    the best value for K in the KNN Classifier.

    Arguments: (xtr, xt, ytr, yt, lower=1, upper=30)
    Returns: Plot

    Example: p = knn_plot(X_train, X_test, y_train, y_test, 1, 30)

    '''
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score
    import matplotlib.pyplot as plt
    plt.style.use('seaborn')

    krange = range(lower, upper)
    acc_score = []
    # Might take some time
    for i in krange:
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(xtr, ytr)
        pred_i = knn.predict(xt)
        acc_score.append(accuracy_score(yt, pred_i))

    plt.figure(figsize=(14, 6))
    plt.plot(krange, acc_score, color='salmon', linestyle='solid',
             marker='o', mfc='purple', label='K vs Testing Accuracy', lw=2)
    plt.title('KNN K-GRAPH')
    plt.xlabel('K', fontsize=18)
    plt.ylabel('Test Accuracy', fontsize=16)
    plt.legend()
    plt.show()