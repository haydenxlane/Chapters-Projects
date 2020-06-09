class Car:
    '''
    Class for creating car objects.
    '''

    average_person_weight = 70
    min_pax_count = 1
    max_pax_count = 5
    max_car_mass = 2000
    min_car_mass = 0

    def __init__(self, pax_count, car_mass, gear_count):
        '''
        The constructor for Car class.

        Parameters:
            pax_count - number of passengers riding in the car (including the driver)
            car_mass - mass of the empty car (in kg)
            gear_count - number of gears
        '''

        if not Car.validate_pax_count(pax_count):
            raise IllegalCarError("Number of passengers is not in (1, 5) range")
        if not Car.validate_car_mass(car_mass):
            raise IllegalCarError("Car mass is not in (0, 2000) range")

        self._pax_count = pax_count
        self._car_mass = car_mass
        self._gear_count = gear_count

    def __str__(self):
        val = '''
        Pax Count: {0}
        Mass of a car: {1}
        Number of grears: {2}
        Total mass of a car {3}
        '''.format(self.pax_count, self.car_mass, self.gear_count, self.total_mass)
        
        return val

    @property
    def pax_count(self):
        return self._pax_count

    @pax_count.setter
    def pax_count(self, new_pax):
        if not Car.validate_pax_count(new_pax):
            raise IllegalCarError("Number of passengers is not in (1, 5) range")
        self._pax_count = new_pax

    @property
    def car_mass(self):
        return self._car_mass

    @car_mass.setter
    def car_mass(self, new_mass):
        if not Car.validate_car_mass(new_mass):
            raise Exception("Car mass is not in (0, 2000) range")
        self._car_mass = new_mass

    @property
    def gear_count(self):
        return self._gear_count
    @gear_count.setter
    def gear_count(self, new_gear):
        self._gear_count = new_gear

    @property
    def total_mass(self):
        return self._car_mass + (self._pax_count * Car.average_person_weight)

    @staticmethod
    def validate_pax_count(pax_count):
        '''
        Checks if the pax_count value is valid
        Returns True if valid, False if invalid
        '''
        if pax_count < Car.min_pax_count or pax_count > Car.max_pax_count:
            return False
        else:
            return True

    @staticmethod
    def validate_car_mass(car_mass):
        '''
        Checks if the car_mass value is valid
        Returns True if valid, False if invalid
        '''
        if car_mass > Car.max_car_mass:
            return False
        if car_mass < Car.min_car_mass:
            return False
        else:
            return True

class IllegalCarError(Exception):
    '''Exception raised for errors in creating Car objects'''
    pass

def main():
    while True:
        print("Welcome to the car creator! \nWe need some details about the car.")
        pax_count = int(input("Please provide pax count: "))
        car_mass = int(input("Please provide mass of a car: "))
        gear_count = int(input("Please provide number of gears: "))

        test_object = Car(pax_count, car_mass, gear_count)

        print("Congratulations! Your car object was succesfully created!")
        print("The details are as follows: " + str(test_object))
        key = input("Press q if you want to quit or any other key to try again: ")
        if key == 'q':
            break

if __name__ == '__main__':
    main()
