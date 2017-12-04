.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


=====
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
  

The following command lines trigger the verification experiment using mobio-male protocol and the results computation (in terms of HTER)
repectivelly::

  $ ./bin/bob_faceongoing_baselines.py --baselines vgg16 --databases mobio
  $ ./bin/collect_results.py -D [MY-PATH] -c HTER
  

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


The following command lines triggers, respectivelly, the sequence of verification experiments and plots the evaluation table above::

  $ ./bin/bob_faceongoing_baselines.py --baselines vgg16 --databases ijba
  $ ./bin/bob_ijba_collect_results.py [MY-PATH] -r comparison


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


The following command lines triggers, respectivelly, the sequence of search experiments and plots the evaluation table above::

  $ ./bin/bob_faceongoing_baselines.py --baselines vgg16 --databases ijba
  $ ./bin/bob_ijba_collect_results.py [MY-PATH] -r search

IJB-B
*****

.. Todo:: Running

