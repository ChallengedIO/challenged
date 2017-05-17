#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
description:
Eventually the purpose of CIOFormatter is to operate as a formatter class for accepting challenge 
files from external sources and ensuring they are converted into our current 
format of: 

<EVENT>/<YEAR>/<CATEGORY>/<LEVEL>/<$CHALLENGE>

most likely will run in AWS as a Lambda code function. the idea is to make it easy for ctf organizers
to submit challenges, only handing us challenges files and the formatter requiring only a single
XML file

author: 	q@challenged.io
date: 		05|10|17
license: 	tbd
'''

# Given a DIRECTORY, receive/parse/transform/deliver
# 	receive: 		give me a path and a directory structure and i'll make that data into useable objects
# 	deliver:		give me unorganized_challenge_data as an object and a delivery format and i'll deliver your new formatted data

import os
import xml.etree.ElementTree as et

""" A formatter class for CIO."""
class CIOFormatter:

	# Variables declared here are Class Variables and will be defined within every instance of CIOFormatter.

	""" Typically instance variables are declared here, those used only for an instance of the class."""
	def __init__(self):
		self.repolayout = 'ctfs.xml'		# TODO: do not hard code this
		self.rootdir = ''

	def receive(self, path):
		""" Give me a path, and an XML structure/object, i'll return a new XML object 
				with values of each element included.
		"""
		# TODO: make an XML object from inpath

		self.inpath = path
		self.intree = et.parse(self.repolayout)
		self.inroot = self.intree.getroot()

		# TODO: make a challenge XML object from every challenge in a directory


	def deliver(self, path):
		""" Give me unorganized challenge data as an XML object and a delivery format and I'll deliver 
		your new formatted data"""

		# TODO: make an XML object from outpath

		self.outpath = path
		self.outtree = et.parse(self.repolayout)
		self.outroot = self.outtree.getroot()

if __name__ == "__main__":
	if __debug__:
		c = CIOFormatter(rootdir='/home/q/ctf/challenged.io/write-ups-2014')
		c.receive('/home/q/ctf/challenged.io/write-ups-2014')
		c.deliver('/home/q/ctf/challenged.io/ctf-challenges')
		
		for challenge in c.inroot.findall('challenge'):	
			event = challenge.find('event').text
			year = challenge.find('year').text
			level = challenge.find('level').text
			name = challenge.find('name').text
			points = challenge.find('points').text
			category = challenge.find('category').text
		print event, year, level, name, points, category

	else:
		pass	
