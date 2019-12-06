from num2words import num2words

class Fibo:
    """
    Class for displaying Fibonacci sequence
    """
    # Starting with immutable data
    results = None
    iterations = None
    to_words = None

    def fibonacci_to_degree(self, degree):
        """
        Function to display fibonacci sequence up to a specific degree
        """
        # If the degree is less than or equal to 1, return degree
        if degree <= 1:
            return degree
        else:
            # Otherwise return (degree - 1) + (degree - 2)
            calc = (self.fibonacci_to_degree(degree-1) + self.fibonacci_to_degree(degree-2))
            return calc

    def loop_iterations(self):
        """
        Iterates over the range of iterations
        """
        # Iterate over iterations
        for i in range(self.iterations):
            # If to_words is True, print number and number to word
            if self.to_words:
                # Get the result of the function
                result = self.fibonacci_to_degree(i)
                # Print a formatted string for number - number to string
                # Example (1 - One)
                print("{} - {}".format(result,num2words(result)))
            else:
                print(self.fibonacci_to_degree(i))

    def __init__(self, degree, to_words=True):
        """
        Constructor method to make an execute data
        """

        # Raise if degree is not a number
        if not isinstance(degree, int):
            raise TypeError('degree must be an int')
        # Raise if degree is less than or equal to 0
        if degree <= 0:
            raise ValueError('degree must be positive')

        # Switch for displaying numbers to words
        self.to_words = to_words

        # Initialize lists
        self.iterations = degree
        self.results = []

        # Start loop_iterations
        self.loop_iterations()
