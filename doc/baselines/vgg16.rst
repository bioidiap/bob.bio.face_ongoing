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

  +-----------------+-----------------+-----------------+-----------------+
  |        RR       | TPIR% (FAR=0.1) | TPIR% (FAR=0.01)|TPIR% (FAR=0.001)|
  +=================+=================+=================+=================+
  |  96.17 (0.66 )  |  88.23 (1.12)   |  58.36 (3.6)    | 31.55 (4.31)    |
  +-----------------+-----------------+-----------------+-----------------+


The following command lines triggers, respectivelly, the sequence of verification experiments and plots the evaluation table above::

  $ ./bin/bob_faceongoing_baselines.py --baselines vgg16 --databases ijba
  $ ./bin/bob_ijba_collect_results.py [MY-PATH] -r comparison


IJB-C
*****

.. Todo:: Running

