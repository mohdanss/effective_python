'''
Item 2: Follow the PEP 8 Style Guide
Python Enhancement Proposal #8, otherwise known as PEP 8, is the style guide for how to
format Python code.
Here are a few rules you should be sure to follow:

Whitespace: 
In Python, whitespace is syntactically significant. Python programmers
are especially sensitive to the effects of whitespace on code clarity.
 - Use spaces instead of tabs for indentation.
 - Use four spaces for each level of syntactically significant indenting.
 - Lines should be 79 characters in length or less.
 - Continuations of long expressions onto additional lines should be indented 
    by four extra spaces from their normal indentation level.
 - In a file, functions and classes should be separated by two blank lines.
 - In a class, methods should be separated by one blank line.
 - Don’t put spaces around list indexes, function calls, or keyword argument
    assignments.
 - Put one—and only one—space before and after variable assignments.

Naming: 
PEP 8 suggests unique styles of naming for different parts in the language.
This makes it easy to distinguish which type corresponds to each name when 
reading code.
 - Functions, variables, and attributes should be in lowercase_underscore 
    format.
    Example:
        def my_function():
            pass
            
 - Protected instance attributes should be in _leading_underscore format.
 - Private instance attributes should be in __double_leading_underscore
    format.
    Example:
        class MyClass:
            def __init__(self, value):
                self.__private_value = value # Private instance attribute
                self._protected_value = value # Protected instance attribute
                self.public_value = value # Public instance attribute

 - Classes and exceptions should be in CapitalizedWord format.
    Example:
        class MyException(Exception):
            pass
            
 - Module-level constants should be in ALL_CAPS format.
    Example:    
        MY_CONSTANT = 1

 - Instance methods in classes should use self as the name of the first 
    parameter (which refers to the object).
 - Class methods should use cls as the name of the first parameter 
    (which refers to the class).

    Example:
        class MyClass:
            # I am available to all instances of MyClass
            class_variable = "I am a class variable" 

            def __init__(self, instance_variable):
                # I am available to only this instance of MyClass
                self.instance_variable = instance_variable

            def instance_method(self):
                print(f"Instance variable: {self.instance_variable}")
                # Accessing class variable inside instance method
                print(f"Class variable: {self.class_variable}")
            
            @classmethod
            def class_method(cls):
                print(f"Class variable: {cls.class_variable}")

    Point to Ponder:
    - What do we need class_method for? Why can't we just use instance_method?
        Let's say you have a class called Employee. You create two instances of Employee
        called emp1 and emp2. Now, if you change the value of class variable company_name
        using emp1, the value of company_name will change for both emp1 and emp2. But, if
        you change the value of instance variable name using emp1, the value of name will
        change only for emp1 and not for emp2. This is because class variables are shared
        by all instances of a class. This is why we need class methods. Class methods
        can access and modify class variables. Instance methods can access and modify
        instance variables.

Expressions and Statements: 
 - Use inline negation (if a is not b) instead of negation of positive expressions
(if not a is b).
 - Don’t check for empty values (like [] or '') by checking the length (if
    len(somelist) == 0). Use if not somelist and assume empty values implicitly 
    evaluate to False.
 - The same thing goes for non-empty values (like [1] or 'hi'). The statement 
    if somelist is implicitly True for non-empty values.
 - Avoid single-line if statements, for and while loops, and except compound
    statements. Spread these over multiple lines for clarity.
 - Always put import statements at the top of a file.
 - Always use absolute names for modules when importing them, not names 
    relative to the current module’s own path. For example, 
    to import the foo module from the bar package, you should do:
    from bar import foo, not just import foo.
 - If you must do relative imports, use the explicit syntax from . import foo.
 - Imports should be in sections in the following order: 
    standard library modules, thirdparty modules, your own modules. 
    Each subsection should have imports in alphabetical order.

Things to Remember:
- Always follow the PEP 8 style guide when writing Python code.
- Sharing a common style with the larger Python community facilitates 
    collaboration with others.
- Using a consistent style makes it easier to modify your own code later
'''
