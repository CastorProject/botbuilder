#!/usr/bin/env python
import rospy
import time

#import actuator.Actuator as Actuator

#base class for modules
class Module(object):
	'''Module base class'''
	def __init__(self, args):
		self.name = args
		self.components = []
		pass
		
	def print_name(self):
		print "Oject class: " +  str(type(self)) + " my name is: " + self.name
					
	def register_component(self, component):
		self.components.append(component)
		pass
		
		


		
		

if __name__ == '__main__':
	a = Assembler()
	time.sleep(3)
	a.load_robot_file()

