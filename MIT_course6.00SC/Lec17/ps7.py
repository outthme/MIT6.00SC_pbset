# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        # TODO
        if maxBirthProb < 0 or maxBirthProb >1 \
            or clearProb < 0 or clearProb > 1:
                raise Exception('Defined wrong maxBirthProb or clearProb!')
        else:
            self.maxBirthProb = maxBirthProb
            self.clearProb = clearProb

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        # TODO
        if random.random() <= self.clearProb: #In this case, virus cell was cleaned
            return True
        else:
            return False
    
    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        # TODO
        if random.random() <= self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException('NoChildBeReproduced')


class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        # TODO
        if len(viruses) <= 0 or  maxPop <= 0:
            raise Exception('viruses and maxPop can not be negatives!')
        else:
            self.viruses =viruses
            self.maxPop = maxPop
            self.popDensity = len(viruses) / maxPop

    def getTotalPop(self):

        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """

        # TODO        
        return len(self.viruses)

    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO
        # Clear virus in self.viruses list following with doesClear()
        virusId = 0
        for virus in self.viruses:  #does class NotClearException will be effect?
            if virus.doesClear():   
                self.viruses.pop(virusId)
            else:
                pass
            virusId += 1
        self.popDensity = len(self.viruses) / self.maxPop#calculate popDensity after cleaning
        for survived_virus in self.viruses: #set in reproduce process
            try:
                self.viruses.append(survived_virus.reproduce(self.popDensity))
            except NoChildException, e: #if it unsucessful in reproduce virus
                print e                 #raise NoChildExceptions
        return len(self.viruses)       


#
# PROBLEM 2
#
def simulationWithoutDrug():

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """

    # TODO
    #Initializing Simulation paraments
    timeSteps = 300
    simulation1 = []
    simulation2 = []
    simulation3 = []
    simulations = [simulation1, simulation2, simulation3]
    #Initializing parameters and SimplePatient 
    viruses = []
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    for i in range(100):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    test_patient = SimplePatient(viruses, maxPop)
    for simulation in simulations:
        for step in range(timeSteps): #Starting simulations for 300 time steps
            simulation.append(test_patient.update())
    dataset = numpy.array(simulation1) + numpy.array(simulation2) + numpy.array(simulation3)
    dataset = dataset / 3
    x = []
    for i in range(1,301):
        x.append(i)
    x = numpy.array(x)
    pylab.plot(x, dataset)
    pylab.xlabel('Time steps.')
    pylab.ylabel('Amounts of viruses.')
    pylab.title('Viruses dynamic plot')
    