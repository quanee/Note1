import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

'''
Softmax Regression识别手写数字
训练数据特征: 55000x784(28x28)的Tensor
训练数据Label: 55000x10

'''


mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

# 训练集(55000)
print(mnist.train.images.shape, mnist.train.labels.shape)
# 测试集(10000)
print(mnist.test.images.shape, mnist.test.labels.shape)
# 验证集(5000)
print(mnist.validation.images.shape, mnist.validation.labels.shape)


# 创建并注册默认session
sess = tf.InteractiveSession()
# 输入
x = tf.placeholder(tf.float32, [None, 784])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
# y=softmax(Wx+b)
y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

tf.global_variables_initializer().run()

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    train_step.run({x: batch_xs, y_: batch_ys})


correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))