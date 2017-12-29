from bob.learn.tensorflow.network import inception_resnet_v2
from bob.learn.tensorflow.estimators import Logits
from bob.learn.tensorflow.dataset.tfrecords import batch_data_and_labels_image_augmentation, shuffle_data_and_labels_image_augmentation
from bob.learn.tensorflow.utils.hooks import LoggerHookEstimator
from bob.learn.tensorflow.loss import mean_cross_entropy_loss
import os
import tensorflow as tf

learning_rate = 0.1
data_shape = (182, 182, 3)  # size of atnt images
output_shape = (160, 160)
data_type = tf.uint8
batch_size = 16
validation_batch_size = 250
epochs = 5
n_classes = 10575
embedding_validation = True
steps = 2000000

model_dir = "/idiap/temp/tpereira/casia_webface/new_tf_format/inception_resnet_v2_gray/crossentropy"
tf_record_path = "/idiap/project/hface/databases/tfrecords/casia_webface/182x/RGB"
tf_record_path_validation = "/idiap/project/hface/databases/tfrecords/lfw/182x/RGB"


# Creating the tf record
tfrecords_filename = [os.path.join(tf_record_path, f) for f in os.listdir(tf_record_path)]
tfrecords_filename_validation = [os.path.join(tf_record_path_validation, f) for f in os.listdir(tf_record_path_validation)]

def train_input_fn():
    return shuffle_data_and_labels_image_augmentation(tfrecords_filename, data_shape, data_type, batch_size, epochs=epochs,
                                                      output_shape=output_shape,
                                                      random_flip=True,
                                                      random_brightness=False,
                                                      random_contrast=False,
                                                      random_saturation=False,
                                                      per_image_normalization=True,
                                                      gray_scale=True)
        

def eval_input_fn():
    return batch_data_and_labels_image_augmentation(tfrecords_filename_validation, data_shape, data_type, validation_batch_size, epochs=1,
                                                    output_shape=output_shape,
                                                    random_flip=False,
                                                    random_brightness=False,
                                                    random_contrast=False,
                                                    random_saturation=False,
                                                    per_image_normalization=True,
                                                    gray_scale=True)


run_config = tf.estimator.RunConfig()
run_config = run_config.replace(save_checkpoints_steps=2000)

#                             
optimizer = tf.train.RMSPropOptimizer(learning_rate, decay=0.9, momentum=0.9, epsilon=1.0)
#tf.train.AdagradOptimizer(learning_rate)
estimator = Logits(model_dir=model_dir,
                             architecture=inception_resnet_v2,
                             optimizer=optimizer,
                             n_classes=n_classes,
                             embedding_validation=embedding_validation,
                             validation_batch_size=validation_batch_size,
                             loss_op=mean_cross_entropy_loss,
                             config=run_config)


hooks = [LoggerHookEstimator(estimator, 16, 300),
         tf.train.SummarySaverHook(save_steps=1000,
                                   output_dir=model_dir,
                                   scaffold=tf.train.Scaffold(),
                                   summary_writer=tf.summary.FileWriter(model_dir) )]

