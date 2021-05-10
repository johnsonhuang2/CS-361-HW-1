# Author: Dacin Titus
# Date: 4/20/21
# Description: Library simulator with classes for LibraryItem, Patron, and Library.
# Book, Album, and Movie will inherit from LibraryItem.
# Patron's may check out, request, and return LibraryItems.
# Library will keep track of fines for overdue LibraryItems.

"""
LibraryItem:

library_item_id - a unique identifier for a LibraryItem - you can assume uniqueness, you don't have to enforce it
title - cannot be assumed to be unique
location - a LibraryItem can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
checked_out_by - refers to the Patron who has it checked out (if any)
requested_by - refers to the Patron who has requested it (if any); a LibraryItem can only be requested by one Patron at a time
date_checked_out - when a LibraryItem is checked out, this will be set to the current_date of the Library
init method - takes a library item ID and title; checked_out_by and requested_by should be initialized to None;
a new LibraryItem's location should be on the shelf
get_location returns the Library Item's location
other get and set methods as needed
"""

class LibraryItem:
    """A class to be inherited by Book, Album, and Movie"""
    def __init__(self, library_item_id, title):
        """
        Creates an object with an id and title;
        initializes checked_out_by and requested_by to None;
        location initialized to ON_SHELF.
        """
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        self._date_checked_out = None

    def get_library_item_id(self):
        """returns library item id"""
        return self._library_item_id

    def set_library_item_id(self, new_library_item_id):
        """sets a new library item id"""
        self._library_item_id = new_library_item_id

    def get_title(self):
        """returns title"""
        return self._title

    def set_title(self, new_title):
        """sets a new title"""
        self._title = new_title

    def get_checked_out_by(self):
        """returns which Patron has checked out the item"""
        return self._checked_out_by

    def set_checked_out_by(self, patron):
        """sets the patron as who the item is checked out by"""
        self._checked_out_by = patron

    def get_requested_by(self):
        """returns which Patron has requested the item"""
        return self._requested_by

    def set_requested_by(self, patron):
        """sets the patron as who the item is requested by"""
        self._requested_by = patron

    def get_location(self):
        """returns the location of the item"""
        return self._location

    def set_location(self, new_location):
        """sets the new location for the item"""
        self._location = new_location

    def date_checked_out(self, current_date):   # calls current_date from Library class
        """sets to the current_date of the Library class"""
        self._date_checked_out = current_date


class Book(LibraryItem):
    """
    represents a Book object which inherits from LibraryItem and adds fields for
    checkout length and author
    """
    def __init__(self, library_item_id, title, author):
        """
        creates a Book object that inherits id and title from LibraryItem;
        takes additional parameter for author;
        initializes check out length to 21
        """
        super().__init__(library_item_id, title)
        self._author = author
        self._check_out_length = 21

    def get_author(self):
        """returns the author"""
        return self._author

    def get_check_out_length(self):
        """returns the check out length"""
        return self._check_out_length


class Album(LibraryItem):
    """
    represents an Album object which inherits from LibraryItem and adds fields for
    checkout length and artist
    """
    def __init__(self, library_item_id, title, artist):
        """
        creates an Album object that inherits id and title from LibraryItem;
        takes additional parameter for artist;
        initializes check out length to 14
        """
        super().__init__(library_item_id, title)
        self._artist = artist
        self._check_out_length = 14

    def get_artist(self):
        """returns the artist"""
        return self._artist

    def get_check_out_length(self):
        """returns the check out length"""
        return self._check_out_length


class Movie(LibraryItem):
    """
    represents a Movie object which inherits from LibraryItem and adds fields for
    checkout length and author
    """
    def __init__(self, library_item_id, title, director):
        """
        creates a Movie object that inherits id and title from LibraryItem;
        takes additional parameter for director;
        initializes check out length to 7
        """
        super().__init__(library_item_id, title)
        self._director = director
        self._check_out_length = 7

    def get_director(self):
        """returns the director"""
        return self._director

    def get_check_out_length(self):
        """returns the check out length"""
        return self._check_out_length


class Patron:
    """
    represents a Patron with an id and name;
    collection of items checked out by Patron;
    how much the Patron owes in late fees
    """
    def __init__(self, patron_id, name):
        """
        creates Patron object with id and name;
        initializes checked out items to an empty list;
        initializes fine amount to 0
        """
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self):
        """returns patron id"""
        return self._patron_id

    def get_name(self):
        """returns patron's name"""
        return self._name

    def get_checked_out_items(self):
        """returns the patron's checked out items"""
        return self._checked_out_items

    def get_fine_amount(self):
        """returns the fine amount"""
        return self._fine_amount

    def add_library_item(self, library_item):   # uses LibraryItem object as parameter
        """appends a LibraryItem object to list of checked out items"""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):   # uses LibraryItem object as parameter
        """removes a LibraryItem object from list of checked out items"""
        self._checked_out_items.remove(library_item)

    def amend_fine(self, change_in_fine):
        """
        subtracts new_fine from the current fine amount;
        if new_fine is negative, this will cause it to add it instead
        """
        self._fine_amount += change_in_fine


