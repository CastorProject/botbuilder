#!/usr/bin/env python
import rospy
import time
#Import all components for the robot builder
from toolkit import Toolkit

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
	
	




if __name__ == '__main__':
	t = Toolkit()
	print t.get_components()
	
	t.add_component('test_component', Toolkit)
	print t.get_components()

	t.delete_component('tes_component')
	print t.get_components()
