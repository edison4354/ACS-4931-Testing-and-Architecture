LEGAL_DRINKING_AGE = 18


class Person:
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    age : float
        age of the person
    """
    
    def __init__(self, my_age):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            age : float
                age of the person
        """
        self.age = my_age


def enter_night_club(individual):
    '''
    Prints if a person is over the LEGAL_DRINKING_AGE and allowed to enter.

            Parameters:
                    individual (obj): A person object
    '''
    if individual.age > LEGAL_DRINKING_AGE:
        print("Allowed to enter.")
    else:
        print("Entrance of minors is denied.")


person = Person(17.9)
enter_night_club(person)
