def inorder_transversal(root):
    result=[]


    def inorder(root):
        if not root:
            return
        
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)

    inorder(root)

    return result

