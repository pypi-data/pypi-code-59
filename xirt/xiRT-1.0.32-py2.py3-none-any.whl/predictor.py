"""Module to organize predictions from CLMS data."""
import sys

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

from xirt import processing as xp
from xirt import sequences as xs
from xirt import xirtnet


class ModelData:
    """Class to keep data together."""

    def __init__(self, psms_df, features1, features2=pd.DataFrame(), le=None):
        """
        Class to keep the model data at a single place.

        Args:
            psms_df: df, dataframe with identifications
            features1: df, features for the second peptide
            features2: df, features for the second peptide
            le:
        """
        self.psms = psms_df
        self.features1 = features1
        self.features2 = features2
        self.le = le
        self.train_idx = []
        self.predict_idx = []
        self.cv_idx = []
        self.shuffled = False
        # init prediction df
        self.prediction_df = pd.DataFrame(index=psms_df.index)

    def set_fdr_mask(self, fdr_cutoff, str_filter=""):
        """
        Set the training mask on the input data.

        Args:
            fdr_cutoff: float, fdr cutoff to be used
            str_filter: str, a string filter to include psms only if containg the given string

        Returns:
            None
        """
        if str_filter == "":
            fdr_mask = (self.psms["FDR"] <= fdr_cutoff) & self.psms["isTT"]
        else:
            fdr_mask = (self.psms["FDR"] <= fdr_cutoff) & (self.psms["isTT"]) \
                & (self.psms["Fasta1"].str.contains("_ECOLI")) \
                & (self.psms["Fasta2"].str.contains("_ECOLI"))
        self.psms["fdr_mask"] = fdr_mask

    def set_unique_shuffled_sampled_training_idx(self, sample_frac=1, random_state=42):
        """
        Set the training index based on fdr mask and removing duplicates.

        This function also servers for learning curves (by reducing the sample_frac) and
        CV variations (using different states).

        Args:
            sample_frac: float, percentage of training samples to use
            random_state: int, random state

        Returns:
            None
        """
        psms_train_idx = self.psms[
            (self.psms["fdr_mask"]) & (~self.psms["Duplicate"].astype(bool))].sample(
            frac=sample_frac, random_state=random_state).index
        self.train_idx = psms_train_idx
        self.predict_idx = self.psms.index.difference(psms_train_idx)
        self.shuffled = True

    def iter_splits(self, n_splits, test_size):
        """
        Return iterator indicies for training, testing, validation based on the training data.

        The returned indices belong to the training data, validation data and prediction data.
        The prediction fold is used in xiRT to predict RTs without using the observations during
        training.

        Args:
            n_splits: int, number of crossvalidation splits
            test_size: float, percentage of validation data to use

        Returns:
            iterator, (train_idx, val_idx, pred_idx)
        """
        if not self.shuffled:
            raise ValueError("Data must be shuffled to avoid undesired bias in the splits.")

        if test_size <= 0:
            raise ValueError('Test split value must be > 0. Please set test_size to min 0.1 (10%).')

        # note: code with *loc indicates 0 based locations. code with idx indicates pandas index
        # used for train/validation splits
        cv_folds_ar = np.arange(n_splits) + 1
        cv_pattern = ["t"] * (cv_folds_ar[-1] - 1) + ["v"]
        train_df_idx = self.train_idx.values

        if len(cv_pattern) == 1:
            # train on entire data set - a fraction for testing/validation is mandatory!
            # syntax a bit confusing:
            # split data into 100% - 2x test size, % test size, % test size
            # e.g. test-size= 10% --> 80%, 10%, 10%
            # prediction set is used for model assessment here
            train_idx, val_idx, pre_idx = \
                np.split(train_df_idx, [int((1 - test_size * 2) * len(train_df_idx)),
                                        int((1 - test_size) * len(train_df_idx))])
            yield train_idx, val_idx, pre_idx

        else:
            # get n_splits of the training
            kf = KFold(n_splits=n_splits, shuffle=False)
            kf.get_n_splits(self.features1.loc[self.train_idx])
            cv_locs = np.array([i[1] for i in kf.split(self.features1.loc[self.train_idx])])

            for i in cv_folds_ar:
                # this will get all the slices where "t" indicates the training
                # here the validation data should be dependant on the CV fold sizes
                train_msk = np.array(cv_pattern) == "t"

                # combine 2 test folds to get a training fold
                # get train folds -> get locations -> get index
                train_init_idx = train_df_idx[np.concatenate(cv_locs[train_msk])]
                train_idx, val_idx = np.split(train_init_idx,
                                              [int((1 - test_size) * len(train_init_idx))])

                # take a testing fold
                pre_idx = train_df_idx[cv_locs[~train_msk][0]]

                # change the pattern for next iteration
                cv_pattern = cv_pattern[1:] + [cv_pattern[0]]

                yield train_idx, val_idx, pre_idx

    def get_train_psms(self):
        """
        Return the psms used for training.

        Returns:
            df, dataframe with psms passing training conditions
        """
        return self.psms.loc[self.train_idx]

    def get_predict_psms(self):
        """
        Return the psms used for prediction.

        Returns:
            df, dataframe with psms passing training conditions
        """
        return self.psms.loc[self.predict_idx]

    def get_features(self, idx, meta=False):
        """
        Return the feature format for multi-task learning for linear and crosslinked peptides.

        Args:
            idx: ar-like, indices to subset feature data
            meta: bool, if meta features should be included.

        Returns:
            df, feature dataframe
        """
        if meta:
            # TODO
            xfeatures = None
        else:
            xfeatures = (self.features1.filter(regex="rnn").loc[idx],
                         self.features2.filter(regex="rnn").loc[idx])
        return xfeatures

    def get_classes(self, idx, frac_cols, cont_cols):
        """
        Return the feature format for multi-task learning for linear and crosslinked peptides.

        Args:
            idx: ar-like, indices to subset feature data
            frac_cols: ar-like, strings with categorical variables
            cont_cols: ar-like, strings with continuous variables
        Returns:
            df, feature dataframe
        """
        # if only continous columns, only return these etc.
        if len(frac_cols) == 0:
            return [self.psms[ccol].loc[idx].values for ccol in cont_cols]

        if len(cont_cols) == 0:
            return [xirtnet.reshapey(self.psms[fcol].loc[idx].values) for fcol in frac_cols]

        y_var = [xirtnet.reshapey(self.psms[fcol].loc[idx].values) for fcol in frac_cols]
        y_var.extend([self.psms[ccol].loc[idx].values for ccol in cont_cols])
        return y_var

    def predict_and_store(self, xirtnetwork, xdata, store_idx):
        """
        Generate and store predictions for the observations from store_idx.

        Formatting, prediction and indexing is all done via this high-level wrapper function.
        The given network model will be used to predict for all CSMs (store_idx) the respective
        RT dimensions. The predictions are processed so that they can be stored in a table.

        Parameters:
            xirtnetwork: xirnetwork, class object xirt
            xdata: tuple of dataframes, corresponding on the RNN / features of the one/two peptides
            store_idx: ar-like, indices to be used for the prediction process.

        Returns:
            None
        """
        # store crosslink predictions
        predictions = xirtnetwork.model.predict(xdata)
        self.store_predictions(xirtnetwork, predictions, store_idx, suf="")

        # if single predictions should be included in the df.Not meaningful for linear peptides.
        # For crosslinked peptides, the raw RT time of the two peptides are added.
        if xirtnetwork.siamese_p["single_predictions"]:
            # create dummy input with all zeroes as second peptide
            dummy = np.zeros_like(xdata[0])
            pep1_predictions = xirtnetwork.model.predict((xdata[0], dummy))
            self.store_predictions(xirtnetwork, pep1_predictions, store_idx, suf="peptide1")

            pep2_predictions = xirtnetwork.model.predict((xdata[1], dummy))
            self.store_predictions(xirtnetwork, pep2_predictions, store_idx, suf="peptide2")

    def store_predictions(self, xirtnetwork, predictions, store_idx, suf=""):
        """
        Format predictions to store them in a prediction dataframe.

        This function processes linear, softmax, sigmoid predictions differently. For linear
        activations no processing apart from 1d flattening is done. For softmax the class prediction
        and the probability are retrieved. For sigmoid (usually used for ordered regression style
        predictions, the class values are retrieved.

        Args:
            xirtnetwork:    tf obj, trained network model
            predictions: ar-like, array with predictions
            store_idx: ar-like, index belonging to the predictions to the predictions
            suf: str, suffix to append to the default column names for the predictions
        Returns:
            None
        """
        # make column name nicer
        if len(suf) > 0:
            suf = "-" + suf

        # make sure list is iterable per task
        if len(xirtnetwork.tasks) == 1:
            predictions = [predictions]

        for task_i, pred_ar in zip(xirtnetwork.tasks, predictions):
            # get activation type because linear, sigmoid, softmax all require different encoding/
            pred_type = xirtnetwork.output_p[task_i + "-activation"]

            # only init once
            if task_i + "-prediction" + suf not in self.prediction_df.columns:
                self.prediction_df[task_i + "-prediction" + suf] = -1000000

                # softmax also gets probabilities
                if pred_type == "softmax":
                    self.prediction_df[task_i + "-probability" + suf] = -1000000

            if pred_type == "linear":
                # easiest, just ravel to 1d ar
                self.prediction_df[task_i + "-prediction" + suf].at[store_idx] = np.ravel(
                    pred_ar)

            elif pred_type == "softmax":
                # classification, take maximum probability as class value
                self.prediction_df[task_i + "-prediction" + suf].at[store_idx] = \
                    np.argmax(pred_ar, axis=1) + 1
                self.prediction_df[task_i + "-probability" + suf].at[store_idx] = \
                    np.max(pred_ar, axis=1)

            elif pred_type == "sigmoid":
                self.prediction_df[task_i + "-prediction" + suf].at[store_idx] = \
                    sigmoid_to_class(pred_ar) + 1

            else:
                raise ValueError("{} not supported, only linear/softmax/sigmoid".format(pred_type))


