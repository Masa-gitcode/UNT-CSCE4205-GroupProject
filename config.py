# Random seed using for 
# shuffling batches, initializing weightsm spliting
SEED = 50
# Number for cross validation folds
N_FOLD = 5
# C value for SVM
SVM_C_GRID = [0.1, 1, 10, 100]
# Ganma for RBF kernel's reach 
SVM_GAMMA_GRID = ["scale", 0.001, 0.01]
# Learning rate for gradient descent
SOFTMAX_LR = 0.1
# L2 regularization strength
SOFTMAX_L2 = 1e-5
# Mini-batch size for SGD
BATCH_SIZE = 150
# Number of full passes over the training data
EPOCHS = 50