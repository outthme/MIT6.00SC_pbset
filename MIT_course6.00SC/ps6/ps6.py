# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)
    def __str__(self):
        return  '(' + str(self.x) +', ' + str(self.y) +')'
# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        #detection of room size.
        if width <= 0 or height <= 0:
            raise Exception('The room size should be interger which > 0')            
        self.width = width
        self.height = height
        #Tiles: using dictionary to store tiles and their conditions(0:dirty,
        #1:cleaned).
        self.tiles = {}
        for i in range(self.width):
            for j in range(self.height):
                self.tiles[(i, j)] = 0
        
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        #Firstly, we need to verify that whether robots on the line between
        #tiles or not. Obviously, we can find that the robots are inside one 
        #tiles only if the pos of robots are not equal to the sub-interger. 
        #for example: both pos(3.0, 2.0) and pos(3.1, 2.0) are on the line
        #pos(3.1,2.1) is inside the tile(4, 3)
        x = pos.getX()
        y = pos.getY()
        if x == int(x) or y == int(y):
            pass #robots are on the line between tiles, it can't clean tiles.
        else:    #if not, marke the tile is cleaned which has the robots
            tail_x = int(math.ceil(x))
            tail_y = int(math.ceil(y))
            if self.isTileCleaned(tail_x - 1, tail_y - 1):
                pass
            else: #calculating the position of tails which in the dictionary
                  #Obviously, we can use formula:
                  #'tail_pos = (tail_y - 1) * widthOfRoom + (tail_x - 1)'
                self.tiles[(tail_x - 1, tail_y - 1)] += 1#mark cooresponing tails are cleaned.
                print 'clean tile: ' + str((tail_x - 1, tail_y - 1))
                
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if self.tiles[(m, n)]: # we assumed that(0:tail is dirty, 1: tail is clean)
            return True
        else:
            return False 
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return len(self.tiles)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        numCleanedTiles = 0
        for tile_flag in self.tiles.values():
            if tile_flag:
                numCleanedTiles += 1
            else:
                pass
        return numCleanedTiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.uniform(0, self.width), random.uniform(0, self.height))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if 0 <= pos.getX() <= self.width and 0 <= pos.getY() <= self.height:
            return True
        else:
            return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.robotInRoom = room
        self.robotSpeed = speed
        self.setRobotPosition(self.robotInRoom.getRandomPosition())
        self.setRobotDirection(random.uniform(0,360))

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.robotPosition
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.robotDirection

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.robotPosition = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.robotDirection = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #In this simulation function we test whether the next position is 
        #inside room or not, if position is inside room we move robot onto it
        #and clean the tile which the robot at, otherwise we raise an Exception
        #for the outside room positions.
        temp_pos = self.robotPosition.getNewPosition(self.robotDirection, self.robotSpeed)
        if self.robotInRoom.isPositionInRoom(temp_pos):
            self.setRobotPosition(temp_pos)
            self.robotInRoom.cleanTileAtPosition(self.robotPosition)
        else:
            raise Exception('robot was outside the room!')

# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        temp_pos = self.robotPosition.getNewPosition(self.robotDirection, self.robotSpeed)
        if self.robotInRoom.isPositionInRoom(temp_pos):
            print str(temp_pos) + ' is in the room'
            self.setRobotPosition(temp_pos)
            self.robotInRoom.cleanTileAtPosition(self.robotPosition)
        else: #when the temp_pos is outside the room, it means that robot was 
              #hitted on the walls of the room, then we need to rectify the 
              #temp_pos to a corresponding coordinate which on one wall
              #for example: if roomSize=(width=4, height=4), temp_pos=(-1,3)
              #under such circumstance we should change temp_pos into (0,3)
              #and temp_pos=(0, 3) is on the left wall or the room
            temp_x = 0
            temp_y = 0
            #rectify temp_x
            if temp_pos.getX() < 0:
               temp_x = 0
            elif temp_pos.getX() > self.robotInRoom.width:
                temp_x = self.robotInRoom.width
            #rectify temp_y
            if temp_pos.getY() < 0:
                temp_y = 0
            elif temp_pos.getY() > self.robotInRoom.height:
                temp_y = self.robotInRoom.height
            #move robot onto the wall
            self.setRobotPosition(Position(temp_x,temp_y))
            self.setRobotDirection(random.uniform(0,360)) #choose a random direction
# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    #plot the animation of each trial
    anim = ps6_visualize.RobotVisualization(1, 20, 20)
    for trial in range(num_trials): #run num_trials times.
    #initiallizing room and robots.
        clockTicks = 0
        totalTicks = 0
        room = RectangularRoom(width, height)
        robotList = []
        for foo in range(num_robots):
            robotList.append(robot_type(room, speed))
    #Run robots to clean the room in each trial.
        while True:
            clockTicks += 1
            for robot in robotList:
                robot.updatePositionAndClean()
                anim.update(room, robotList) #plotting animation   
    #Check out whether the percentage of cleaned tiles is larger-equal than min coverage.
            if float(room.getNumCleanedTiles()) / room.getNumTiles() >= min_coverage:
                break
            else:# if the room is not clean enough, go through while-loop again.
                pass
        totalTicks += clockTicks #totalTicks add clockTicks of each trials up.
    anim.done()
    return str(num_robots) + ' robot takes around '\
                    + str(totalTicks / num_trials) + ' clock ticks to clean '\
                    + str(min_coverage*100) + '% of a '\
                    + str(width) + 'x' +str(height) + ' room.'
# === Problem 4
#
# 1) How long does it take to clean 80% of a 20×20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20×20, 25×16, 40×10, 50×8, 80×5, and 100×4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
   

# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
   


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """

