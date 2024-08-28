# #!/usr/bin/env python3

# class Shoe:
#    def __init__(self, brand,size ):
#       self.brand= brand
#       self.size= size

#    @property
#    def brand(self):
#         return self._brand
#    @brand.setter
#    def brand(self, brand):
#       self._brand = brand

#    @property
#    def size(self):
#        return self._size
#    @size.setter
#    def size(self, size):
#        if isinstance(size,int):
#            self._size = size
#        else:
#           print('size must be an integer')   
#    def cobble(self):
#         """Repairs the shoe and sets its condition to 'New'."""
#         print("Your shoe is as good as new!")
#         self.condition = "New"  # Set the condition to "New"

class Shoe:
    def __init__(self, brand, size, condition = 'New'):
        self.brand = brand
        self.size = size
        self.condition = condition
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
           print('size must be an integer')

    @property
    def condition(self):
        return self._condition
    @condition.setter
    def condition(self, condition):
        self._condition = condition

    def cobble(self):
        print('Your shoe is as good as new!')
        self.condition = 'New'

            