class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list = SLinkList()
list.headval = Node('Jan')
e2 = Node('Feb')
e3 = Node('Mar')
e4 = Node('Apr')
e5 = Node('May')
e6 = Node('Jun')
e7 = Node('Jul')
e8 = Node('Aug')
e9 = Node('Sep')
e10 = Node('Oct')
e11 = Node('Nov')
e12 = Node('Dec')

list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6
e6.nextval = e7
e7.nextval = e8
e8.nextval = e9
e9.nextval = e10
e10.nextval = e11
e11.nextval = e12

list.listprint()