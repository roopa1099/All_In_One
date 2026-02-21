## Python Notes

1. When a variable is float it can store upto 16 decimal point
2. Difference between '', "", ''' ''' -> Normally we use ''(single), but when we need to use ' in our string like, wasn't kind of words we can use "". But if our string contains both "" and ' then we use ''' to help python to know what is the actual start and end of string.
3. We can also have it in '' like 'I wasn\ 't planning to go out'
4. \n -> next line. \t is white space


5. Strings, List, Set, Dicstionaries, Tuples
6. Strings: Immutable
7. Slicing : substring of a string
8. List: Mutable
9. Tuple: Immutable, [preferred for data that does not change]
10. Set : No duplicates, unordered in memory level hence no slicing is possible
11. input() will save value in string format
12. In Python, slicing for lists and tuples (and other sequence types like strings) uses a left-inclusive, right-exclusive system. 
13. Floor division is a division operation that returns the largest integer that is less than or equal to the result of the division, mean always integer
14. and, or is logical operator
15. zip : function to iterate multip-le list simultaneously(The shortest list wins.)
16. List comprehension => itertaing in list inf single line
17. shallow copy : you point to exisitng array, where as in deep copy you create a new copy of array in new memory location


[ ## Class and object ](classes.py)
9. self inside a method, is we are passing the particular instance of object. The method can only be called by the instance of the class.
10. Unlike Java where instance variables must be explicitly declared in the class body, Python allows dynamic creation of instance variables by assigning them in methods like __init__ without prior declaration. 
11. In Python, instance methods (like display) always require self as the first parameter to access instance variables (e.g., self.id). You cannot declare or assign instance variables "explicitly" at the class level like in Java and access them in methods without self—Python doesn't support that syntax.
12. Class variables (declared at the class level, outside methods) are shared across all instances of the class—they are not copied or duplicated per instance.
Same as static variable of a class in java.
13. In Python, all variables declared at the class level (outside methods) are class variables by default, which behave like static variables in Java—they are shared across all instances.
14. The pass keyword in Python is a null operation placeholder. It does nothing when executed but is syntactically required in contexts where a statement is expected.
15. In python  __init__(self, variables) is constructor
16. Instance methods: Require an object and automatically receive self.
17. Class methods (@classmethod): Accessed via the class (e.g., MyClass.class_method()) and receive cls. @classmethod methods cannot directly access instance variables
18. Static methods (@staticmethod): Accessed via class or object (e.g., MyClass.static_method() or obj.static_method()) and receive no implicit first argument.
@staticmethod methods can access class variables, but only by explicitly referencing the class name (e.g., MyClass.class_var). They cannot access instance variables at all, as they have no instance context.
19. in Python, class-level variables (which behave like static variables) are defined outside methods (at the class level) and are initialized once when the class is first loaded/defined, not during object creation in __init__
20. tatic methods (@staticmethod) are pure utility functions with no self or cls, unable to access class/instance state directly. Utility functions related to the class but not needing class context (e.g., helper calculations).
Code organization (grouping related functions in a class namespace). Used only when we r not modifying any class/instance variable, but logically belongs to a class



[## OOP Properties](./oop.py)
21. Inheritance
22. Abstraction: The practice of hiding internal implementation details and showing only the essential features of an object or system.
23. @abstractmethod only enforces implementation when the base class is an ABC.
24. Encapsulation: In many languages, this is enforced through access modifiers like private, protected, and public, which strictly control what can and cannot be accessed from outside the class. However, Python does not have true encapsulation in this sense.
Instead, developers are trusted to follow naming conventions to indicate private or protected attributes (like using a leading underscore _var), but the language doesn't enforce access restrictions. 

Public: attribute or method – Accessible everywhere.
Protected: _attribute (single underscore) – Convention indicating internal use; not enforced, but signals "use at your own risk."
Private: __attribute (double underscore) – Name mangling occurs (e.g., __attr becomes _ClassName__attr), making it harder to access accidentally, but still accessible.


[ ## Numpy ](numpy_array.py)
25. NumPy array : accepts data of one type, whereas a single list can accept data of different types
26. can’t have arrays of varying sizes within the same dimension of a NumPy array,
27. Properties: Elememt-wise properties, Vectorisation, broadcasting(eaqsily perform operation on numpy list with different sizes), easy to reshape, transform
28. Fancy indexing
29. Numpy are primarily designed for numerical data and perform best when the entire array contains a single, homogeneous data type (e.g., an array entirely of 64-bit floating-point numbers or an array of integers) [2, 3]. While you can force a NumPy array to store mixed data types by using dtype=object, this approach is generally inefficient and less common
30. you can change the dimensions of an array by directly assigning a new tuple to its .shape attribute.
31. Slicing a NumPy array returns a view of the original array,
32. np.append() function never modifies the original array in place

## Panda series
30. OPanda series can also store any type of data.
31. Panda series is built over numpy to have control over labelled data
32. Default datatype of empty series in 0
33. Panda series are strictly one dimensional(In pandas, "one-dimensional" refers to the structure of the Series (the index system))
34.  pandas uses hashing to optimize label-based lookups, but its behavior changes depending on the state of the index
35. Immutable Labels: This is the reason why labels in a pandas index must be hashable (immutable). Types like strings, integers, and tuples work, but lists do not.
36. .fillna() method to fill NaN values in any series.
37. Identify entries which have NaN values using the .isna() or .isnull() methods, and drop NaN values with the .dropna() method
38. Reset the index of a series to have a simple numeric index from 0 onwards, you can use the .reset_index() method. This will create a DataFrame.
39. .sort_values() method sorts a Series by its actual data (values), not by its index labels.
40. While .describe() focuses on numeric columns by default, it can also analyze non-numerical data like strings (objects), booleans, and timestamps. 
For Object/Categorical data: It provides different metrics: count, unique, top (the most frequent value), and freq (the frequency of the top value).
For Timestamps: It additionally provides the first and last dates in the Series. 


## Dataframe
41. Dataframes h have labeled row and cokumn
42. Can have multiple datatype in each frame.
43. Each column is a Pandas Series, so it can have different data types per column.
44. Loading file with pd : nrows => loads only rows ghiven. header() loads all but displays ony require
45. If there are duplicate values for a given combination of index and columns, the .pivot() method will raise an error.
46. pivot(): If there are duplicate values for a given combination of index and columns, the .pivot() method will raise an error. Reshapes data from long format → wide format
47. The palette parameter in lineplot() is used to control the colour scheme for multiple categories, not the line styles. To control line styles, you should use the style parameter.
48. idxmin() : Returns the index (label) of the minimum value
49. zip(names, ages) → creates tuples:,  When data comes as separate lists
50. Line Plot: Line plots are used to show trends over time or ordered data.
The x-axis usually represents time or sequence, and the y-axis represents the measured value. Line plots help identify increases, decreases, and patterns over time.
51. Bar Plot: Bar plots are used to compare categorical data.
The x-axis represents different categories, and the y-axis represents a numeric value such as count, sum, or average. Bar plots make it easy to compare values across categories.
52. Histogram: Histograms are used to visualize the distribution of continuous numerical data.(count or frequncy distribution in certain groups)
The x-axis represents value ranges (bins), and the y-axis represents the frequency or density of observations within each range. Histograms help understand data spread and skewness.
53. Count plot: Count/frequency Distributionn for categorical data
53. Box Plot: Box plots are used to summarize the distribution of numerical data.
They display the median, quartiles, and outliers. Box plots are useful for comparing distributions across different categories and identifying extreme values.
54. Scatter Plot: Scatter plots are used to analyze the relationship between two numerical variables.
Each point represents an observation, with its position determined by x- and y-values. Scatter plots help identify correlations, trends, and clusters.
55. Pie Chart: Pie charts are used to show proportions or percentages of a whole.
Each slice represents a category’s contribution to the total. Pie charts are best used when there are only a few categories.
56. Area Plot: Area plots are used to show cumulative values over time.
They are similar to line plots but with the area filled under the line, making them useful for visualizing contributions to a total over time.
57. Barh (Horizontal Bar Plot): Horizontal bar plots are used to compare categories when category names are long.
The y-axis represents categories, and the x-axis represents the numeric value.
58. Line Graph: Line graphs are used to visualize trends and changes over time or ordered data.
The x-axis typically represents time or sequence, while the y-axis represents the measured value. Line graphs help identify upward or downward trends, seasonality, and fluctuations.
59. Pair Plot: Pair plots are used to visualize relationships between multiple numerical variables simultaneously.
They display scatter plots for each pair of variables and histograms or density plots on the diagonal. Pair plots are useful for identifying correlations, patterns, and potential outliers in multivariate data.
60. Heat Map: Heat maps are used to represent data values using colors. To show coprrelation, it only visualizes, not calculating
Rows and columns represent variables or categories, and the color intensity indicates the magnitude of values. Heat maps are commonly used to visualize correlation matrices, patterns, and concentration of values.
61. The primary purpose of pd.cut() in Pandas is to convert continuous numerical data into discrete intervals (bins).
Raw numerical data like:

23, 27, 35, 41, 58, 62


is often hard to analyze categorically.

pd.cut() converts this into:

20–30, 30–40, 40–50, 50–60, 60+


