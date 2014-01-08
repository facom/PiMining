PiMining
Jorge I. Zuluaga (C) 2013
-------------------------

This set of scripts and C programs are intended to mine the digits of
pi and running a diversity of analysis on them.

Originally intended for fun it could also be used for research.

Quick start
===========

1. Get a copy of PiMining from https://github.com/facom/PiMining:

   NOTE: You can get an anonymous clone of the project using:

   $ git clone git://github.com/facom/PiMining.git

   Then you will be able to get updates using 'git pull'.

2. Download digits.  For geting the 1 billion digits binary file,
   download the file "pi.bin.bz2" from http://bit.ly/pi-bin (411 MB).
   Place it in the "numbers" folder and uncompress it:

   $ bunzip2 pi.bin.bz2

3. Compile utilities:

   $ make compile

4. Run examples in python

   $ python pi.py

5. Search for a string:

   $ ./pi.out 123 1000

   this command search string 123 in the first 1000 digits.

For the contirbutor
===================

1. Generate a public key of your account at the server where you will
   develop contributions:

   $ ssh-keygen -t rsa -C "user@email"

2. Upload public key to the github project site
   (https://github.com/facom/PiMining).  You will need access to the
   account where the repository was created.

3. Configure git:

   $ git config --global user.name "Your Name"
   $ git config --global user.email "your@email"

4. Get an authorized clone of the master trunk:

   $ git clone git@github.com:facom/PiMining.git

