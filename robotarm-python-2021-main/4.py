from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

robotArm.grab()
for moveRight in range(2):
    robotArm.moveRight()
robotArm.drop()
for moveLeft in range(2):
    robotArm.moveLeft()
robotArm.grab()
for moveRight in range(2):
    robotArm.moveRight()
robotArm.drop()
for moveLeft in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for grabDrop in range(2):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
