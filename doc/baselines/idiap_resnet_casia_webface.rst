.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


=====================================
Idiap - Resnet V2/V1 - Casia Webface
=====================================

Inspired by `**FaceNet** <https://github.com/davidsandberg/facenet>`_ we here at Idiap trained our own CNN using the Inception Resnet 2 architecture using Casia Webface database.
In this `links <https://gitlab.idiap.ch/bob/bob.bio.htface/blob/eb4f2f66723dc54d9fa5341f9bd46d3b3fe6b347/bob/bio/htface/config/tensorflow/CASIA_inception_resnet_v2_center_loss.py>`_ you can find the script that trains this neural network.

To trigger this training it's necessary to use the `bob.learn.tensorflow <http://gitlab.idiap.ch/bob/bob.learn.tensorflow/>`_ package and run the following command::

  $ ./bin/jman submit --name CELEB-GRAY --queue gpu -- bob_tf_train_generic CASIA_inception_resnet_v2_center_loss.py
  

Some quick details about this CNN (just as a mental note):

  - The hot encoded layer has 10574 neurons.
  - Faces were detected and croped to :math:`182 \times 182` using `MTCNN <https://gitlab.idiap.ch/bob/bob.ip.mtcnn>`_ face and landmark detector
  - The following data augmentation strategies were implemented:
     * Random crop to :math:`160 \times 160`
     * Random Flip
     * Images were normalized to have zero mean and standard deviation one
  - Learning rate of 0.1, 0.01, 0.001
  - RMSPROP Optimizer
  - Batch size of 90


Four versions of it were trained: one providing color images for training and another one providing  gray scale images both using crossentropy loss and crossentropy + center loss.



Mobio
*****

Follow bellow the results for the mobio-male protocol only.

  +------------------------------------------+-----------+-------------+
  |                                          | ERR (dev) | HTER (eval) |
  +==========================================+===========+=============+
  | v2 color cross+center loss               | 1.194%    | 0.893%      |
  +------------------------------------------+-----------+-------------+
  | v1 color cross+center loss               | 1.562%    | 1.184%      |
  +------------------------------------------+-----------+-------------+  
  | v2 color crossentropy loss               | 3.679%    | 3.722%      |
  +------------------------------------------+-----------+-------------+    
  | v2 gray cross+center loss                | 2.686%    | 1.695%      |
  +------------------------------------------+-----------+-------------+
  | v1 gray cross+center loss                | 2.554%    | 1.722%      |
  +------------------------------------------+-----------+-------------+  
  | v2 gray crossentropy loss                | 5.309%    | 6.894%      |
  +------------------------------------------+-----------+-------------+
  | v1 color + Tantriggs crossentropy loss   | 8.655%    | 7.525% *    |  
  +------------------------------------------+-----------+-------------+
  

The following command lines trigger the verification experiment using mobio-male protocol and the results computation (in terms of HTER)
repectivelly::

  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_casia_inception_v2_centerloss --databases mobio
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_casia_inception_v1_centerloss --databases mobio  
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_casia_inception_v2_crossentropy --databases mobio
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_casia_inception_v2_centerloss_gray --databases mobio
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_casia_inception_v1_centerloss_gray --databases mobio
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_casia_inception_v2_crossentropy_gray --databases mobio  
  $ ./bin/collect_results.py -D [MY-PATH] -c HTER


IJB-A
*****

This section presents the results for verification and search protocols.
Check `here <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijba/stable/index.html>`_ for more details.


Verification protocols
----------------------

Follow bellow the results using CMC (Cumulative Matching Curve) and TPIR (True Positive Identification Rate)
under different values of FAR (False Alarm Rate).


  +-----------------------+-----------------+-----------------+-----------------+-----------------+
  |      CNN              |        RR       | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)|
  +=======================+=================+=================+=================+=================+
  | v2 center loss gray   | 90.76 (1.3)     | 82.23 (2.24)    | 46.33 (3.01)    | 23.59 (3.22)    |
  +-----------------------+-----------------+-----------------+-----------------+-----------------+
  | v2 center loss rgb    | 92.12 (1.48)    | 81.03 (1.86)    | 47.48 (2.46)    | 24.97 (4.3)     |
  +-----------------------+-----------------+-----------------+-----------------+-----------------+
  | v2 cross  loss gray   | 85.22 (2.19)    | 68.65 (2.58)    | 25.13 (3.3)     | 7.22  (2.0)     |
  +-----------------------+-----------------+-----------------+-----------------+-----------------+
  | v2 cross loss rgb     | 86.31 (1.36)    | 73.23 (1.59)    | 30.95 (4.14)    | 10.28 (3.6)     |
  +-----------------------+-----------------+-----------------+-----------------+-----------------+





The following command lines triggers, respectivelly, the sequence of verification experiments and plots evaluation tables above::

  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_casia_inception_v2 --databases ijba
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_casia_inception_v2_gray --databases ijba
  $ ./bin/bob_ijba_collect_results.py [MY-PATH-COLOR-EXPERIMENT] -r comparison
  $ ./bin/bob_ijba_collect_results.py [MY-PATH-GRAY-EXPERIMENT] -r comparison  


Search protocols
----------------

.. Todo:: To be done


LFW
***

This section presents the results for LFW 10 fold:


  +-----------------------+-----------------+-----------------+-----------------+
  |      CNN              | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)|
  +=======================+=================+=================+=================+
  | v2 center loss gray   | 97.8  (1.36)    | 91.43 (3.37)    | 0.0   (0.0)     |
  +-----------------------+-----------------+-----------------+-----------------+
  | v2 center loss rgb    | 97.93 (1.21)    | 91.33 (1.99)    | 0.0   (0.0)     |
  +-----------------------+-----------------+-----------------+-----------------+


The following command lines trigger the experiments 

  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_casia_inception_v2_centerloss_gray --databases lfw
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_casia_inception_v2_centerloss --databases lfw  
  $ ./bin/bob_ijba_collect_results.py [MY-PATH] -r comparison




IJB-C
*****

This section presents the results for verification (1:1) protocol.
Check `bob.db.ijbc <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijbc/stable/index.html>`_ for more details.

  +-----------------------+-----------------+-----------------+-----------------+-----------------+
  |      CNN              |        RR       | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)|
  +=======================+=================+=================+=================+=================+
  | v1 center loss gray   |59.787           |90.597           |67.945           |41.402           |
  +-----------------------+-----------------+-----------------+-----------------+-----------------+
  | v1 center loss rgb    |61.619           |90.985           |68.4             |42.041           |
  +-----------------------+-----------------+-----------------+-----------------+-----------------+
  | v2 center loss gray   |58.312           |90.806           |66.754           |39.577           |
  +-----------------------+-----------------+-----------------+-----------------+-----------------+
  | v2 center loss rgb    |61.154           |90.633           |67.388           |41.837           |
  +-----------------------+-----------------+-----------------+-----------------+-----------------+






.. Note::
  The result doesn't look sound. How is it possible to have RR=70% and TPIR under certain threshold above this value?

The following command line triggers the sequence of verification experiments::

 $ ./bin/bob_faceongoing_baselines.py --baselines facenet_msceleba_inception_v1 --databases ijbc
 $ ./bin/bob_ijba_collect_results.py [MY-PATH] -r comparison

