.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


In the next subsections follow results in the following baselines:

 - `VGG16`_
 - `Resnet V1 trained by David Sandberg`_
 - `Idiap - Resnet V2 - MSCeleba`_
 - `Gaussian Mixture Models`_

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

Next sections presents the results and some discussions for each database.

Mobio
*****

Follow bellow the results for the mobio-male protocol only.

  +-----------+-------------+
  | ERR (dev) | HTER (eval) |
  +===========+=============+
  | 2.409%    | 2.624%      |
  +-----------+-------------+
  

To trigger this experiment run the following command::

 $ ./bob/bio/face-ongoing/configs/mobio--vgg16.sh
 
  

IJB-A
*****

This section presents the results for verification and search protocols.
Check `here <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijba/stable/index.html>`_ for more details.


Verification protocols
----------------------

Follow bellow the results using CMC (Cumulative Matching Curve) and TPIR (True Positive Identification Rate)
under different values of FAR (False Alarm Rate).

  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |    CMC% (R=1)   | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)| split                    |
  +=================+=================+=================+=================+==========================+
  |96.062           |87.965           |57.515           |25.069           |split 0                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |96.753           |88.42            |63.294           |36.706           |split 1                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |95.778           |88.444           |52.962           |30.197           |split 2                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |97.83            |88.815           |63.328           |37.117           |split 3                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |95.838           |87.685           |56.67            |33.238           |split 4                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |95.449           |88.35            |54.248           |27.427           |split 5                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |96.429           |89.709           |58.656           |35.109           |split 6                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |95.891           |89.541           |63.34            |34.578           |split 7                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |95.635           |85.449           |56.067           |30.955           |split 8                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |96.062           |87.965           |57.515           |25.069           |split 9                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+


The following command line triggers the sequence of verification experiments::

 $ ./bob/bio/face-ongoing/configs/ijba--vgg16--compare.sh



Search protocols
----------------

Follow bellow the results using DIR (Detection Identification Rate) under different values of FAR (False Alarm Rate).

  +-----------------+-----------------+-----------------+--------------------------+
  | DIR% (FAR=0.1)  | DIR% (FAR=0.01) | DIR% (FAR=0.001)| split                    |
  +=================+=================+=================+==========================+
  |34.585           |11.102           |0.0              |split 0                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |38.87            |19.601           |0.0              |split 1                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |35.162           |13.882           |0.0              |split 2                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |39.431           |20.813           |0.0              |split 3                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |37.744           |14.758           |0.0              |split 4                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |45.951           |22.411           |0.0              |split 5                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |40.809           |15.993           |0.0              |split 6                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |43.696           |27.721           |0.0              |split 7                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |38.691           |19.967           |0.0              |split 8                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |34.585           |11.102           |0.0              |split 9                   |
  +-----------------+-----------------+-----------------+--------------------------+

The following command line triggers the sequence of verification experiments::

 $ ./bob/bio/face-ongoing/configs/ijba--vgg16--search.sh




IJB-B
*****

To be done.


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

Follow bellow the results for the mobio-male protocol only.


  +-----------+-------------+
  | ERR (dev) | HTER (eval) |
  +===========+=============+
  | 0.521%    | 0.293%      |
  +-----------+-------------+

The following command line triggers the verification using mobio-male protocol::

 $ ./bob/bio/face-ongoing/configs/mobio--facenet_msceleba_inception_v1.sh


IJB-A
*****

This section presents the results for verification and search protocols.
Check `here <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijba/stable/index.html>`_ for more details.


Verification protocols
----------------------

Follow bellow the results using CMC (Cumulative Matching Curve) and TPIR (True Positive Identification Rate)
under different values of FAR (False Alarm Rate).

  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |    CMC% (R=1)   | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)| split                    |
  +=================+=================+=================+=================+==========================+
  |94.565           |92.069           |66.223           |39.046           |split 0                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |93.897           |93.086           |69.252           |48.904           |split 1                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |93.985           |92.683           |67.712           |34.088           |split 2                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |95.938           |93.6             |74.457           |47.301           |split 3                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |94.47            |91.277           |64.31            |34.322           |split 4                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |94.053           |93.083           |64.138           |36.286           |split 5                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |94.431           |94.855           |69.613           |48.91            |split 6                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |93.863           |91.409           |68.196           |32.497           |split 7                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |94.572           |91.798           |69.27            |48.539           |split 8                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |94.565           |92.069           |66.223           |39.046           |split 9                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+


The following command line triggers the sequence of verification experiments::

 $ ./bob/bio/face-ongoing/configs/ijba--facenet_msceleba_inception_v1--compare.sh


Search protocols
----------------

Follow bellow the results using DIR (Detection Identification Rate) under different values of FAR (False Alarm Rate).


  +-----------------+-----------------+-----------------+--------------------------+
  | DIR% (FAR=0.1)  | DIR% (FAR=0.01) | DIR% (FAR=0.001)| split                    |
  +=================+=================+=================+==========================+
  |51.118           |28.355           |0.0              |split 0                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |52.741           |31.146           |0.0              |split 1                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |53.865           |28.595           |0.0              |split 2                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |49.431           |27.642           |0.0              |split 3                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |43.342           |14.758           |0.0              |split 4                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |56.591           |31.544           |0.0              |split 5                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |46.507           |26.93            |0.0              |split 6                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |51.214           |26.233           |0.0              |split 7                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |51.118           |30.075           |0.0              |split 8                   |
  +-----------------+-----------------+-----------------+--------------------------+
  |51.118           |28.355           |0.0              |split 9                   |
  +-----------------+-----------------+-----------------+--------------------------+

