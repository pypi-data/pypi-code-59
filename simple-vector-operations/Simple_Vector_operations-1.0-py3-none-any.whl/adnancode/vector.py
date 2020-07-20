class Vector:
    """ 
    This class perform operations on vectors

    """
    def add(self,lst1,lst2):
        """
        you can add vector using this method
        
        syntax:Vector.add([x1,y1,z1],[x2,y2,z2])
        return: Addition of vectors
        """
        self.lst1,self.lst2=lst1,lst2
        sum= [a+b for a,b in zip(self.lst1,self.lst2)]
        return sum
        
    def subtract(self,lst1,lst2):
        """
        you can subtract vector using this method

        syntax:Vector.subtract([x1,y1,z1],[x2,y2,z2])
        return: Subtraction of vectors
        """
        self.lst1,self.lst2=lst1,lst2
        subtract= [a-b for a,b in zip(self.lst1,self.lst2)]
        return subtract
    def dist(self,lst1,lst2):
        """
        you can find distance between two vectors using this method

        syntax:Vector.dist([x1,y1,z1],[x2,y2,z2])
        return: Distance between vectors
        """
        self.lst1,self.lst2=lst1,lst2
        distance= [b-a for a,b in zip(self.lst1,self.lst2)]
        return distance
    def unitvector(self,lst):
        """
        you can find  unit vector using this method

        syntax:Vector.unitvector([x,y,z])
        return: Unit vector of given vector
        """
        self.lst=lst
        mod=sum(self.lst)**0.5
        unit= [x/mod for x in self.lst]
        return unit
    def crossp(self,lst1,lst2):
        """"
        you can find cross product using this method

        syntax:Vector.croosp([x1,y1,z1],[x2,y2,z2])
        return: cross product of vectors
        """
        self.lst1,self.lst2=lst1,lst2
        x=self.lst1[1]*self.lst2[2]-self.lst1[2]*self.lst2[1]
        y=-self.lst1[0]*self.lst2[2]+self.lst1[2]*self.lst2[0]
        z=self.lst1[0]*self.lst2[1]-self.lst1[1]*self.lst2[0]
        return [x,y,z]

    def dotp(self,lst1,lst2):
        """"
        you can find dot product using this method

        syntax:Vector.dotp([x1,y1,z1],[x2,y2,z2])
        return: dot product of vectors
        """
        self.lst1,self.lst2=lst1,lst2
        dot= [a*b for a,b in zip(self.lst1,self.lst2)]
        return dot


