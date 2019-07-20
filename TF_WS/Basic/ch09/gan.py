# Generative Adversarial Network(GAN)을 구현해봅니다.
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

#=================================
# 옵션 설정 - 하이퍼 파라미터
#=================================
total_epoch = 100
batch_size = 100
learning_rate = 0.0002

# 신경망 레이어 구성 옵션
n_hidden = 256
n_input = 28 * 28
n_noise = 128               # 생성기의 입력값으로 사용할 노이즈의 크기

#=================================
# 신경망 모델 구성
#=================================
# GAN 도 Unsupervised 학습이므로 Autoencoder 처럼 Y를 사용하지 않습니다.
X = tf.compat.v1.placeholder(tf.float32, [None, n_input])

# 가짜 이미지 생성을 위해 노이즈 Z를 입력값으로 사용합니다.
Z = tf.compat.v1.placeholder(tf.float32, [None, n_noise])

# 생성기 신경망에 사용하는 변수들입니다.
# 첫번째 가중치와 편향은 은닉층으로 출력하기 위한 변수들
G_W1 = tf.Variable(tf.random.normal([n_noise, n_hidden], stddev=0.01))
G_b1 = tf.Variable(tf.zeros([n_hidden]))

# 두번째 가중치와 편향은 출력층에 사용할 변수들
# 따라서 두번째 가중치의 변수 크기는 실제 이미지 크기와 같아야 함 28 X 28  ==> 784
G_W2 = tf.Variable(tf.random.normal([n_hidden, n_input], stddev=0.01))
G_b2 = tf.Variable(tf.zeros([n_input]))

# 판별기 신경망에 사용하는 변수들입니다.
D_W1 = tf.Variable(tf.random.normal([n_input, n_hidden], stddev=0.01))
D_b1 = tf.Variable(tf.zeros([n_hidden]))

# 판별기의 최종 결과값은 얼마나 진짜와 가깝냐를 판단하는 한 개의 스칼라값입니다.
D_W2 = tf.Variable(tf.random.normal([n_hidden, 1], stddev=0.01))
D_b2 = tf.Variable(tf.zeros([1]))

#==================================
# 생성자(G) 신경망을 구성합니다.
#==================================
# 생성자는 무작위로 생성한 노이즈를 받아 가중치와 편향을 반영하여 은닉층을 만들고,
# 은닉층에서는 실제 이미지와 같은 크기의 결과 값을 출력
def generator(noise_z):
    hidden = tf.nn.relu(tf.matmul(noise_z, G_W1) + G_b1)
    output = tf.nn.sigmoid(tf.matmul(hidden, G_W2) + G_b2)

    return output

#==================================
# 구분자(D) 신경망을 구성합니다.
#==================================
# 0~1 사이의 스칼라값 하나를 출력하도록 하였으며, 이를 위한 활성화함수로
# sigmoid 함수 사용
def discriminator(inputs):
    hidden = tf.nn.relu(tf.matmul(inputs, D_W1) + D_b1)
    output = tf.nn.sigmoid(tf.matmul(hidden, D_W2) + D_b2)

    return output

#==================================
# 랜덤한 노이즈(Z)를 만듭니다.
#==================================
def get_noise(batch_size, n_noise):
    return np.random.normal(size=(batch_size, n_noise))

#===========================================================================
# 노이즈 Z를 이용하여 가짜 이미지를 만들 생성자 G를 만들고, 이 G가 만든 가짜 이미지와
# 진짜 이미지 X를 각각 구분자에 넣어 입력한 이미지가 진짜인지를 판별하도록 한다.
#===========================================================================
# 노이즈를 이용해 랜덤한 이미지를 생성합니다.
G = generator(Z)

# 노이즈를 이용해 생성한 이미지가 진짜 이미지인지 판별한 값을 구합니다.
D_gene = discriminator(G)

# 진짜 이미지를 이용해 판별한 값을 구합니다.
D_real = discriminator(X)

