import tensorflow as tf

a = tf.random_normal([1])

sess = tf.Session()
sess.run( tf.global_variables_initializer() )

print( "a=", sess.run(a) )

#for i in range(5):
#    print( "a=", sess.run(a) )