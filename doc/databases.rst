.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


==========
 Databases
==========


MOBIO
-----

The MOBIO database is a bi-modal (face/speaker) video database recorded from 152 people. 
The database has a female-male ratio of nearly 1:2 (100 males and 52 females) and was collected from August 2008 until July 2010 in 6 different sites from 5 different countries. 
In total 12 sessions were captured for each individual.

The database was recorded using two types of mobile devices: mobile phones (NOKIA N93i) and laptop computers (standard 2008 MacBook). 
In this paper we only use the mobile phone data. 
The MOBIO database is challenging since the data are acquired with uncontrolled illumination, facial expression, and face pose, and sometimes only parts of the face are visible.


IARPA Janus Benchmark A (IJB-A)
-------------------------------

The IJB-A database is a mixture of frontal and non-frontal images and videos (provided as single frames) from 500 different identities.
In many of the images and video frames, there are several people visible, but only the ones that are annotated with a bounding box should be taken into consideration.
For both model enrollment as well as for probing, images and video frames of one person are combined into so-called Templates.

The database is divided in 10 splits each defining training, enrollment and
probe data.


IARPA Janus Benchmark A (IJB-B)
-------------------------------

The IJB-B database is a mixture of frontal and non-frontal images and videos
(provided as single frames) from 1845 different identities. 
In many of the images and video frames, there are several people visible, but only the ones that are annotated with a bounding box should be taken into consideration.
For both model enrollment as well as for probing, images and video frames of one person are combined into so-called Templates.
For some of the protocols, probe templates are also generated from raw video data.

