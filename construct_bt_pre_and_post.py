class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def util(self,pre,post,low,high,d):
        if low > high or self.pre_indx >= len(post):
            return None
        
        root = TreeNode(pre[self.pre_indx])
        self.pre_indx += 1
        if low == high or self.pre_indx >= len(post):
            return root
        
        post_indx = d[pre[self.pre_indx]]
        
        if post_indx <= high:
            root.left = self.util(pre,post,low,post_indx,d)
            root.right = self.util(pre,post,post_indx+1,high,d)
        return root
    
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        self.pre_indx = 0
        d = {}
        for i,elem in enumerate(post):
            d[elem] = i
        return self.util(pre,post,0,len(post)-1,d)

s = Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
pre = [3,4,2,1]
post = [1,4,2,3]
root = s.constructFromPrePost(pre,post)
print root.val,root.left.val,root.right.val