The following command line triggers the sequence of verification experiments::

 $ ./bob/bio/face-ongoing/configs/ijba--facenet_msceleba_inception_v1--search.sh



IJB-B
*****

To be done.


Idiap - Resnet V2 - MSCeleba
============================

Inspired by `**FaceNet** <https://github.com/davidsandberg/facenet>`_ we here at Idiap trained our own CNN using the Inception Resnet 2 architecture using MSCeleba database.
In this `link <https://gitlab.idiap.ch/bob/bob.bio.htface/blob/277781d9c99738ff141218e1ce04103f9a427b0c/bob/bio/htface/config/tensorflow/MSCELEBA_inception_resnet_v2_center_loss.py>`_ you can find the script that trains this neural network.

To trigger this training it's necessary to use the `bob.learn.tensorflow <http://gitlab.idiap.ch/bob/bob.learn.tensorflow/>`_ package and run the following command::

  $ ./bin/jman submit --name CELEB-GRAY --queue gpu -- bob_tf_train_generic MSCELEBA_inception_resnet_v2_center_loss_GRAY.py
  

Some quick details about this CNN (just as a mental note):

  - The hot encoded layer has 99879 neurons.
  - MSCeleba has a lot of mislabeling, a very simple prunning was implemented `in this python package <http://gitlab.idiap.ch/tiago.pereira/bob.db.msceleb>`_.
  - Faces were detected and croped to :math:`182 \times 182` using `MTCNN <https://gitlab.idiap.ch/bob/bob.ip.mtcnn>`_ face and landmark detector
  - The following data augmentation strategies were implemented:
     * Random crop to :math:`160 \times 160`
     * Random Flip
     * Images were normalized to have zero mean and standard deviation one
  - Learning rate of 0.01
  - Adagrad as Optimizer
  - Batch size of 16


Two versions of it were trained: one providing color images for training and another one providing  gray scale images.



Mobio
*****

Follow bellow the results for the mobio-male protocol only.

  +------------+-----------+-------------+
  |            | ERR (dev) | HTER (eval) |
  +============+===========+=============+
  | color      | 7.327%    | 5.639%      |
  +------------+-----------+-------------+  
  | gray-scale | 7.564%    | 7.450%      |
  +------------+-----------+-------------+

The following command line triggers the verification using mobio-male protocol::

 $ ./bob/bio/face-ongoing/configs/mobio--idiap_msceleba_inception_v2.sh
 $ ./bob/bio/face-ongoing/configs/mobio--idiap_msceleba_inception_v2_GRAY.sh 



IJB-A
*****

This section presents the results for verification and search protocols.
Check `here <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijba/stable/index.html>`_ for more details.


Verification protocols
----------------------

Follow bellow the results using CMC (Cumulative Matching Curve) and TPIR (True Positive Identification Rate)
under different values of FAR (False Alarm Rate) using the **COLORED** network.

  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |    CMC% (R=1)   | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)| split                    |
  +=================+=================+=================+=================+==========================+
  |84.581           |69.606           |19.079           |4.493            |split 0                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.027           |65.374           |21.417           |4.553            |split 1                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |83.227           |69.861           |20.035           |4.239            |split 2                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |87.201           |73.289           |28.993           |7.012            |split 3                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |85.063           |73.204           |23.204           |4.048            |split 4                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.342           |68.265           |18.568           |3.701            |split 5                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.685           |71.429           |26.513           |7.688            |split 6                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |80.309           |62.38            |14.354           |2.775            |split 7                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |83.884           |67.416           |20.843           |5.449            |split 8                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.581           |69.606           |19.079           |4.493            |split 9                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+

  
Now the same table using the **GRAY** scaled network.
  
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |    CMC% (R=1)   | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)| split                    |
  +=================+=================+=================+=================+==========================+
  |84.581           |67.499           |18.58            |4.992            |split 0                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |81.355           |67.004           |20.63            |3.822            |split 1                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |80.74            |66.028           |20.267           |1.742            |split 2                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |85.977           |72.51            |23.929           |6.956            |split 3                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |86.887           |68.586           |21.437           |3.706            |split 4                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.464           |67.536           |17.597           |3.459            |split 5                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.806           |74.334           |23.245           |4.298            |split 6                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |81.003           |60.832           |14.728           |2.134            |split 7                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |83.324           |66.18            |18.371           |2.809            |split 8                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.581           |67.499           |18.58            |4.992            |split 9                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+

 $ ./bob/bio/face-ongoing/configs/ijba--idiap_msceleba_inception_v2--compare.sh
 $ ./bob/bio/face-ongoing/configs/ijba--idiap_msceleba_inception_v2_GRAY--compare.sh



Search protocols
----------------

To be done.


Intersession Variability Modelling
==================================

To be done.

Gaussian Mixture Models
=======================
  
To be written.
