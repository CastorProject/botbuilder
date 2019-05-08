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
		
		

class Assembler(object):
	'''Assembler class to create the robot modules based on yaml files'''
	def __init__(self):
		rospy.init_node("robot_builder")
		self.rate = rospy.Rate(10)
		self.modules = []
		self.load_robot_file()
		
	
	def load_robot_file(self):
		self.robot = rospy.get_param("robot")
		print self.robot['physical_modules']
		for module in self.robot['physical_modules']:
			self.modules.append(Module(module))
			print "###################################################"
			print self.robot['physical_modules'][module]['components']
			print "###################################################"
		
		for m in self.modules:
			m.print_name()
			
		
		

a = Assembler()
time.sleep(3)
a.load_robot_file()

