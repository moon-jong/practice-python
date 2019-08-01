import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('/tmp/data/', one_hot=True)

learning_rate_RMSprob = 0.02
learning_rate_GradientDescent = 0.5
num_epochs = 100
batch_size = 256
display_step = 1
input_size = 784
hidden1_size = 128
hidden2_size = 64

x = tf.placeholder(tf.float32, shape=[None, input_size])
y = tf.placeholder(tf.float32, shape=[None, 10])

def building_autoencoder(x):
    Wh_1 = tf.Variable(tf.random_normal([input_size, hidden1_size]))
    bh_1 = tf.Variable(tf.random_normal([hidden1_size]))
    H1_output = tf.nn.sigmoid(tf.matmul(x, Wh_1) + bh_1)

    Wh_2 = tf.Variable(tf.random_normal([hidden1_size, hidden2_size]))
    bh_2 = tf.Variable(tf.random_normal([hidden2_size]))
    H2_output = tf.nn.sigmoid(tf.matmul(H1_output, Wh_2) + bh_2)

    Wh_3 = tf.Variable(tf.random_normal([hidden2_size, hidden1_size]))
    bh_3 = tf.Variable(tf.random_normal([hidden1_size]))
    H3_output = tf.nn.sigmoid(tf.matmul(H2_output, Wh_3) + bh_3)

    Wo = tf.Variable(tf.random_normal([hidden1_size, input_size]))
    bo = tf.Variable(tf.random_normal([input_size]))
    X_reconstructed = tf.nn.sigmoid(tf.matmul(H3_output, Wo) + bo)

    return X_reconstructed, H2_output

def softmax_classifier(x):
    W_sofmax= tf.Variable(tf.zeros([hidden2_size, 10]))
    b_softmax= tf.Variable(tf.zeros([10]))

    y_pred = tf.nn.softmax(tf.matmul(x, W_sofmax) + b_softmax)

    return y_pred

y_pred, extracted_features =building_autoencoder(x)

y_true = x

y_pred_softmax = softmax_classifier(extracted_features)

pretraing_loss = tf.reduce_mean(tf.pow(y_true - y_pred,2))
pretraing_train_step = tf.train.RMSPropOptimizer(learning_rate_RMSprob).minimize(pretraing_loss)

finetunnig_loss = tf.reduce_mean(-tf.reduce_sum(y* tf.log(y_pred_softmax), reduction_indices=[1]))
finetuning_train_step = tf.train.GradientDescentOptimizer(learning_rate_GradientDescent).minimize(finetunnig_loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    total_batch = int(mnist.train.num_examples/batch_size)

    for epoch in range(num_epochs):

         for i in range(total_batch):
             batch_xs, batch_ys = mnist.train.next_batch(batch_size)
             _, pretraing_loss_print = sess.run([pretraing_train_step, pretraing_loss], feed_dict={x: batch_xs})
         if epoch % display_step == 0:
             print('반복: %d, Pretraing 손실함수(pretraing_loss): %f' % ((epoch+1),pretraing_loss_print))
    print("Step1 : Mnist 데이터 재구축을 위한 오토인코더 최적화 완료(Pre_Training")

    for epoch in range(num_epochs + 100):

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            _, finetunig_loss_print = sess.run([finetuning_train_step,finetunnig_loss],
                                                feed_dict={x: batch_xs, y: batch_ys})
        if epoch % display_step == 0:
            print("반복(epoch):%d, Fine-Tuning 손실함수(finetuning_loss):%f" % ((epoch + 1), finetunig_loss_print))
    print("Step2: Mnist 데이터 분류를 위한 오토인코더 + Softmax 분류기 최적화 완료(Fine-Tuning)")


    corret_prediction= tf.equal(tf.argmax(y,1),tf.argmax(y_pred_softmax,1))
    accuracy = tf.reduce_mean(tf.cast(corret_prediction, tf.float32))

    print("정확도(오토인코더 + Softmax 분류기:%f" % sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))