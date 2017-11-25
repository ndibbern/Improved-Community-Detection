#sys.path.append('C:/Users/juanj/Projects/LMU-RSCH-Fall17/Code/Python/my_packages')
import os
import sys
import numpy as np
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from my_packages.clusters.save_cluster import import_example
from my_packages.clusters.plot_cluster import plot_G
from my_packages.clusters.nx_np import nx_np

'''
# Description
This file showcases some useful operations that will be used for the algorithm
Can be thought of as a galery of tensorflow nodes

# On how to structure the project
https://www.tensorflow.org/versions/r0.12/get_started/basic_usage
'''

# CONSTRUCTION PHASE
## assemble the graph

# Constant Nodes
one = tf.constant(1.)
R = tf.constant(2)
n = tf.constant(20)
alph = tf.constant(0.1)

### source nodes (do not need any input i.e. Constant)
#R = tf.placeholder(tf.int32, name='n_clusters')
W = tf.placeholder(tf.float32, name='W') # The input adj matrix with 0s and 1s
F_i = tf.placeholder(tf.int32, name='initial_parition')
f = tf.placeholder(tf.float32, shape=[20, 1], name='cluster')

clas_i = tf.placeholder(tf.int32, name='target_clas') # value in [0, R-1]
node_i = tf.placeholder(tf.int32, name='node_index') # value in [0, n-1]

### Operation nodes
#n = tf.shape(W)[0]
D = tf.diag(tf.reduce_sum(W, 0), name='degree')
D_ = tf.diag((tf.pow(tf.diag_part(D), -0.5)))
I = tf.eye(n, name='identity')
Op = tf.matmul(D_, tf.matmul(W, D_), name='smooth_operator')
L = tf.subtract(I, Op, name='Laplacian')

### Function Nodes
difuse = tf.scalar_mul(alph, tf.matmul(Op, f)) + tf.scalar_mul((one - alph), f)

### Model nodes (to be trained)
F = tf.Variable(tf.fill([n, R], 0.), name='Partition')
# clas = tf.scatter_update(tf.Variable(tf.zeros([R])), [clas_i], one)
generic_clas = tf.Variable(tf.zeros([R]))
clas = tf.assign(generic_clas[clas_i] , one) # gives [0, 0, 1] with a 1 on clas_i
#clas = tf.concat([tf.zeros(clas_i), [one], tf.zeros(R-clas_i-1)], 0) # to which class clas_i
#change_clas = tf.scatter_update(F, [node_i], clas) #what node?, to which class?
# sess.run(F.initializer)
# update F = F.assign(F + 1.0)



# EXCECUTION PHASE

if __name__ == '__main__':
    G, coordinates, labels_true = import_example('small')
    W_i, R_i = nx_np(G)
    f_i = np.vstack([1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    print(f_i)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        #print(sess.run(L, feed_dict={W:W_i}))
        #print(sess.run(clas, feed_dict={clas_i: 1}))
        #print(sess.run(F))
        print(sess.run(difuse, feed_dict={W: W_i, f: f_i,}))
