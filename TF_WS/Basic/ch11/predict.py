import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

tf.app.flags.DEFINE_string("output_graph", "./workspace/flowers_graph.pb", "학습된 신경망이 저장된 위치")
tf.app.flags.DEFINE_string("output_labels", "./workspace/flowers_labels.txt", "학습할 레이블 데이터 파일")
tf.app.flags.DEFINE_boolean("show_image", True, "이미지 추론 후 이미지를 보여줍니다.")

FLAGS = tf.app.flags.FLAGS

def main(_):
    labels = [line.rstrip() for line in tf.io.gfile.GFile(FLAGS.output_labels)]
    print(labels)   # 꽃 이름 ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

    # 프로토콜 버퍼 형식(.pb)의 파일 읽어 신경망 그래프 작성하기
    with tf.gfile.FastGFile(FLAGS.output_graph, 'rb') as fp:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(fp.read())
        tf.import_graph_def(graph_def, name='')

    with tf.compat.v1.Session() as sess:
        #신경망 모델에서 예측에 사용할 텐서 지정
        logits = sess.graph.get_tensor_by_name('final_result:0')   # 최종 출력층의 텐서 이름

        # 에측 스크립트를 실행할 때 주어진 이름의 이미지 파일을 읽어들인 뒤, 그 이미지를
        # 예측 모델에 넣어 예측을 실행함
        image = tf.gfile.FastGFile(sys.argv[1], 'rb').read()
        prediction = sess.run(logits, {'DecodeJpeg/contents:0': image})

    print('=== 예측 결과 ===')
    for i in range(len(labels)):
        name = labels[i]
        score = prediction[0][i]
        print('%s (%.2f%%)' % (name, score * 100))

    if FLAGS.show_image:
        img = mpimg.imread(sys.argv[1])
        plt.imshow(img)
        plt.show()


if __name__ == "__main__":
    tf.compat.v1.app.run()
