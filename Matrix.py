#Resources:

#https://stackoverflow.com/questions/15478127/remove-final-character-from-string
#https://stackoverflow.com/questions/1730961/convert-a-2d-array-index-into-a-1d-index
#https://en.wikipedia.org/wiki/Matrix_multiplication
#https://en.wikipedia.org/wiki/Transpose
#https://stackoverflow.com/questions/28253102/python-3-multiply-a-vector-by-a-matrix-without-numpy


class Matrix():
    """
    Class to represent a matrix.

    Args:
        rows: The number of rows in the matrix.
        columns: The number of columns in the matrix.
        data: A list of values for the matrix.

    Raises:
        ValueError: If the number of columns and/or number of rows don't match the length of the data.
    """
    
    __slots__ = ('_num_rows', "_num_columns", "_data") #instance variables. the argument names in the __init__ method
    def __init__(self, rows: int, colums: int, data: [int]) -> None:

        #instance variable should be private and not accsed from other scopes. dev needs to build specific fucniotns that will do the change you want.

   
        
        
        self._num_rows: int = rows
        self._num_columns: int = colums
        self._data: [int] = data.copy()

        if((self._num_rows * self._num_columns) > len(self._data)):
            raise ValueError('Number of columns and/or number of rows dont match length of data') 
      


    def __str__(self) -> str:

        """
        Returns a string representation of the matrix.

        Returns:
            A string representation of the matrix.
        """

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

    

  

    def setValue(self, row: int, colums: int, newValue: int):
        """
        Sets the value at the specified row and column.

        Args:
            row: The row index.
            columns: The column index.
            newValue: The new value.

        Raises:
            ValueError: If the new value is negative.
        """

        if newValue < 0:
            raise ValueError(f"cannot set using negative value {newValue}")
        idx = (row * self._num_columns) + colums

        self._data[idx] = newValue
    
    def getNumRows(self: 'Matrix') -> int:
        """
        Returns the number of rows in the matrix.

        Returns:
            The number of rows in the matrix.
        """



        return self._num_rows

    def getNumCols(self) -> int:
        """
        Returns the number of columns in the matrix.

        Returns:
            The number of columns in the matrix.
        """

        return self._num_columns
    
    def __getitem__(self, row_col_coord: (int))-> int:
        """
        Gets the value at the specified row and column.

        Args:
            row_col_coord: A tuple containing the row and column indices.

        Returns:
            The value at the specified row and column.
        """

        row = row_col_coord[0]
        col = row_col_coord[1]

        indx = (row * self._num_columns) + col

        return self._data[indx]
    

    def __eq__(self, other: "Matrix")-> bool:
        """
        Checks if two matrices are equal.

        Args:
            other: The other matrix.

        Returns:
            True if the matrices are equal, False otherwise.
        """

        if type(other) != Matrix:
            raise TypeError("input was not a matrix")

        if (self._data == other._data):
            return True
        
        else:
            return False
        

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """
        Adds two matrices.

        Args:
            other: The other matrix.

        Returns:
            The sum of the two matrices.
        """

        if type(other) != Matrix:
            raise TypeError("input was not a matrix")

        if ((self._num_columns != other._num_columns) and (self._num_rows != other._num_rows)):
            raise ValueError("two matrices must have same number of columns and rows")
        
        data_list = []
        for i in range(len(self._data)):
            data_list.append(self._data[i] + other._data[i])

        
        return Matrix(self._num_rows, self._num_columns, data_list)
    

    def transpose(self)-> "Matrix":
        """
        Transposes the matrix.

        Returns:
            The transpose of the matrix.
        """

        

        new_num_columns = self._num_rows
        new_num_rows = self._num_columns

        new_data = [self._data[j * self._num_columns + i] for i in range(self._num_columns) for j in range(self._num_rows)]


        #print(f"New data : {new_data}")

        newMatrix = Matrix(new_num_columns, new_num_rows, new_data)

        return newMatrix
    

    def __mul__(self: 'Matrix', other: 'Matrix')-> 'Matrix':
        """
        Multiplies two matrices.

        Args:
            other: The other matrix.

        Returns:
            The product of the two matrices.
        """

        if self._num_columns != other._num_rows:
            raise ValueError("Number of columns must match number of rows to mupltuply to matrices. ")
        if self._num_rows != other._num_columns:
            raise ValueError("Number of columns must match number of rows to mupltuply to matrices. ")
        if type(other) != Matrix:
            raise TypeError("Input was not a matrix")

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




def main():
    # Test for getNumRows and getNumCols
    matrix1 = Matrix(2, 2, [1, 2, 3, 4])
    print(f"Rows in matrix1: {matrix1.getNumRows()}, Columns in matrix1: {matrix1.getNumCols()}")  # Should be 2, 2

    # Test for ==
    matrix2 = Matrix(2, 2, [1, 2, 3, 4])
    matrix3 = Matrix(2, 2, [4, 3, 2, 1])
    print(f"matrix1 == matrix2: {matrix1 == matrix2}")  # Should be True
    print(f"matrix1 == matrix3: {matrix1 == matrix3}")  # Should be False
    matrix4 = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
    try:
        print(matrix1 == matrix4)  # Should raise TypeError
    except TypeError as e:
        print(f"Expected TypeError: {e}")

    # Test for +
    matrix5 = Matrix(2, 2, [5, 6, 7, 8])
    matrix_sum1 = matrix1 + matrix5
    print(f"matrix1 + matrix5: \n{matrix_sum1}")
    try:
        matrix_sum2 = matrix1 + matrix4  # Should raise ValueError
    except ValueError as e:
        print(f"Expected ValueError: {e}")

    # Test for *
    matrix6 = Matrix(2, 2, [2, 0, 1, 2])
    matrix_product1 = matrix1 * matrix6
    print(f"matrix1 * matrix6: \n{matrix_product1}")
    matrix7 = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
    try:
        matrix_product2 = matrix1 * matrix7  # Should raise ValueError
    except ValueError as e:
        print(f"Expected ValueError: {e}")

        # Test for transpose
    matrix8 = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
    transposed_matrix8 = matrix8.transpose()
    print(f"Original matrix8: \n{matrix8}")
    print(f"Transposed matrix8: \n{transposed_matrix8}")  # Should be a 3x2 matrix with transposed values

    matrix9 = Matrix(3, 1, [7, 8, 9])
    transposed_matrix9 = matrix9.transpose()
    print(f"Original matrix9: \n{matrix9}")
    print(f"Transposed matrix9: \n{transposed_matrix9}")  # Should be a 1x3 matrix with transposed values


if __name__ == "__main__":
    main()




