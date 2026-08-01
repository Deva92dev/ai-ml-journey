# Vector Operations

- In programming, a vector typically refers to a dynamic array, a data structure that stores a sequence of elements of the same type and automatically resizes itself as elements are added or removed

- In mathematics and machine learning, a vector is also an ordered list of scalars
  (e.g., <x, y, z>) used to represent data points, features, or physical quantities with both magnitude and direction.

- Store values as tuple
- Tuples have a slightly smaller memory footprint than lists because they don't need extra space for resizing.
- in case of invalid vector, raise error
- every vector must have repr, addition, multiplication, truediv, rmul, norm, etc

- use len-dunder method to get the length of Vector class
- If there is a empty vector, it must result in error or undefined behavior.

- the asterisk \* is the unpacking operator

- Utility operations
- Where A , B are vectors
- Addition: Dimensions must match
- Subtraction: Dimensions must match
- Scalar Product = n . A
- Cross Product = A x B = |A| |B| Sinθ : Dimensions must match
- Dot Product(Scalar Product) = A ⋅ B = |A| |B| . cosθ : Dimensions must match
- If dot product is zero(what happens)

- dot product produces a scalar value representing the alignment of two vectors. It Measures projection and work.
- the cross product produces a vector perpendicular to the plane of the original two. It Measures perpendicularity and area

# Matrix Operations

- In software, a matrix is a two-dimensional data structure (often called a 2D array) that organizes values into rows and columns. It serves as a compact, efficient container for structured data, such as grid-based images, game boards, or mathematical models.
  - rows of tuple

- Empty, Null Matrices
  - an empty matrix (a tuple of tuple with no rows) is detected by checking if the outer list is empty using len(matrix) == 0 or the boolean evaluation "not matrix"
  - a null matrix (a matrix where all elements are zero) in pure Python without external libraries, you can iterate through the nested list structure to verify that every element equals zero.

- Invalid Matrix
  - An invalid matrix in Python (represented as a tuple of tuples) is detected by ensuring two conditions: every element is a list (checking if the outer structure is a matrix) and all inner lists have the same length (ensuring rectangular consistency)

  - Type Check: Use isinstance(matrix, tuple) to confirm the input is a list.

  - Row Type Check: Verify every element in the outer list is itself a list using isinstance(row, list).
  - Dimension Consistency: Ensure all rows have the same number of elements (e.g., comparing len(row) to len(matrix[0]))

  - Matrix multiplication is impossible when the number of columns in the first matrix does not equal the number of rows in the second matrix

- Accept integers as well as floating point integers(make sure to limit it to 2 places after decimal)

- A matrix is not invertible if it has non-square dimensions, its determinant is 0, zero eigenvalues and zero rows and column.

- Utility operations
- Addition
- Subtraction
- Multiplication
- Transpose
- (Gaussian elimination method)
  - Determinant
  - Identity matrix
  - Inverse
  - Rank
- Eigenvalues and Eigenvectors

# Extensibility

- For each future operation, do this:
  - A normal case.
  - A boundary case.
  - An invalid case.

- Matrix multiplication, Vector and Scalar Operations, Transpose operations will come very handy in Gradient descent and Neural Network projects
