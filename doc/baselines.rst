.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

=========
Baselines
=========



VGG16
=====

The VGG-Face network model is made publicly available by the `Visual Geometry Group <www.robots.ox.ac.uk/~vgg/software/vgg_face>`_ at Oxford University.
Involving almost 135 million trainable parameters, this network has been shown to achieve a FR accuracy of 98.95\% on the LFW unrestricted.
VGG-Face is a CNN consisting of 16 hidden layers.
The initial 13 hidden layers are convolution and pooling layers, and the last three layers are fully-connected ('fc6', 'fc7', and 'fc8').
The input to this network is an appropriately cropped color face-image of pre-specified dimensions.

We use the representation produced by the 'fc7' layer of the VGG-Face CNN as a template for the input image.
When enrolling a client, the template produced by the VGG-Face network for each enrollment-sample is recorded.
For scoring, the network is used to generate a template for the probe face-image, which is then compared to the enrolled templates of the claimed identity using the Cosine-similarity measure.


Mobio
*****

  +-----------+-------------+
  | ERR (dev) | HTER (eval) |
  +===========+=============+
  | 2.409%    | 2.624%      |
  +-----------+-------------+


IJB-A
*****

Check `here <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijba/stable/index.html>`_ for protocol details.


Verification protocols
----------------------

The following command line triggers the sequence of verification experiments::

 $ ./bob/bio/face-ongoing/compare_vgg16.sh

Follow bellow the Rank-1 for each one of the 10 splits:


  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | CMC(R=1)  | FRR (FAR=0.1) | FRR (FAR=0.01) | FRR (FAR=0.001) | directory                                |
  +===========+===============+================+=================+==========================================+
  | 96.062%   | 12.035%       | 42.485%        | 74.931%         | ./vgg16/compare/split1/compare_split1    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 96.753%   | 11.580%       | 36.706%        | 63.294%         | ./vgg16/compare/split2/compare_split2    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 95.778%   | 11.556%       | 47.038%        | 69.803%         | ./vgg16/compare/split3/compare_split3    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 97.830%   | 11.185%       | 36.672%        | 62.883%         | ./vgg16/compare/split4/compare_split4    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 95.838%   | 12.315%       | 43.330%        | 66.762%         | ./vgg16/compare/split5/compare_split5    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 95.449%   | 11.650%       | 45.752%        | 72.573%         | ./vgg16/compare/split6/compare_split6    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 96.429%   | 10.291%       | 41.344%        | 64.891%         | ./vgg16/compare/split7/compare_split7    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 95.891%   | 10.459%       | 36.660%        | 65.422%         | ./vgg16/compare/split8/compare_split8    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 95.635%   | 14.551%       | 43.933%        | 69.045%         | ./vgg16/compare/split9/compare_split9    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 96.062%   | 12.035%       | 42.485%        | 74.931%         | ./vgg16/compare/split10/compare_split10  |
  +-----------+---------------+----------------+-----------------+------------------------------------------+


Search protocols
----------------




IJB-B
*****



Resnet V1 trained by David Sandberg
===================================

Very recently, David Sandberg has made publicly available his implementation as well as trained models for a new FR-CNN named `**FaceNet** <https://github.com/davidsandberg/facenet>`_.
This is the closest open-source implementation of the FaceNet CNN proposed by [Schroff_2015]_, for which neither a pre-trained model nor the training-set is publicly available.
Sandberg's FaceNet implements an Inception-ResNet V1 DNN architecture [Szegedy2017]_.
In these tests, we have used the 20170512-110547 model, trained on the MS-Celeb-1M dataset.
Using this model, FaceNet achieves a FR performance of 99.2\% on the LFW dataset.
We use this representation to construct enrollment and probe templates, which are compared to each other using the Cosine measure.



Mobio
*****

The following command line triggers the verification mobio-male protocol::

 $ ./bob/bio/face-ongoing/configs/mobio--facenet_msceleba_inception_v1.sh

Follow bellow the results in the dev and in the eval set.

  +-----------+-------------+
  | ERR (dev) | HTER (eval) |
  +===========+=============+
  | 0.521%    | 0.293%      |
  +-----------+-------------+


IJB-A
*****

Check `here <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijba/stable/index.html>`_ for protocol details.


Verification protocols
----------------------

The following command line triggers the sequence of verification experiments::

 $ ./bob/bio/face-ongoing/compare_facenet.sh