#=========================================================================================
# 논문에 따르면, GAN 모델의 최적화는 loss_G 와 loss_D 를 최대화 하는 것 입니다.
# 다만 loss_D와 loss_G는 서로 연관관계가 있기 때문에 두 개의 손실값이 항상 같이 증가하는 경향을 보이지는
# 않을 것 입니다. loss_D가 증가하려면 loss_G는 하락해야하고, loss_G가 증가하려면 loss_D는 하락해야하는
# 경쟁관계에 있기 때문입니다.
#=========================================================================================
# 손실값 구하기
# 생성자가 만든 이미지를 구분자가 가짜라고 판단하도록 하는 손실값(경찰 학습용)
# loss_D 를 최대화하기 위해서는 D_gene 값을 최소화하게 됩니다.
# 판별기에 진짜 이미지를 넣었을 때에도 최대값을 : tf.log(D_real)
# 가짜 이미지를 넣었을 때에도 최대값을 : tf.log(1 - D_gene) 갖도록 학습시키기 때문입니다.
# 이것은 판별기는 생성기가 만들어낸 이미지가 가짜라고 판단하도록 판별기 신경망을 학습시킵니다.
loss_D = tf.reduce_mean(tf.math.log(D_real) + tf.math.log(1-D_gene))

# 진짜라고 판단하도록 하는 손실값(위조지폐범 학습용)
# 반면 loss_G 를 최대화하기 위해서는 D_gene 값을 최대화하게 되는데,
# 이것은 가짜 이미지를 넣었을 때, 판별기가 최대한 실제 이미지라고 판단하도록 생성기 신경망을 학습시킵니다.
# 논문에서는 loss_D 와 같은 수식으로 최소화 하는 생성기를 찾지만, 결국 D_gene 값을 최대화하는 것이므로
# 다음과 같이 사용할 수 있습니다.
loss_G = tf.reduce_mean(tf.math.log(D_gene))

#===========================================
# 손실값들을 이용해 학습 시키기
#===========================================
# loss_D 를 구할 때는 판별기 신경망에 사용되는 변수만 사용하고 --> 생성자가 변하지 않음,
# loss_G 를 구할 때는 생성기 신경망에 사용되는 변수만 사용하여 최적화를 합니다. --> 구분자가 변하지 않음
D_var_list = [D_W1, D_b1, D_W2, D_b2]
G_var_list = [G_W1, G_b1, G_W2, G_b2]

#===========================================
# 최적화
#===========================================
# GAN 논문의 수식에 따르면 loss 를 극대화 해야하지만, minimize 하는 최적화 함수를 사용하기 때문에
# 최적화 하려는 loss_D 와 loss_G 에 음수 부호를 붙여줍니다.
train_D = tf.compat.v1.train.AdamOptimizer(learning_rate).minimize(-loss_D, var_list=D_var_list)
train_G = tf.compat.v1.train.AdamOptimizer(learning_rate).minimize(-loss_G, var_list=G_var_list)

#==================================
# 신경망 모델 학습
#==================================
# 텐서플로의 세션을 초기화
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

total_batch = int(mnist.train.num_examples/batch_size)
print('total_batch :',total_batch)      # 550

# 결괏값을 받을 수 있는 변수 선언
loss_val_D, loss_val_G = 0, 0

for epoch in range(total_epoch):
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        noise = get_noise(batch_size, n_noise)

        # 판별기와 생성기 신경망을 각각 학습시킨다.
        _, loss_val_D = sess.run([train_D, loss_D], feed_dict={X:batch_xs, Z:noise})
        _, loss_val_G = sess.run([train_G, loss_G], feed_dict={Z:noise})

        print('Epoch:', '%04d' % epoch, 'D loss: {:.4}'.format(loss_val_D), 'G loss: {:.4}'.format(loss_val_G))

        #=============================================================
        # 학습이 되어가는 모습을 보기 위해 주기적으로 이미지를 생성하여 저장
        #=============================================================
        if epoch == 0 or (epoch + 1) % 10 == 0:
            sample_size = 10
            noise = get_noise(sample_size, n_noise)
            samples = sess.run(G, feed_dict={Z: noise})

            fig, ax = plt.subplots(1, sample_size, figsize=(sample_size, 1))

            for i in range(sample_size):
                ax[i].set_axis_off()
                ax[i].imshow(np.reshape(samples[i], (28, 28)))

            plt.savefig('samples/{}.png'.format(str(epoch).zfill(3)), bbox_inches='tight')
            plt.close(fig)

print('최적화 완료')