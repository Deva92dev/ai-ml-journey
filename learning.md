- To return the single book object, use next() with a generator expression to extract the first match
- If you are returing many values from a function, they are in tuple you can not add them like normal variables, you have to unpack them and then yo can perform operations on any single one of them.

- The ChainedAssignmentError occurs because you are using inplace=True on a Series created by indexing (df["Age"]), which behaves as a copy under pandas' Copy-on-Write mode