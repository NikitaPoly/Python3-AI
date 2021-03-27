'''
Decision Tree Induction
Steven Bogaerts (starter code)
'''

# ----------------------------------------------------
# 2) Write the AttributeSpec class here
class AttributeSpec:
    def __init__(self,name,vals):
        self.__name = name
        self.__vals = vals
    def getName(self):
        return self.__name
    def getValAt(self,i):
        return self.__vals[i]
    def getIndexOf(self,value):
        return self.__vals.index(value)
    def getNumVals(self):
        return len(self.__vals)
    def __repr__(self):
        return "AttributeSpec{" + str(self.__name) + ", " + str(self.__vals) + "}"

def testAttributeSpec():
    print("==================== testAttributeSpec ====================")
    tempSpec = AttributeSpec("Temperature", ["Low", "Medium", "High"])
    ratingSpec = AttributeSpec("Rating", [0, 1, 2, 3, 4, 5])
    
    print(tempSpec)
    print(ratingSpec)
    
    print(tempSpec.getName(), tempSpec.getValAt(1), tempSpec.getIndexOf("Medium"), tempSpec.getNumVals())

# ----------------------------------------------------
# 3) Write the Example class here

class Example(object):
    '''
    Example is an example - a collection of attribute keys and values,
    and possibly the class of the example, if known.

    cls - the class of this example (can be left off if unknown)

    nameValDict - dictionary from attribute name (from an AttributeSpec) to the
                 corresponding value for this Example.
    '''

    def __init__(self, nameValDict, cls=None):
        self.__cls = cls
        self.__nameValDict = nameValDict
    def getClass(self):
        return self.__cls
    def hasSameClassAs(self,other):
        return self.__cls == other.__cls
    def getValFor(self,attributeName):
        return self.__nameValDict.get(attributeName)
    def __repr__(self):
        return "Example{"+ self.__cls + ", " + str(self.__nameValDict) + "}"




def testExample():
    print("==================== testExample ====================")
    # "Do you need help lifting this thing?"
    ex1 = Example({"height":5, "width":4, "isHeavy":False}, "No")
    ex2 = Example({"height":5, "width":12, "isHeavy":True}, "Yes")
    ex3 = Example({"height":5, "width":2, "isHeavy":True}) # cls not provided, so it's None (see __init__)
    
    print(ex1)
    print(ex1.getClass())
    print(ex1.hasSameClassAs(ex2))
    print(ex1.getValFor("width"))

# ----------------------------------------------------
# 4) Complete the allSameClass method
# 5) Complete the countClassValues method
# 6) Complete the getMajorityClass method
# 7) Complete the split method
    
class ExampleList(object):
    '''
    A list of Example objects.
    '''

    def __init__(self, exampleList):
        self.__exampleList = exampleList

    def __repr__(self):
        return "ExampleList{" + str(self.__exampleList) + "}"

    def getExampleAt(self, i):
        return self.__exampleList[i]

    def getNumExamples(self):
        return len(self.__exampleList)

    def isEmpty(self):
        return self.__exampleList == []

    def append(self, ex):
        self.__exampleList.append(ex)

    def allSameClass(self):
        standardCLS = self.__exampleList[0]
        for example in self.__exampleList:
            if not standardCLS.hasSameClassAs(example):
                return False
        return True

    def countClassValues(self, classAttrSpec):
        '''
        For the examples in this ExampleList,
        counts the number of occurrences of each class.
        Returns a list valCount, where valCount[i] is the number of occurrences of the ith class value
        (as ordered in classAttrSpec).
        '''
        # Initialize valCount
        valCount = [0 for i in range(classAttrSpec.getNumVals())]
        ''' The above line (a "list comprehension") does the same as the following:
        valCount = []
        for i in range(classAttrSpec.getNumVals()):
            valCount.append(0)
        '''
        
        for ex in self.__exampleList: 
            for i in range(classAttrSpec.getNumVals()):
                if classAttrSpec.getValAt(i) == ex.getClass():
                    valCount[i] += 1
            
        return valCount
    
    def getMajorityClass(self, classAttrSpec):
        '''
        Determines the class that describes the majority of examples
        in the list.
        '''
        valCount = self.countClassValues(classAttrSpec)

        maxID = 0
        for i in range(1, len(valCount)):
            if valCount[i] > valCount[maxID]:
                maxID = i
        return None # change this to what it should be

    def split(self, attrSpec):
        '''
        Splits the examples by attribute.
        Returns a list of ExampleList objects. (So essentially, a list of lists, or a 2-D list.)
        '''
        
        # Initialize the splitExamples structure to a list of empty ExampleList objects.
        splitExamples = [ExampleList([]) for i in range(attrSpec.getNumVals())]
        ''' The above line (a "list comprehension") does the same as the following:
        splitExamples = []
        for i in range(attrSpec.getNumVals()):
            splitExamples.append(ExampleList([]))
        '''
        
        attrName = attrSpec.getName()
        for ex in self.__exampleList: # Using the list for-each notation
            # Get ex's value for this attribute
            # Find the index of that value in the attrSpec
            # Append this example to the corresponding ExampleList (the one for that value)
            #      Use the append method for lists for the above step
            pass # Delete this line once you've filled in your own code
        
        return splitExamples
    

