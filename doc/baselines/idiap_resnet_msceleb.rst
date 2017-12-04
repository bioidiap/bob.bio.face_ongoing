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
  | color      | 5.277%    | 4.881%      |
  +------------+-----------+-------------+  
  | gray-scale | 10.152%   | 6.970%      |
  +------------+-----------+-------------+

The following command lines trigger the verification experiment using mobio-male protocol and the results computation (in terms of HTER)
repectivelly::

  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_msceleba_inception_v2 --databases mobio
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_msceleba_inception_v2_gray --databases mobio
  $ ./bin/collect_results.py -D [MY-PATH] -c HTER


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
  |86.356           |76.927           |24.126           |5.047            |split 0                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.378           |73.243           |26.363           |8.657            |split 1                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |85.078           |73.635           |26.249           |3.368            |split 2                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |88.926           |77.017           |27.268           |4.508            |split 3                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |86.887           |75.314           |27.309           |4.048            |split 4                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |83.495           |74.15            |25.0             |4.672            |split 5                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.806           |74.274           |28.814           |8.535            |split 6                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |81.91            |67.769           |18.997           |5.443            |split 7                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |85.45            |71.348           |23.258           |3.483            |split 8                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |86.356           |76.927           |24.126           |5.047            |split 9                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |**85.36 (1.84 )**|**74.06 (2.73 )**|**25.15 (2.62 )**|**5.28  (1.77 )**|mean(std)                 |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+

  
Now the same table using the **GRAY** scaled network.
  
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |    CMC% (R=1)   | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)| split                    |
  +=================+=================+=================+=================+==========================+
  |81.974           |62.008           |13.533           |1.331            |split 0                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |80.515           |57.448           |13.266           |1.799            |split 1                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |79.352           |55.807           |11.15            |0.29             |split 2                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.752           |60.657           |13.801           |1.836            |split 3                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |85.006           |57.526           |11.973           |0.399            |split 4                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |79.49            |58.313           |13.471           |1.517            |split 5                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |81.78            |58.293           |13.136           |1.755            |split 6                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |77.481           |47.279           |8.591            |1.014            |split 7                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |81.477           |55.73            |10.506           |0.169            |split 8                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |81.974           |62.008           |13.533           |1.331            |split 9                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |**81.38 (2.21 )**|**57.51 (4.03 )**|**12.3  (1.63 )**|**1.14  (0.61 )**|mean(std)                 |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+

The following command lines triggers, respectivelly, the sequence of verification experiments and plots the evaluation tables above::

  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_msceleba_inception_v2 --databases ijba
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_msceleba_inception_v2_gray --databases ijba
  $ ./bin/bob_ijba_collect_results.py [MY-PATH-COLOR-EXPERIMENT] -r comparison
  $ ./bin/bob_ijba_collect_results.py [MY-PATH-GRAY-EXPERIMENT] -r comparison  


Search protocols
----------------

To be done.


