import tensorflow as tf

# building the graph
msg = tf.constant('hi')
num = tf.constant(10.9)
num2 = tf.constant(11.1)

# invokes session's run method to run graph and evaluate val
sess = tf.Session()
print(sess.run([msg, num, num2]))

# add is also a node
nodeSum = tf.add(num, num2)  # optional name as 3rd arg
print(nodeSum)
print(sess.run(nodeSum))

# tensor provide a utility called tensorBoard that display teh graph
# a graph can be parametrized to accept external input (placeHolders)
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)

print(sess.run(adder_node, {a: 3, b: 4.5}))
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))

# more complex using existing adder_node * 3
add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b: 4.5}))

# variables allow us to add trainable parameters to a graph.
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
# variables are not initialized right away unlike constants, call following
init = tf.global_variables_initializer()  # handle to tf sub-graph
sess.run(init)

print(sess.run(linear_model, {x: [1, 2, 3, 4]}))
# create a y  placeholder to provide desired values, and a loss function
# linear_model - y creates a vector where each element is the corresponding
y = tf.placeholder(tf.float32)  # label
squared_deltas = tf.square(linear_model - y)  # node operation square the error
loss = tf.reduce_sum(squared_deltas)  # add all error up into a scalar number
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))  # produce loss value

# variables can be changed using tf.assign( var Name , new val)
fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

# lets use tf.train API to automatically find the right parameter (optimizers)
# gradient descent is the simpliest optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)  # minimize the loss value

sess.run(init)  # reset values to incorrect defaults.
for i in range(1000):  # maybe iteration number
    sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})

print(sess.run([W, b]))

############################################################
import numpy as np
import tensorflow as tf

# Model parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)
# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
# training data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong
for i in range(1000):
  sess.run(train, {x:x_train, y:y_train})

# evaluate training accuracy
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x:x_train, y:y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))

