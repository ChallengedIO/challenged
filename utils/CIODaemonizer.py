#! /usr/bin/env python

'''
description: CIODaemonizer - executes challenge files as a local service for the user.
date: 	05|11|17
license: tbd
'''

import os

""" A Daemonizer class for CIO."""
class CIODaemonizer:

	# Variables declared here are Class Variables and will be defined within every instance of CIOFormatter.

	""" Typically instance variables are declared here, those used only for an instance of the class."""
	def __init__(self):
		pass

if __name__ == "__main__":
	# test harness code
	if __debug__:
		# TODO: some debug shit
		c = CIODaemonizer()
		# ... 
	else:
		pass