def testExampleListBasic():
    print("==================== testExampleListBasic ====================")
    ex2 = Example({"height":5, "width":12, "isHeavy":True}, "Yes")
    ex3 = Example({"height":5, "width":2, "isHeavy":True}, "Yes")
    ex4 = Example({"height":12, "width":7, "isHeavy":True}, "Yes")

    exList = ExampleList([ex2, ex3])
    print("1)", exList)
    print("2)", exList.getExampleAt(1))
    print("3)", exList.getNumExamples())
    print("4)", exList.isEmpty())
    
    exList.append(ex4)
    print("5)", exList)
    
def testAllSameClass():
    print("==================== testAllSameClass ====================")
    ex2 = Example({"height":5, "width":12, "isHeavy":True}, "Yes")
    ex3 = Example({"height":5, "width":2, "isHeavy":True}, "Yes")
    ex4 = Example({"height":12, "width":7, "isHeavy":False}, "Yes")
    ex5 = Example({"height":9, "width":3, "isHeavy":False}, "No")
    ex6 = Example({"height":9, "width":3, "isHeavy":True}, "Yes")
    
    exList = ExampleList([ex2, ex3, ex4])
    print(exList.allSameClass())
    exList.append(ex5)
    exList.append(ex6)
    print(exList.allSameClass())

def testCountClassValues():
    print("==================== testCountClassValues ====================")
    ex2 = Example({"height":5, "width":12, "isHeavy":True}, "Yes")
    ex3 = Example({"height":5, "width":2, "isHeavy":True}, "Yes")
    ex4 = Example({"height":12, "width":7, "isHeavy":False}, "Yes")
    ex5 = Example({"height":9, "width":3, "isHeavy":False}, "No")
    ex6 = Example({"height":9, "width":3, "isHeavy":True}, "Yes")

    exList = ExampleList([ex2, ex3, ex4, ex5, ex6])
    classAttr = AttributeSpec("Need Help?", ["No", "Yes"])
    print(exList.countClassValues(classAttr))
    
def testGetMajorityClass():
    print("==================== testGetMajorityClass ====================")
    ex2 = Example({"height":5, "width":12, "isHeavy":True}, "Yes")
    ex3 = Example({"height":5, "width":2, "isHeavy":True}, "Yes")
    ex4 = Example({"height":12, "width":7, "isHeavy":False}, "Yes")
    ex5 = Example({"height":9, "width":3, "isHeavy":False}, "No")
    ex6 = Example({"height":9, "width":3, "isHeavy":True}, "Yes")

    exList = ExampleList([ex2, ex3, ex4, ex5, ex6])
    classAttr = AttributeSpec("Need Help?", ["No", "Yes"])
    print(exList.getMajorityClass(classAttr))

    ex7 = Example({"height":9, "width":4, "isHeavy":False}, "No")
    exList2 = ExampleList([ex5, ex6, ex7])
    print(exList2.getMajorityClass(classAttr))

def testSplit():
    print("==================== testSplit ====================")
    ex2 = Example({"height":'S', "width":'L', "isHeavy":True}, "Yes")
    ex3 = Example({"height":'S', "width":'S', "isHeavy":True}, "Yes")
    ex4 = Example({"height":'L', "width":'M', "isHeavy":False}, "Yes")
    ex5 = Example({"height":'M', "width":'S', "isHeavy":False}, "No")
    ex6 = Example({"height":'M', "width":'S', "isHeavy":True}, "Yes")

    exList = ExampleList([ex2, ex3, ex4, ex5, ex6])
    heightSpec = AttributeSpec("height", ['S', 'M', 'L'])
    widthSpec = AttributeSpec("width", ['S', 'M', 'L'])
    isHeavySpec = AttributeSpec("isHeavy", [False, True])
    
    print("----- Split by height")
    splitByHeight = exList.split(heightSpec)
    for exListID in range(len(splitByHeight)):
        print("Height", heightSpec.getValAt(exListID), "has list:", splitByHeight[exListID], end='\n\n')
    
    print("----- Split by isHeavy")
    splitByIsHeavy = exList.split(isHeavySpec)
    for exListID in range(len(splitByIsHeavy)):
        print("isHeavy", isHeavySpec.getValAt(exListID), "has list:", splitByIsHeavy[exListID], end='\n\n')

def testAll():
    testAttributeSpec()
    testExample()
    testExampleListBasic()
    testAllSameClass()
    testCountClassValues()
    testGetMajorityClass()
    testSplit()
testCountClassValues()