#create a constructor for tree
class node:
    def __init__(self, data =None): 
        self.data = data  
        self.left = None
        self.right = None

#make a tree like the example tree given below
#        1
#     /     \
#    2       3
#  /  \     /  \
# 4    5   6    7
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

print("Enter a number to check with path sum:")
n = int(input())
s=0
#list to contain the path sums
ans=[]

#function to check path sum
# recursively call to check each path

def pathsum(node,s):
    if node is None:
        print("Empty tree")
    else:
        s = s + node.data
        if node.left is not None:
            pathsum(node.left,s)
        if node.right is not None:
            pathsum(node.right,s)
        if node.left is not None and node.right is not None:
            s = 0
        if s!=0:
            ans.append(s)

#call pathsum fucntion to check if the input is equal to any path sum of tree
pathsum(root,s)       
if n in ans:
    print(True)
else:
    print(False)
"""
Output for correct input:
Enter a number to check with path sum:
7
True
Output for incorrect input:
Enter a number to check with path sum:
13
False
"""