class Library:
    """
    represents a Library with a collection of LibraryItems that belong to the Library,
    a collection of Patrons who are members;
    keeps track of the current date;
    allows lookup of LibraryItems and Patrons;
    allows checkout, request, and return of LibraryItem;
    allows Patron to pay a fine;
    increments the current date and calculates Patron's fines for each overdue LibraryItem they have checked out
    """
    def __init__(self):
        self._holdings = {}
        self._members = {}
        self._current_date = 0

    def get_current_date(self):
        return self._current_date

    def add_library_item(self, library_item):
        """takes a LibraryItem object and adds it to the holdings"""
        self._holdings[library_item.get_library_item_id()] = library_item

    def add_patron(self, patron):
        """takes a Patron object and adds it to the members"""
        self._members[patron.get_patron_id()] = patron

    def lookup_library_item_from_id(self, library_item_id):
        """
        returns LibraryItem object corresponding to the ID parameter,
        or returns None if no such item is in the holdings
        """
        if library_item_id in self._holdings:
            return self._holdings[library_item_id]
        else:
            return None

    def lookup_patron_from_id(self, patron_id):
        """
        returns the Patron Object corresponding to the ID parameter,
        or returns None if no such Patron is a member
        """
        if patron_id in self._members:
            return self._members[patron_id]
        else:
            return None

    def check_out_library_item(self, patron_id, library_item_id):
        """
        return "patron not found" if specified Patron is not in members;
        return "item not found" if specified LibraryItem is not in holdings;
        return "item on hold by another patron" if specified LibraryItem is on hold by other Patron;
        otherwise: update LibraryItem's checked out by, date checked out, and location;
        if LibraryItem was on hold for this Patron, update requested by;
        update Patron's checked out items
        return "check out successful"
        """
        if patron_id not in self._members:
            return "patron not found"
        if library_item_id not in self._holdings:
            return "item not found"

        library_item_object = self._holdings[library_item_id]
        patron_object = self._members[patron_id]
        if library_item_object.get_location() == "ON_HOLD_SHELF" and library_item_object.get_requested_by() is not patron_object:
            return "item on hold by other patron"
        if library_item_object.get_location() == "CHECKED_OUT":
            return "item already checked out"


        library_item_object.set_checked_out_by(patron_object)
        library_item_object.date_checked_out = self._current_date
        library_item_object.set_location("CHECKED_OUT")

        if library_item_object.get_requested_by() == patron_object:
            library_item_object.set_requested_by(None)

        patron_object.add_library_item(library_item_object)

        return "check out successful"

    def return_library_item(self, library_item_id):
        """
        return "item not found" if LibraryItem not in holdings;
        return "item already in library" if LibraryItem is not checked out;
        update Patron's checked out items;
        update LibraryItem's location
        update LibraryItem's checked out by;
        return "return successful"
        """
        if library_item_id not in self._holdings:
            return "item not found"

        library_item_object = self._holdings[library_item_id]
        if library_item_object.get_location() != "CHECKED_OUT":
            return "item already in library"

        patron_object = library_item_object.get_checked_out_by()
        patron_object.remove_library_item(library_item_object)

        if library_item_object.get_requested_by() is None:
            library_item_object.set_location("ON_SHELF")
        elif library_item_object.get_requested_by() is not None:
            library_item_object.set_location("ON_HOLD_SHELF")

        return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """
        return "patron not found" if specified Patron not in members;
        return "item not found" if specified LibraryItem not in holdings;
        return "item already on hold" if specified LibraryItem is already requested;
        update LibraryItem's requested by;
        if LibraryItem is on shelf, update location to on hold
        return "request successful"
        """
        if patron_id not in self._members:
            return "patron not found"
        if library_item_id not in self._holdings:
            return "item not found"

        patron_object = self._members[patron_id]
        library_item_object = self._holdings[library_item_id]

        if library_item_object.get_requested_by() is not None:
            return "item already on hold"

        library_item_object.set_requested_by(patron_object)

        if library_item_object.get_location() == "ON_SHELF":
            library_item_object.set_location("ON_HOLD_SHELF")


        return "request successful"

    def pay_fine(self, patron_id, change_in_fine):   # change in fine should be negative since patron is paying
        """
        return "patron not found" if specified patron not in members;
        use amend fine to update patron's fine, return "payment successful"
        """
        if patron_id not in self._members:
            return "patron not found"

        patron_object = self._members[patron_id]
        change_in_fine = abs(change_in_fine)
        change_in_fine = float(-change_in_fine)
        patron_object.amend_fine(change_in_fine)

        return "payment successful"

    def increment_current_date(self):
        """
        increments current date;
        increase Patron's fines by 10 cents for each overdue LibraryItem they have checked out
        """
        self._current_date += 1
        for patron in self._members.values():
            for my_items in patron.get_checked_out_items():
                date_difference = self._current_date - my_items.date_checked_out
                if date_difference > 0:
                    check_out_length = str(my_items.get_check_out_length())
                    check_out_length = float(check_out_length)
                    if date_difference - check_out_length > 0:
                        new_fine = 0.10
                        patron.amend_fine(new_fine)


b1 = Book("1234", "Slaughterhouse Five", "Vonnegut")
b2 = Book("2345", "Hamlet", "Shakespeare")
a1 = Album("3456", "Gyotaku", "GO!GO!7188")
a2 = Album("4567", "2001", "Dr. Dre")
m1 = Movie("5678", "The Incredibles", "Bird")
m2 = Movie("6789", "Jurassic Park", "Spielberg")
book_patron = Patron("abc", "Felicity")
album_patron = Patron("bcd", "Ralph")
movie_patron = Patron("cde", "Waldo")
combined_patron = Patron("def", "Emerson")
lib = Library()
lib.add_library_item(b1)
lib.add_library_item(b2)
lib.add_library_item(a1)
lib.add_library_item(a2)
lib.add_library_item(m1)
lib.add_library_item(m2)
lib.add_patron(book_patron)
lib.add_patron(album_patron)
lib.add_patron(movie_patron)
lib.add_patron(combined_patron)
lib.check_out_library_item("abc", "1234")
lib.check_out_library_item("bcd", "3456")
lib.check_out_library_item("cde", "5678")
lib.check_out_library_item("def", "2345")
lib.check_out_library_item("def", "4567")
lib.check_out_library_item("def", "6789")