from random import shuffle

class FlashCard(object):
    def __init__(self, name, ans):
        self.name=name
        self.ans=ans

    def check(self, kind,  val):
        #This will ask the quesiton and display the answer when user hits "Enter"
        #kind is a String that names what is asked for in the question
        #val is the answer
        resp=input("What is the {} of {}?".format(kind, self.name))
        while self.name==self.name:
            print("The answer is:\n{}".format(val))
            print("You wrote:\n\"{}\"".format(resp))
            resp2=input("Were you correct? [Y/N]")
            if resp2=="Y":
                return True
            elif resp2=="N":
                return False
            else:
                print("Invalid Response\nWhat is the {} of {}?".format(kind, self.name))

class Muscle (FlashCard):
    def __init__(self, name, origin, insert, action, nerve, notes):
        self.name=name#muscle name
        self.origin=origin#Muscle Origin
        self.insert=insert#Muscle Insertion
        self.action=action#Muscle Actions
        self.nerve=nerve#Muscle Innervation
        self.notes=notes#whatever errata relate to muscle (muscle bellies, multiple innervations, variability, etc.)
        self.score={"Origin":0,"Insertion":0,"Action":0,"Innervation":0}#Keeps track of how one is doing.
    
    def __str__(self):
        return("{} Muscle. Query [Muscle Name].info() for more information".format(self.name))
    
    def __repr__(self):
        #For Brevity, this is not a full declaration
        return("Muscle({}, {}, {})".format(self.name, self.origin[0], self.insert[0]))
    
    def eval(self):
        print("Your score for {}'s Origin is: {}".format(self.name, self.score[0]))
        print("Your score for {}'s Insertion is: {}".format(self.name, self.score[1]))
        print("Your score for {}'s Action is: {}".format(self.name, self.score[2]))
        print("Your score for {}'s Innervation is: {}".format(self.name, self.score[3]))
    
    def info(self):
        print("\nThis Muscle is {}. \nIt originates on the {} of the {}.".format(self.name, self.origin[1], self.origin[0]))
        print("It inserts on the {} of the {}.".format(self.insert[1], self.insert[0]))
        print("\nThe Action(s) listed for the {} is/are:".format(self.name))
        print("\n".join(self.action))
        print("\n{} is Innervated by:".format(self.name))
        if isinstance(self.nerve, str):
            print(self.nerve)
        else:
            print("\n".join(self.nerve))
        if self.notes is not None:
            print("\nExtra notes about {} are as follows:".format(self.name))
            print(self.notes)
    
    def test_origin(self):
        ans=self.check("Origin", self.origin)
        if ans:
            self.score["Origin"]+=1
        else:
            self.score["Origin"]-=1
    
    def test_insert(self):
        ans=self.check("Insertion", self.insert)
        if ans:
            self.score["Insertion"]+=1
        else:
            self.score["Insertion"]-=1
    
    def test_action(self):
        ans=self.check("Action", self.action)
        if ans:
            self.score["Action"]+=1
        else:
            self.score["Action"]-=1
    
    def test_nerve(self):
        ans=self.check("Innervation", self.nerve)
        if ans:
            self.score["Innervation"]+=1
        else:
            self.score["Innervation"]-=1
    
    def test(self):
        test=[1,2,3,4]
        shuffle(test)
        while test:
            val=test.pop()
            if val==1:
                self.test_origin()
            elif val==2:
                self.test_insert()
            elif val==3:
                self.test_action()
            elif val==4:
                self.test_nerve()
            else:
                print("Error in Function 'Test'")
        resp=input("Would you like to see more information about {}? [Y/N]".format(self.name))
        if resp=="Y":
            print(self.notes)
            input("Please press \"Enter\" when you are ready to continue.")