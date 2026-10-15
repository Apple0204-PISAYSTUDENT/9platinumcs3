
"""
SG 9 - Inheritance
Formative Assessment No. 1: Library Management System

Demonstrates inheritance, encapsulation, getters, setters,
and data validation.
"""


class Publication:
    """Parent class for common publication information."""

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    # Setters
    def set_title(self, title):
        if isinstance(title, str) and title.strip():
            self.__title = title
        else:
            print("The title cannot be empty.")

    def set_author(self, author):
        if isinstance(author, str) and author.strip():
            self.__author = author
        else:
            print("The author cannot be empty.")

    def display_info(self):
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")


class Book(Publication):
    """Child class representing a book."""

    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = None
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        # Page counts must be positive integers.
        if (
            isinstance(number_of_pages, int)
            and not isinstance(number_of_pages, bool)
            and number_of_pages > 0
        ):
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")

            # Give a newly created object a valid fallback value.
            if self.__number_of_pages is None:
                self.__number_of_pages = 1

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.get_number_of_pages()}")


class Magazine(Publication):
    """Child class representing a magazine."""

    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        # Issue numbers must be positive integers.
        if (
            isinstance(issue_number, int)
            and not isinstance(issue_number, bool)
            and issue_number > 0
        ):
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

            # Keep the object valid even if its initial value is invalid.
            if self.__issue_number is None:
                self.__issue_number = 1

    def display_info(self):
        super().display_info()
        print(f"Issue number: {self.get_issue_number()}")


def main():
    # Create two Publication objects.
    publication1 = Publication(
        "Introduction to Computer Science",
        "Alex Morgan"
    )
    publication2 = Publication(
        "Journal of Experimental Psychology",
        "Ratcliff and Van Dongen"
    )

    # Create two Book objects.
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    book2 = Book("The Little Prince", "Antoine de Saint-Exupery", 96)

    # Create two Magazine objects.
    magazine1 = Magazine("National Geographic", "Various Authors", 202)
    magazine2 = Magazine("Science Monthly", "Editorial Team", 18)

    # Display Publication information.
    print("=== PUBLICATION INFORMATION ===")
    publication1.display_info()
    print()
    publication2.display_info()

    # Display Book information.
    print("\n=== BOOK INFORMATION ===")
    book1.display_info()
    print()
    book2.display_info()

    # Display Magazine information.
    print("\n=== MAGAZINE INFORMATION ===")
    magazine1.display_info()
    print()
    magazine2.display_info()

    # Test validation using invalid values.
    print("\n=== VALIDATION TEST ===")

    book1.set_number_of_pages(-310)
    print(
        "Book page count after invalid update:",
        book1.get_number_of_pages()
    )

    magazine1.set_issue_number(0)
    print(
        "Magazine issue number after invalid update:",
        magazine1.get_issue_number()
    )


if __name__ == "__main__":
    main()
