## Here are all the functions and classes to run the system. 
## Please, if you don't know how works Python, don't touch anything !

init python:
    import collections

## This class lets the dev create some events for his game. By default, all the events have the 
## pending state and are hidden.
    class Quest:
        def __init__(self, id, title, category,  state= "pending"):
            self.id = id
            self.title = title
            self.category = category
            self.state = state

        def __repr__(self):
            return "<{}>".format(self.title)





## This class allows the developer to perform various operations on the events
    class Manager:

        def __init__(self):
            self.quests_dict = collections.OrderedDict() ## The place where are loaded the events 
            self.states = ["pending", "unlocked", "in progress", "completed", "done", "failed", "canceled"]


#_______Loading and deleting chapter into the manager_______________

        ## Load the chapter into the manager memory
        def load(self, chapter):
            if type(chapter) is not tuple:
                print("Error: must be a tuple")
                renpy.quit()
            self.quests_dict.clear()
            for quest in chapter:
                if quest.category not in self.quests_dict:
                    self.quests_dict[quest.category] = collections.OrderedDict([(quest.id,quest)])
                else:
                    self.quests_dict[quest.category][quest.id] = quest
            self._reload_screen("diary")
            renpy.block_rollback()
            print(self.quests_dict)


        ## Delete the chapter from the manager memory
        def free(self):
            self.quests_dict.clear()
            renpy.block_rollback()



#____________Search functions to find some events______________

        def _search(self, id, category = ""):
            if category == "":
                return self._searchID(id)
            return self.quests_dict[category][id]


        def _searchID(self, id):
            for k in self.quests_dict.keys():
                if id in self.quests_dict[k]:
                    return self.quests_dict[k][id]



#____________Functions to do some tests_____________________

        ## Return True if the category exists in the chapter
        def exists(self, id, category = ""):
            if self._search(id, category):
                return True
            return False


        ## Return the category
        def is_in(self, id):
            for k in self.quests_dict.keys():
                if id in self.quests_dict[k]:
                    return k


        ## Return True if the ID has the right state
        def is_state(self, id, state, category = ""):
            if self._search(id, category).state == state:
                return True
            return False

        ## Return True if all the events of a category are done
        def is_category_over(self, category):
            for v in self.quests_dict[category].values():
                if v.state != "done":
                    return False
            return True

        ## Return True if all the events from all the categories are done
        def is_chapter_over(self):
            for k in self.quests_dict.keys():
                if not self.is_category_over(k):
                    return False
            return True


#_____________Some functions to change the state of quests__________________

        ## Check if the event has the right state, otherwise it is updated
        def check(self, id, state, category = ""):
            if state not in self.states:
                print("Error: this state doesn't exist ! Please check the documentation.")
                return
            if category == "" and state != "canceled":
                self._checkID(id, state)
                return
            if state == "canceled":
                self._remove_quest(id)
                return
            self._search(id, category).state = state
            print("{} {}".format(id ,self._search(id, category).state))
            

        ## Private function to find an event by his ID
        def _checkID(self, id, state):
            self._searchID(id).state = state



        def update(self, id="", state="", unchanged = [], category=""):
            temp = False
            if isinstance(id, tuple):
                id1, id2 = id
            else:
                id1, id2 = id, id
                temp = True
            if isinstance(state, tuple):
                state1, state2 = state
            else:
                state1, state2 = state, state

            if category == "" and id != "":
                category = self._searchID(id2).category  

            if id == "" and category != "":
                self._update_all_quests(state, unchanged, category)
                return

            for k,v, in self.quests_dict[category].items():
                if k == id1:
                    temp = True 
                if k == id2:
                    v.state = state2
                    return
                if temp == True:
                    if v.state not in unchanged:
                        v.state = state1


        def _update_all_quests(self, state="", unchanged = [], category=""):
            for k,v, in self.quests_dict[category].items():
                if v.state not in unchanged:
                    v.state = state


#_____________Add or remove categories from the chapter___________

        ## Add a new category into the chapter during the game 
        ## The added categories will not be stored when the chapter is freed
        def add(self, quests):
            if type(quests) is list:
                self._add_multi(quests)
                return
            if self.exists(quests.id):
                print("Error: already in quests_dict")
                return
            if quests.category not in self.quests_dict:
                self.quests_dict[quests.category] = collections.OrderedDict([(quests.id,quests)])
            else:
                self.quests_dict[quests.category][quests.id] = quests


        def _add_multi(self, quest_list):
            for quest in quest_list:
                self.add(quest)

        ## Remove a category from the category
        def remove(self, category):
            if category not in self.quests_dict:
                return
            del self.quests_dict[category]
            self._reload_screen("diary")


        def _remove_quest(self, id, category = ""):
            if category == "":
                category = self.is_in(id)
            del self.quests_dict[category][id]
            if self.quests_dict[category] == {}:
                del self.quests_dict[category]



        ## If a category is deleted and the log is open, you have to reload the screen
        def _reload_screen(self, screen_name):
            if renpy.get_screen(screen_name):
                renpy.hide_screen(screen_name)
                renpy.show_screen(screen_name)
