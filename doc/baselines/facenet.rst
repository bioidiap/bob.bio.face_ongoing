.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


===================================
Resnet V1 trained by David Sandberg
===================================

Very recently, David Sandberg has made publicly available his implementation as well as trained models for a new FR-CNN named `**FaceNet** <https://github.com/davidsandberg/facenet>`_.
This is the closest open-source implementation of the FaceNet CNN proposed by [Schroff_2015], for which neither a pre-trained model nor the training-set is publicly available.
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

The following command lines trigger the verification experiment using mobio-male protocol and the results computation (in terms of HTER)
repectivelly::

 $ ./bin/bob_faceongoing_baselines.py --baselines facenet_msceleba_inception_v1 --databases mobio
 $ ./bin/collect_results.py -D [MY-PATH] -c HTER


IJB-A
*****

This section presents the results for verification and search protocols.
Check this `link <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijba/stable/index.html>`_ for more details.


Verification protocols
----------------------

Follow bellow the results using CMC (Cumulative Matching Curve) and TPIR (True Positive Identification Rate)
under different values of FAR (False Alarm Rate).

  +-----------------+-----------------+-----------------+-----------------+--------------------------+
  |        RR       | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)| split                    |
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
  |**94.43 (0.57 )**|**92.59 (1.05 )**|**67.94 (2.87 )**|**40.89 (6.45 )**|mean(std)                 |
  +-----------------+-----------------+-----------------+-----------------+--------------------------+



The following command lines triggers, respectivelly, the sequence of verification experiments and plots this evaluation table above::

 $ ./bin/bob_faceongoing_baselines.py --baselines facenet_msceleba_inception_v1 --databases ijba
 $ ./bin/bob_ijba_collect_results.py [MY-PATH] -r comparison
 

IJB-B
*****

This section presents the results for verification (1:1) protocol.
Check `here <https://www.idiap.ch/software/bob/docs/bob/bob.db.ijbb/stable/index.html>`_ for more details.

+-----------------+-----------------+-----------------+-----------------+
|        RR       | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)|
+=================+=================+=================+=================+
|72.736           |96.904           |85.891           |62.853           |
+-----------------+-----------------+-----------------+-----------------+

.. Note::
  The result doesn't look sound. How is it possible to have RR=70% and TPIR under certain threshold above this value?

The following command line triggers the sequence of verification experiments::

 $ ./bin/bob_faceongoing_baselines.py --baselines facenet_msceleba_inception_v1 --databases ijbb
 $ ./bin/bob_ijba_collect_results.py [MY-PATH] -r comparison



LFW
***

This section presents the results for LFW 10 fold:

  +----------------+
  | FRR (FAR 0.01) |
  +================+
  | 98.13% (1.06)  |
  +----------------+


The following command lines trigger the verification experiment using mobio-male protocol and the results computation (in terms of HTER)
repectivelly::

  $ ./bin/bob_faceongoing_baselines.py --baselines facenet_msceleba_inception_v1 --databases lfw




