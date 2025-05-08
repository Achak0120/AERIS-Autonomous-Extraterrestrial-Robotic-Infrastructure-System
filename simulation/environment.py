import numpy as np
import pybullet as p
import pybullet_data
import time

p.connect(p.GUI) # connect to environment

p.resetSimulation()
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Create gravity for environment ---> Mars Gravity Constant
p.setGravity(0, 0, -3.721)

# Run in real time --> Mars conditions
p.setRealTimeSimulation(1)

# Load Assets
p.loadURDF("plane.urdf", [0, 0, 0], [0, 0, 0, 1])
targid = p.loadURDF("franka_panda/panda.urdf", [0, 0, 0], [0, 0, 0, 1], useFixedBase = False)
obj_of_focus = targid # accessor for the URDF