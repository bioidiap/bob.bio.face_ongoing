.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


In the next subsections follow results in the following baselines:

 - `VGG16`_
 - `Resnet V1 trained by David Sandberg`_
 - `Idiap - Resnet V2 - MSCeleba`_
 - `Idiap - Resnet V2 - Casia Webface`_ 
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
|**50.7  (3.51 )**|**27.36 (4.51 )**|**0.0   (0.0  )**|mean(std)                 |
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
|84.748           |74.653           |21.298           |6.101            |split 0                   |
+-----------------+-----------------+-----------------+-----------------+--------------------------+
|81.579           |68.353           |19.899           |5.171            |split 1                   |
+-----------------+-----------------+-----------------+-----------------+--------------------------+
|83.112           |71.254           |18.641           |5.517            |split 2                   |
+-----------------+-----------------+-----------------+-----------------+--------------------------+
|87.59            |75.515           |28.77            |6.789            |split 3                   |
+-----------------+-----------------+-----------------+-----------------+--------------------------+
|85.519           |75.143           |25.941           |4.447            |split 4                   |
+-----------------+-----------------+-----------------+-----------------+--------------------------+
|82.767           |70.813           |21.117           |5.34             |split 5                   |
+-----------------+-----------------+-----------------+-----------------+--------------------------+
|83.656           |71.186           |23.063           |6.477            |split 6                   |
+-----------------+-----------------+-----------------+-----------------+--------------------------+
|81.43            |63.074           |14.141           |4.055            |split 7                   |
+-----------------+-----------------+-----------------+-----------------+--------------------------+
|82.429           |69.157           |18.82            |5.056            |split 8                   |
+-----------------+-----------------+-----------------+-----------------+--------------------------+
|84.748           |74.653           |21.298           |6.101            |split 9                   |
+-----------------+-----------------+-----------------+-----------------+--------------------------+
|**83.76 (1.82 )**|**71.38 (3.69 )**|**21.3  (3.83 )**|**5.51  (0.83 )**|mean(std)                 |
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




Idiap - Resnet V2 - Casia Webface
=================================

Inspired by `**FaceNet** <https://github.com/davidsandberg/facenet>`_ we here at Idiap trained our own CNN using the Inception Resnet 2 architecture using Casia Webface database.
In this `links <https://gitlab.idiap.ch/bob/bob.bio.htface/blob/eb4f2f66723dc54d9fa5341f9bd46d3b3fe6b347/bob/bio/htface/config/tensorflow/CASIA_inception_resnet_v2_center_loss.py>`_ you can find the script that trains this neural network.

To trigger this training it's necessary to use the `bob.learn.tensorflow <http://gitlab.idiap.ch/bob/bob.learn.tensorflow/>`_ package and run the following command::

  $ ./bin/jman submit --name CELEB-GRAY --queue gpu -- bob_tf_train_generic CASIA_inception_resnet_v2_center_loss.py
  

Some quick details about this CNN (just as a mental note):

  - The hot encoded layer has 10575 neurons.
  - Faces were detected and croped to :math:`182 \times 182` using `MTCNN <https://gitlab.idiap.ch/bob/bob.ip.mtcnn>`_ face and landmark detector
  - The following data augmentation strategies were implemented:
     * Random crop to :math:`160 \times 160`
     * Random Flip
     * Images were normalized to have zero mean and standard deviation one
  - Learning rate of 0.1
  - Adagrad as Optimizer
  - Batch size of 16


Two versions of it were trained: one providing color images for training and another one providing  gray scale images.



Mobio
*****

Follow bellow the results for the mobio-male protocol only.

  +------------+-----------+-------------+
  |            | ERR (dev) | HTER (eval) |
  +============+===========+=============+
  | color      | 6.536%    | 5.831%      |
  +------------+-----------+-------------+  
  | gray-scale | 7.078%    | 8.768%      |
  +------------+-----------+-------------+

The following command line triggers the verification using mobio-male protocol::

 $ ./bob/bio/face-ongoing/configs/mobio--idiap_casia_inception_v2.sh
 $ ./bob/bio/face-ongoing/configs/mobio--idiap_casia_inception_v2_GRAY.sh 



IJB-A
*****

This section presents the results for verification and search protocols.
Check `here <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijba/stable/index.html>`_ for more details.


Verification protocols
----------------------

Follow bellow the results using CMC (Cumulative Matching Curve) and TPIR (True Positive Identification Rate)
under different values of FAR (False Alarm Rate) using the **COLORED** network.

To be done

  
Now the same table using the **GRAY** scaled network.
  
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |    CMC% (R=1)   | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)| split                    |
  +=================+=================+=================+=================+==========================+
  |85.191           |66.889           |25.846           |11.148           |split 0                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |83.931           |70.714           |32.715           |11.861           |split 1                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.384           |72.938           |30.197           |11.847           |split 2                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |88.926           |74.513           |33.556           |9.516            |split 3                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |86.944           |66.363           |27.765           |9.578            |split 4                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.951           |65.655           |27.852           |10.498           |split 5                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |83.717           |65.617           |31.598           |12.167           |split 6                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |83.351           |68.623           |29.242           |10.886           |split 7                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.051           |66.292           |31.798           |14.719           |split 8                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |85.191           |66.889           |25.846           |11.148           |split 9                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |**85.06 (1.61 )**|**68.45 (3.03 )**|**29.64 (2.63 )**|**11.34 (1.42 )**|mean(std)                 |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+


Now the same table using the **COLOR** scaled network.

  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |    CMC% (R=1)   | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)| split                    |
  +=================+=================+=================+=================+==========================+
  |83.195           |61.176           |24.404           |11.481           |split 0                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.027           |61.889           |27.993           |7.757            |split 1                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.186           |61.498           |25.436           |13.531           |split 2                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |86.978           |65.832           |27.323           |9.738            |split 3                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.55            |61.174           |26.112           |10.091           |split 4                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.646           |58.434           |23.665           |11.347           |split 5                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.022           |60.593           |25.242           |11.985           |split 6                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.284           |61.259           |23.372           |14.354           |split 7                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |81.03            |58.764           |25.449           |12.135           |split 8                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |83.195           |61.176           |24.404           |11.481           |split 9                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |**83.01 (1.59 )**|**61.18 (1.9  )**|**25.34 (1.42 )**|**11.39 (1.79 )**|mean(std)                 |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+


 $ ./bob/bio/face-ongoing/configs/ijba--idiap_casia_inception_v2--compare.sh
 $ ./bob/bio/face-ongoing/configs/ijba--idiap_casia_inception_v2_GRAY--compare.sh



Search protocols
----------------

To be done.



Intersession Variability Modelling
==================================

To be done.

Gaussian Mixture Models
=======================
  
To be written.
