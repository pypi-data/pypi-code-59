import math
import numpy as np
import h5py
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.framework import ops
from utils import load_dataset, flatten, create_placeholders,
initialize_parameters, forward_propagation, compute_cost, random_mini_batches


class Model():

    def __init__(self, layers_list, learning_rate=0.001, n_epochs=10,
                 minibatch_size=32):

        self.layers_list = layers_list
        self.learning_rate = learning_rate
        self.n_epochs = n_epochs
        self.minibatch_size = minibatch_size

    def model(self, path_train_dataset, path_test_dataset, X_train_column,
              Y_train_column, X_test_column, Y_test_column, classes_list,
              optimizer_algo='adam', print_cost=True):

        # load the datasets
        X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = load_dataset(
            path_train_dataset, path_test_dataset, X_train_column,
            Y_train_column, X_test_column, Y_test_column, classes_list)

        # pre-processing
        X_train, Y_train, X_test, Y_test = flatten(X_train_orig, Y_train_orig,
                                                   X_test_orig, Y_test_orig, classes)

        # to be able to rerun the model without overwriting tf variables
        ops.reset_default_graph()
        # (n_x: input size, m : number of examples in the train set)
        (n_x, m) = X_train.shape
        n_y = Y_train.shape[0]        # n_y : output size
        costs = []                    # To keep track of the cost

        # Create Placeholders of shape (n_x, n_y)
        X, Y = create_placeholders(n_x, n_y)

        # Initialize parameters
        parameters = initialize_parameters(self.layers_list, seed=1)

        # Forward propagation: Build for-propagation in the tensorflow graph
        Z_final_layer = forward_propagation(X, parameters)

        # Cost function: Add cost function to tensorflow graph
        cost = compute_cost(Z_final_layer, Y)

        # Backpropagation: Define the tensorflow optimizer. Use AdamOptimizer
        if optimizer_algo == 'gradient_descent':
            optimizer = tf.train.GradientDescentOptimizer(
                learning_rate=self.learning_rate).minimize(cost)

        elif optimizer_algo == 'momentum':
            optimizer = tf.train.MomentumOptimizer(learning_rate=self.learning_rate).minimize(cost)

        elif optimizer_algo == 'adam':
            optimizer = tf.train.AdamOptimizer(learning_rate=self.learning_rate).minimize(cost)

        # Initialize all the variables
        init = tf.global_variables_initializer()

        # Start the session to compute the tensorflow graph
        with tf.Session() as sess:

            # Run the initialization
            sess.run(init)

            # Do the training loop
            for epoch in range(self.n_epochs):

                epoch_cost = 0.                       # Defines a cost related to an epoch
                # number of minibatches of size minibatch_size in the train set
                num_minibatches = int(m / minibatch_size)
                seed = seed + 1
                minibatches = random_mini_batches(X_train, Y_train, self.minibatch_size, seed)

                for minibatch in minibatches:

                    # Select a minibatch
                    (minibatch_X, minibatch_Y) = minibatch
                    _, minibatch_cost = sess.run([optimizer, cost], feed_dict={
                        X: minibatch_X, Y: minibatch_Y})

                    epoch_cost += minibatch_cost / minibatch_size

                # Print the cost every epoch
                if print_cost == True and epoch % 100 == 0:
                    print("Cost after epoch %i: %f" % (epoch, epoch_cost))

                if print_cost == True and epoch % 5 == 0:
                    costs.append(epoch_cost)

            # lets save the parameters in a variable
            parameters = sess.run(parameters)
            print("Parameters have been trained!")

            # stores quantities useful for later
            quantities = {"X": X, "Y": Y, "Z_final_layer": Z_final_layer,
                          "X_train": X_train, "Y_train": Y_train,
                          "X_test": X_test, "Y_test": Y_test}

        return quantities, costs, parameters

    def plot_costs(self, costs):

        # plot the cost
        plt.plot(np.squeeze(costs))
        plt.ylabel('cost')
        plt.xlabel('iterations (per fives)')
        plt.title("Learning rate =" + str(self.learning_rate))

        plt.show()

    def correct_predictions(self, quantities):

        Y = quantities["Y"]
        Z_final_layer = quantities["Z_final_layer"]

        # Calculate the correct predictions
        correct_predictions = tf.equal(tf.argmax(Z_final_layer), tf.argmax(Y))

        return correct_predictions

    def train_accuracy(self, correct_predictions, quantities):

        X = quantities["X"]
        Y = quantities["Y"]
        X_train = quantities["X_train"]
        Y_train = quantities["Y_train"]

        # Calculate accuracy on the train set
        accuracy = tf.reduce_mean(tf.cast(correct_predictions, "float"))

        train_accuracy = accuracy.eval({X: X_train, Y: Y_train})

        return train_accuracy

    def test_accuracy(self, correct_predictions, quantities):

        X = quantities["X"]
        Y = quantities["Y"]
        X_test = quantities["X_test"]
        Y_test = quantities["Y_test"]

        # Calculate accuracy on the test set
        accuracy = tf.reduce_mean(tf.cast(correct_predictions, "float"))

        test_accuracy = accuracy.eval({X: X_test, Y: Y_test})

        return test_accuracy
