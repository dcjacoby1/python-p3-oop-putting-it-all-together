#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    #property only used for constraints
    #in this case to force int. otherwise, not needed
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    #when called, prints statemenet => needs self arg
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")



    

    
        