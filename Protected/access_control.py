class Protected:
    # methods/functions which starts with single _ are not ment to be used! (just a convention)
    def _dont_use(self):
        pass

    # attributes/methods/functions starting with double __ are protected and cannot be reached/used outside of the class
    __name = "Security"
    def __method(self):
        return self.__name


prot = Protected()
# raises AttributeError: 'Protected object has no attribute '__name' -> because of the double __ I cannot access them directly by their name
try:
    print(prot.__name)
except AttributeError as err:
    print(err)

try:
    prot.__method()
except AttributeError as err:
    print(err)

# I can access protected attributes and methods via _Protected keyword
print(dir(prot))
print(prot._Protected__name)
prot._Protected__method()