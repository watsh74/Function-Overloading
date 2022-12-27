class calculate:
    def area(self,*args):
        if len(args)==1:
            self.side=args[0]
            print ('Area of square=',self.side*self.side)
        if len(args)==2:
            self.L=args[0]
            self.B=args[1]
            print('Area of rectangle',self.L*self.B)
        if len(args)==3:
            self.L=args[0]
            self.B=args[1]
            self.H=args[2]
            print('Vol of cuboid=',self.L*self.B*self.H)

o=calculate()
o.area(10)
o.area(10,20)
o.area(10,20,30)


        
