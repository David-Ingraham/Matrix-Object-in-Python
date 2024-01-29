from dcs299_lab2 import Matrix



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
        # Split the flat data list into a list of rows
        rows = [self._data[i:i + self._num_columns] for i in range(0, len(self._data), self._num_columns)]

        # Find the longest string length for each column
        column_lengths = [max(len(str(rows[row][col])) for row in range(self._num_rows)) for col in range(self._num_columns)]

        # Build the string representation
        newStr = '|'
        for row in rows:
            for col, item in enumerate(row):
                formatted_item = f"{item:>{column_lengths[col]}}"
                newStr += formatted_item + " "
            newStr = newStr.rstrip()  # Remove trailing space
            newStr += "|\n|"
        
        return newStr.rstrip('|').rstrip()



    def __mul__(self, other: 'Matrix')-> 'Matrix':
        if self._num_columns != other._num_rows:
            raise ValueError("Number of columns must match number of rows to mupltuply to matrices. ")
        if self._num_rows != other._num_columns:
            raise ValueError("Number of columns must match number of rows to mupltuply to matrices. ")
        

        result_data = [0] * (self._num_rows * other._num_columns)
        result_matrix = Matrix(self._num_rows, other._num_columns, result_data)

            # Perform multiplication
        for i in range(self._num_rows):
            for j in range(other._num_columns):
                sum = 0
                for k in range(self._num_columns):
                    sum += self._data[i * self._num_columns + k] * other._data[k * other._num_columns + j]
                result_matrix._data[i * other._num_columns + j] = sum

        return result_matrix






def main()->None:

    a = Matrix(2, 3, [1,2,3,4,5,6])
    b = Matrix(3,2,[70,8,9,10,11,12])

    c = a * b

    print(f"printing a: \n{a}\n")
    print(f"printing b: \n{b}\n")
    print(f"printing c: \n{c}\n")



if __name__ == '__main__':

    main()