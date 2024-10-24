import pybullet as p
import time

physicsClient = p.connect(p.GUI)

duration = 1000
for i in range(duration):
    p.stepSimulation()
    time.sleep(0.5)


p.disconnect