def sigmoid_to_class(predictions, t=0.5):
    """
    Transform an array of sigmoid activations to a class prediction.

    The class prediction will be done to the first entry that has a lower probability than t or
    the last value in the array if no value is smaller than t.

    Args:
        predictions: ar-like, predictions from for ordinal regression task
        t: float, score cutoff to determine prediction.

    Returns:
        ar-like, predictions
    """
    # init output
    pred_hats = np.zeros(len(predictions), dtype=np.intp)

    # iterate over prediction df
    for ii, predi in enumerate(predictions):
        tval = np.where(predi <= t)[0]
        # if all values > t, use last class as predicted label
        pred_hats[ii] = len(predi) - 1 if len(tval) == 0 else tval[0]
    return pred_hats


def preprocess(matches_df, sequence_type="crosslink", max_length=-1, cl_residue=True,
               fraction_cols=[]):
    """Prepare peptide identifications to be used with xiRT.

    High-level wrapper performing multiple steps. In processing order this function:
    sets and index, sorts by score, reorders crosslinked peptides for length (alpha longer),
    rewrites sequences to modX, marks duplicates, modifies cl residues, computes RNN features
    and stores everything in the data model.

    Args:
        matches_df: df, dataframe with peptide identifications
        sequence_type: str, either linear or cross-linked indicating the input molecule type.
        max_length: int, maximal length of peptide sequences to consider. Longer sequences will
        be removed
        cl_residue: bool, if true handles cross-link sites as additional modifications
        fraction_cols: ar-like, list of columsn that encode frationation data
    Returns:
        model_data, processed feature dataframes and label encoder
    """
    # set index
    matches_df.set_index("PSMID", drop=False, inplace=True)

    # sort to keep only highest scoring peptide from duplicated entries
    matches_df = matches_df.sort_values(by="score", ascending=False)

    # generate columns to handle based on input data type
    if sequence_type == "crosslink":
        # change peptide order
        matches_df = xs.reorder_sequences(matches_df)
        seq_in = ["Peptide1", "Peptide2"]

    elif sequence_type == "pseudolinear":
        # TODO
        sys.exit("Sorry, not yet implemented ):. (crosslink, pseudolinears, linear)")

    elif sequence_type == "linear":
        seq_in = ["Peptide1"]
    else:
        sys.exit("sequence type not supported. Must be one of (crosslink, pseudolinears, linear)")

    # dynamically get if linear or crosslinked
    seq_proc = ["Seqar_" + i for i in seq_in]

    # perform the sequence based processing
    matches_df = xp.prepare_seqs(matches_df, seq_cols=seq_in)

    # concat peptide sequences
    matches_df["PepSeq1PepSeq2_str"] = matches_df["Peptide1"] + matches_df["Peptide2"]

    # mark all duplicates
    matches_df["Duplicate"] = matches_df.duplicated(["PepSeq1PepSeq2_str"], keep="first")

    if cl_residue:
        xs.modify_cl_residues(matches_df, seq_in=seq_in)

    # TODO remove longer peptide
    features_rnn_seq1, features_rnn_seq2, le = \
        xp.featurize_sequences(matches_df, seq_cols=seq_proc, max_length=max_length)

    # add the two fraction encoding columns
    # psms_df[col + "_1hot"] and psms_df[col + "_ordinal"]
    if len(fraction_cols) > 0:
        xp.fraction_encoding(matches_df, rt_methods=fraction_cols)

    # keep all data together in a data class
    return ModelData(matches_df, features_rnn_seq1, features_rnn_seq2, le=le)
