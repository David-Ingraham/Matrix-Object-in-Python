#https://stackoverflow.com/questions/15478127/remove-final-character-from-string
#https://stackoverflow.com/questions/1730961/convert-a-2d-array-index-into-a-1d-index
#https://softwareengineering.stackexchange.com/questions/212808/treating-a-1d-data-structure-as-2d-grid


class Matrix():

    def __init__(self, rows: int, colums: int, data: [int]) -> None:

        #instance variable should be private and not accsed from other scopes. dev needs to build specific fucniotns that will do the change you want.

        
        __slots__ = ('_num_rows', "_num_columns", "_data") #instance variables. the argument names in the __init__ method
        self._num_rows: int = rows
        self._num_columns: int = colums
        self._data: [int] = data.copy()

        if((self._num_rows * self._num_columns) > len(self._data)):
            raise ValueError('Number of columns and/or number of rows dont match length of data') 
      


    def __str__(self) -> str:
        #print(str(self._rows))
        newStr = '|'
        #longestStrLen = len(str(max(self._data)))
        
        longestStrLen = len(str(max(self._data)))

        #a = f"{newStr:<10}"
        
        for i in range(len(self._data)):
            #newStr = newStr + str(self._data[i]).ljust(longestStrLen)
            newStr = newStr + f"{str(self._data[i]):>{longestStrLen}}"
            if (i + 1) % self._num_columns == 0: #the final entry in the row of a matrix will have a multiple of 
                                                #the number of colums as its index in the correspdonding 2d list. added 1 because python 
                newStr = newStr + "|\n|"
            

        #for i in range(len(newStr)):
        
             

        return newStr[:-1]
    

  

    def setValue(self, row: int, colums: int, newValue: int):
        if newValue < 0:
            raise ValueError(f"cannot set using negative value {newValue}")
        idx = (row * self._num_columns) + colums

        self._data[idx] = newValue
    
    def getNumRows(self) -> int:
        return self._num_rows

    def getNumCols(self) -> int:
        return self._num_columns
    
    def getItem(self, row_col_coord: (int))-> int:
        row = row_col_coord[0]
        col = row_col_coord[1]

        indx = (row * self._num_columns) + col

        return self._data[indx]
    

    def __eq__(self, other: "Matrix")-> bool:
        if (self._data == other._data):
            return True
        
        else:
            return False
        

    def __add__(self, other: 'Matrix') -> 'Matrix':

        if ((self._num_columns != other._num_columns) and (self._num_rows != other._num_rows)):
            raise ValueError("two matrices must have same number of columns and rows")
        
        data_list = []
        for i in range(len(self._data)):
            data_list.append(self._data[i] + other._data[i])

        
        return Matrix(self._num_rows, self._num_columns, data_list)
    

    def transpose(self)-> "Matrix":
        

        new_num_columns = self._num_rows
        new_num_rows = self._num_columns

        #new_data = [self._data[j * self._num_columns + i] for i in range(self._num_columns) for j in range(self._num_rows)]


        #print(f"New data : {new_data}")

        #return Matrix(new_num_columns, new_num_rows, new_data)




def main() -> None:

    a = Matrix(2, 3, [12,234,3456,12345,23,3])
    b = Matrix(2, 3, [12,12345,234,23,3456,3])
    d = Matrix(2,3,[1,2,367676,4,5,666])
    #print(a)

    #data = [1,2,3,4,5,6,7,8,9]

    #m1 = Matrix(3,3, data)

    #data[-1] = 99


    c = a + b
 
    print(f'\tPrinted Matrix a : \n{a}\n')
    print(f'\tPrinted Matrix b : \n{b}\n')

    #print(f'testing getItems (0,1):\n{a.getItem((0,2))}\n')

    #print(f'testin __eq__ \n{a == b}\n')

    #print(f"testing __add__ a + b\n{c}\n")
    print(f' Printed Matrix d : \n{d}\n')

    #print(f"tetsing transpose(self) \n{a.transpose()}\n")

    #print(f"\n{a}\n")
    #print(f"\n{b}\n")
    #print(f"\n{c._data}\n")


if __name__ == "__main__":
    main()