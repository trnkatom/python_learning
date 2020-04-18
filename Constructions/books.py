class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class Bookcase:
    def __init__(self, books=None):
        self.books = books

    ''' 
     - 'CONSTRUCTICON' --> class method which is used as alternative constructor! Usually defines a method which encapsulates some logic and in return statement creates an instance of its class via: cls(params)
     - because its marked as @classmethod, we call this method from a Class, not an instance! Bookcase.create_bookcase() , NOT bookcase.create_bookcase()
    '''
    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        # book_list can be any type of iterable, which contains two-item iterables = tuple of tuples / list of tuples / tuple of lists ; if it's not then there will be an error raised
        # store the first value into 'title', second value into 'author', create Book instance using these values and add them to the books[] list
        # finally create standard (__init__) instance of Bookcase, passing books[] as argument
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)

    # another constructicon; does not take any arguments; creates mocked books which is then used to create the bookcase instance
    @classmethod
    def create_bookcase_mockdata(cls):
        books = []
        for number in range(3):
            title = "title" + str(number)
            author = "author" + str(number)
            books.append(Book(title, author))
        return cls(books)

# creating Bookcase instance via classmethod with LIST of TUPLES as argument
bc = Bookcase.create_bookcase([('Book1','Tomas Trnka'),('Book2','Ivan Trnka'),('Book3','Martin Pergl')])
# creating Bookcase instance via classmethod with TUPLE of TUPLES as argument
bc2 = Bookcase.create_bookcase((('Book1','ABC'),('Book2','DDD'),('Book3','EEE')))
# creating Bookcase instance via classmethod with TUPLE of LISTS as argument
bc3 = Bookcase.create_bookcase((['Book1','X'],['Book2','Y'],['Book3','Z']))
# creating Bookcase instance via classmethod with no argument; returns mocked data specified in classmethod definition
bc4 = Bookcase.create_bookcase_mockdata()
