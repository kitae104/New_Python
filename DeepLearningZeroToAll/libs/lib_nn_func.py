import tensorflow as tf

class Softmax_Classifer(tf.keras.Model):
    def __init__(self, nb_classes):

        super(Softmax_Classifer, self).__init__()
        self.W = tf.Variable(tf.random.normal((4, nb_classes)), name='weight')
        self.b = tf.Variable(tf.random.normal((nb_classes,)), name='bias')
        self.vars = [self.W, self.b]

    ############################################
    # Softmax 구하기
    ############################################
    def softmax_regression(self, X):
        return tf.nn.softmax(tf.matmul(X, self.W) + self.b)

    ############################################
    # 비용 계산
    ############################################
    def cost_fn(self, X, Y):
        logits = self.softmax_regression(X)  # x에 대한 가설값
        cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.math.log(logits), axis=1))  # 각 행에 대해 비용을 구한 후 함계 반환 -> 평균
        return cost

    ############################################
    # 기울기 계산
    ############################################
    def grad_fn(self, X, Y):
        with tf.GradientTape() as tape:
            cost = self.cost_fn(X, Y)
            grads = tape.gradient(cost, self.vars)
            return grads

    ############################################
    # 학습 수행
    ############################################
    def fit(self, X, Y, epochs=2000, verbose=100):
        optimizer =  tf.keras.optimizers.SGD(learning_rate=0.1)

        for i in range(epochs):
            grads = self.grad_fn(X, Y)
            optimizer.apply_gradients(zip(grads, self.vars))
            if (i==0) | ((i+1)%verbose==0):
                print('Loss at epoch %d: %f' %(i+1, self.cost_fn(X, Y).numpy()))
