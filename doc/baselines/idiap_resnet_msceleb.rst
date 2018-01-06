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

The following command lines trigger the verification experiments using mobio-male protocol and the results computation (in terms of HTER)
repectivelly::

  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_msceleba_inception_v2 --databases mobio
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_msceleba_inception_v2_gray --databases mobio
  $ ./bin/collect_results.py -D [MY-PATH] -c HTER


Data selection is everything,  bellow follow the same architection working with a different prunning based on DBScan outlier detector using the facenet embeddings.

.. Todo:: Details about this strategy is needed.


The following command lines trigger the verification experiments under these new data selection::

  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_msceleba_inception_v2_facenet_prunning --databases mobio
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_msceleba_inception_v2_gray_facenet_prunning --databases mobio
  $ ./bin/collect_results.py -D [MY-PATH] -c HTER


As before, follow this results in terms of HTER of such data selection.

  +-------------------------+-----------+-------------+
  |                         | ERR (dev) | HTER (eval) |
  +=========================+===========+=============+
  | color - centerloss      | 4.161%    | 4.114%      |
  +-------------------------+-----------+-------------+
  | gray-scale - crossent.  | 4.336%    | 5.513%      |
  +-------------------------+-----------+-------------+
  | gray-scale - centerloss | 4.336%    | 5.513%      |
  +-------------------------+-----------+-------------+


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


Data selection is everything, bellow follow the same architecture working with a different prunning based on DBScan outlier detector using facenet embeddings.

.. Todo:: Details about this strategy is needed.

Below follow the same results with this data prunning using the **COLORED** network:

  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |        RR       | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)| split                    |
  +=================+=================+=================+=================+==========================+
  |82.973           |73.821           |19.135           |4.049            |split 0                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.139           |71.332           |21.698           |6.521            |split 1                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.88            |71.429           |22.416           |4.065            |split 2                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |87.924           |75.626           |24.93            |6.9              |split 3                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |85.918           |71.437           |18.13            |3.763            |split 4                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.524           |70.449           |21.056           |5.643            |split 5                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.383           |70.46            |25.726           |5.327            |split 6                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |80.203           |62.38            |16.649           |3.148            |split 7                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.219           |68.989           |20.955           |3.933            |split 8                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |82.973           |73.821           |19.135           |4.049            |split 9                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |**83.61 (2.03 )**|**70.97 (3.42 )**|**20.98 (2.73 )**|**4.74  (1.21 )**|mean(std)                 |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+

Now the same table using the **GRAY** scaled signals.

  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |        RR       | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)| split                    |
  +=================+=================+=================+=================+==========================+
  |79.978           |58.458           |13.921           |2.219            |split 0                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |79.227           |56.043           |11.411           |2.979            |split 1                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |77.328           |56.446           |12.66            |2.613            |split 2                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |84.641           |67.39            |15.637           |3.617            |split 3                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |83.124           |62.543           |15.45            |3.079            |split 4                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |78.58            |58.192           |13.228           |2.913            |split 5                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |79.6             |61.077           |14.891           |4.298            |split 6                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |75.72            |50.534           |9.232            |2.508            |split 7                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |79.351           |59.157           |12.978           |3.034            |split 8                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |79.978           |58.458           |13.921           |2.219            |split 9                   |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |**79.75 (2.44 )**|**58.83 (4.19 )**|**13.33 (1.84 )**|**2.95  (0.61 )**|mean(std)                 |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+


The following command lines trigger the verification experiments under these new data selection::

  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_msceleba_inception_v2_facenet_prunning --databases ijba
  $ ./bin/bob_faceongoing_baselines.py --baselines idiap_msceleba_inception_v2_gray_facenet_prunning --databases ijba
  $ ./bin/collect_results.py -D [MY-PATH] -c HTER



Search protocols
----------------

.. Todo:: To be done