Follow bellow the Rank-1 for each one of the 10 splits:


  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | CMC(R=1)  | FRR (FAR=0.1) | FRR (FAR=0.01) | FRR (FAR=0.001) | directory                                |
  +===========+===============+================+=================+==========================================+
  | 94.565%   | 7.931%        | 33.777%        | 60.954%         | ./vgg16/compare/split1/compare_split1    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 93.897%   | 6.914%        | 30.748%        | 51.096%         | ./vgg16/compare/split2/compare_split2    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 93.985%   | 7.317%        | 32.288%        | 65.912%         | ./vgg16/compare/split3/compare_split3    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 95.938%   | 6.400%        | 25.543%        | 52.699%         | ./vgg16/compare/split4/compare_split4    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 94.470%   | 8.723%        | 35.690%        | 65.678%         | ./vgg16/compare/split5/compare_split5    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 94.053%   | 6.917%        | 35.862%        | 63.714%         | ./vgg16/compare/split6/compare_split6    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 94.431%   | 5.145%        | 30.387%        | 51.090%         | ./vgg16/compare/split7/compare_split7    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 93.863%   | 8.591%        | 31.804%        | 67.503%         | ./vgg16/compare/split8/compare_split8    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 94.572%   | 8.202%        | 30.730%        | 51.461%         | ./vgg16/compare/split9/compare_split9    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 94.565%   | 7.931%        | 33.777%        | 60.954%         | ./vgg16/compare/split10/compare_split10  |
  +-----------+---------------+----------------+-----------------+------------------------------------------+


Search protocols
----------------




IJB-B
*****




Idiap - Resnet V2 - MSCeleba
============================

Inspired by `**FaceNet** <https://github.com/davidsandberg/facenet>` we here at Idiap trained our own CNN using the Inception Resnet 2 architecture using MSCeleba database.
In this `link <https://gitlab.idiap.ch/bob/bob.bio.htface/blob/277781d9c99738ff141218e1ce04103f9a427b0c/bob/bio/htface/config/tensorflow/MSCELEBA_inception_resnet_v2_center_loss.py>` you can find the script that trains this neural network.

To trigger this training it's necessary to use the `bob.learn.tensorflow <http://gitlab.idiap.ch/bob/bob.learn.tensorflow/>` package and run the following command::

  $ ./bin/jman submit --name CELEB-GRAY --queue gpu -- bob_tf_train_generic MSCELEBA_inception_resnet_v2_center_loss_GRAY.py
  

Some quick details about this CNN (just as a mental note):

  - The hot encoded layer has 99879 neurons.
  - MSCeleba has a lot of mislabeling, a very simple prunning was implemented `here <http://gitlab.idiap.ch/tiago.pereira/bob.db.msceleb>`.
  - Faces were detected and croped to :math:`182 x 182` using `MTCNN <https://gitlab.idiap.ch/bob/bob.ip.mtcnn>` face and landmark detector
  - The following data augmentation strategies were implemented:
     * Random crop to :math:`160 x 160`
     * Random Flip
     * Images were normalized to have zero mean and standard deviation one
  - Learning rate of 0.01
  - Adagrad as Optimizer
  - Batch size of 16


Two versions of it were trained: one providing color images for training and another one providing  gray scale images.



Mobio
*****

The following command line triggers the verification mobio-male protocol::

 $ ./bob/bio/face-ongoing/configs/mobio--idiap_msceleba_inception_v2.sh

Follow bellow the results in the dev and in the eval set.

  +------------+-----------+-------------+
  |            | ERR (dev) | HTER (eval) |
  +============+===========+=============+
  | color      | 7.327%    | 5.639%      |
  +------------+-----------+-------------+  
  | gray-scale | 7.564%    | 7.450%      |
  +------------+-----------+-------------+


IJB-A
*****

Check `here <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijba/stable/index.html>` for protocol details.


Verification protocols
----------------------

The following command line triggers the sequence of verification experiments::

 $ ./bob/bio/face-ongoing/compare_facenet.sh

Follow bellow the Rank-1 for each one of the 10 splits for the **COLOR** CNN (** ~ 3 epochs so far**):

  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | CMC(R=1)  | FRR (FAR=0.1) | FRR (FAR=0.01) | FRR (FAR=0.001) | directory                                |
  +===========+===============+================+=================+==========================================+
  | 84.581%   | 30.394%       | 80.921%        | 0000000         | ./vgg16/compare/split1/compare_split1    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 82.027%   | 34.626%       | 78.583%        | 0000000         | ./vgg16/compare/split2/compare_split2    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 83.227%   | 30.139%       | 79.965%        | 0000000         | ./vgg16/compare/split3/compare_split3    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 87.201%   | 26.711%       | 71.007%        | 0000000         | ./vgg16/compare/split4/compare_split4    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 85.063%   | 26.796%       | 76.796%        | 0000000         | ./vgg16/compare/split5/compare_split5    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 82.342%   | 31.735%       | 81.432%        | 0000000         | ./vgg16/compare/split6/compare_split6    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 84.685%   | 28.571%       | 73.487%        | 0000000         | ./vgg16/compare/split7/compare_split7    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 80.309%   | 37.620%       | 85.646%        | 0000000         | ./vgg16/compare/split8/compare_split8    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 83.884%   | 32.584%       | 79.157%        | 0000000         | ./vgg16/compare/split9/compare_split9    |
  +-----------+---------------+----------------+-----------------+------------------------------------------+
  | 84.581%   | 30.394%       | 80.921%        | 0000000         | ./vgg16/compare/split10/compare_split10  |
  +-----------+---------------+----------------+-----------------+------------------------------------------+


Search protocols
----------------



Intersession Variability Modelling
==================================
  
  





