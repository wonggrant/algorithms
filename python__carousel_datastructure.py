

class Carousel:

    def __init__(self, N):
        self.N = N
        self.LIST__ = []
        self.NONE = 328093
        self.COUNTER = 0
        self.__pointer = 0
        for i in range(self.N):
            self.LIST__.append(self.NONE)


    def __next__(self):
        self.COUNTER += 1
        self.__pointer = self.COUNTER % self.N


        
    def PLACE(self, element):
        if self.LIST__[self.__pointer] is not self.NONE:
            return False
        self.LIST__[self.__pointer] = element
        return True


    
    def VIEW(self):
        if self.LIST__[self.__pointer] is self.NONE:
            return False
        return self.LIST__[self.__pointer]


    
    def TAKE(self):
        if self.LIST__[self.__pointer] is self.NONE:
            return False
        self.__ELEMENT = self.LIST__[self.__pointer]
        self.LIST__[self.__pointer] = self.NONE
        return self.__ELEMENT
    
    def __str__(self):
        # i
        # 0   1    2    3   4
        # len(element__str__)
        #   4   5    5   3  3
        # [12][168][125][1][0]
        #        ^
        #     __pointer
        __return__ = ""
        __pointer_defined = False
        __pointer_spaces = 0
        for i,e in enumerate(self.LIST__):
            element__str__ = '['+str(e)+']'
            if i == self.__pointer:
                __pointer_spaces += len(element__str__) // 2
                break
            else:
               __pointer_spaces += len(element__str__)

        for i,e in enumerate(self.LIST__):
            element__str__ = '['+str(e)+']'
            __return__ += element__str__
            
        __return__ += '\n'
        for i in range(__pointer_spaces -1):
            __return__ += ' '
        __return__ += '^'
        return __return__
