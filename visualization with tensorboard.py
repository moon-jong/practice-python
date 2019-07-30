import tensorflow as tf

W = tf.Variable(tf.random_normal(shape=[1]), name='W')
b = tf.Variable(tf.random_normal(shape=[1]), name='b')
x = tf.placeholder(tf.float32, name= 'x')
linear_model = W*x + b

y = tf.placeholder(tf.float32,name= 'y')

loss = tf.reduce_mean(tf.square(linear_model - y))
tf.summary.scalar('loss', loss)

optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

x_train = [1, 2, 3, 4]
y_train = [2, 4, 6, 8]

sess= tf.Session()
sess.run(tf.global_variables_initializer())

merged = tf.summary.merge_all()
tensor_board_Writer = tf.summary.FileWriter('./ tensorboard/sample_1', sess.graph)

for i in range(1000):
    sess.run(optimizer,feed_dict= {x: x_train, y: y_train})
    summary = sess.run(merged, feed_dict= {x: x_train, y: y_train})
    tensor_board_Writer.add_summary(summary,i)