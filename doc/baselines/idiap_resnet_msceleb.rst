.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


============================
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
  | color      | 5.676%    | 5.876%      |
  +------------+-----------+-------------+  
  | gray-scale | 12.989%   | 12.989%     |
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


