#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
description: CIODownloader - retrieves challenge files from S3 repository
date: 	05|11|17
license: tbd
'''

import os

""" A Downloader class for CIO."""
class CIODownloader(object):
	""" Typically instance variables are declared here, those used only for an instance of the class."""

	def __init__(self):
		# Variables declared here are Class Variables and will be defined within every instance of CIOFormatter.
		self.event = "DEFCON"
		self.year = "2011"
		self.category = "PWN"
		self.difficulty = "1"
		self.name = "B100"
		self.url = "https://s3.amazonaws.com/ctf-challenges/DEFCON/Defcon-19-quals/Binary_L33tness/b100/b100_6817e51fa3b60f176b56"

if __name__ == "__main__":
	# test harness code
	if __debug__:
		# TODO: some debug shit
		c = CIODownloader()
		# ...
	else:
		pass
