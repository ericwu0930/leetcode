class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

# cur=root
# stack=[]
# sum=0
# if not cur:print (False)
# else:
#     while cur!=None or len(stack):
#         while cur!=None:
#             if len(stack):
#                 stack.append((cur,stack[len(stack)-1][1]+cur.val))
#             else:stack.append((cur,cur.val))
#             cur=cur.left
#         if stack[len(stack)-1][1]==sum:
#             print (True)
#         if cur and cur.right:cur=cur.right
#         else:stack.pop()
#         if len(stack) and cur.right==None:
#             cur=stack[len(stack)-1][0]
#             cur=cur.right
#     print (False)

sum = 22


def f(root, sum):
    if root == None: return False
    if root.left == root.right == None and root.val == sum: return True
    new_sum = sum - root.val
    return f(root.left, new_sum) or f(root.right,new_sum)


print(f(root, sum))
