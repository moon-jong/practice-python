import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('/tmp/data/',one_hot=True)

learning_rate = 0.001
num_epoch = 30
batch_size = 256
display_size = 1
input_size = 784
hidden_size1 = 256
hidden_size2 = 256
output_size = 10

x = tf.placeholder(tf.float32,shape=[None,input_size])
y = tf.placeholder(tf.float32,shape=[None,output_size])

def build_ANN(x):
    W1 = tf.Variable(tf.random_normal(shape=[input_size, hidden_size1]))
    b1 = tf.Variable(tf.random_normal(shape=[hidden_size1]))
    H1_output = tf.nn.relu(tf.matmul(x,W1)+b1)
    W2 = tf.Variable(tf.random_normal(shape=[hidden_size1, hidden_size2]))
    b2 = tf.Variable(tf.random_normal(shape=[hidden_size2]))
    H2_output = tf.nn.relu(tf.matmul(H1_output,W2)+b2)
    W_output = tf.Variable(tf.random_normal(shape=[hidden_size2, output_size]))
    b_output = tf.Variable(tf.random_normal(shape=[output_size]))
    logits = tf.matmul(H2_output, W_output) + b_output

    return logits

predicted_value = build_ANN(x)

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predicted_value,labels= y))
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(num_epoch):
        average_loss = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        for i in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            _, current_loss = sess.run([train_step, loss],feed_dict={x: batch_x, y:batch_y})
            average_loss += current_loss/total_batch
        if epoch % display_size ==0:
            print('반복(Epoch):%d, 손실함수(loss):%f' % ((epoch+1),average_loss))

    correct_prediction = tf.equal(tf.argmax(predicted_value,1),tf.argmax(y,1))
    acc = tf.reduce_mean(tf.cast(correct_prediction,"float"))
    print("정확도:%f"%(acc.eval(feed_dict={x:mnist.test.images,y: mnist.test.labels})))


