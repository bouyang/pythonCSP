class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_sum(root: TreeNode) -> int:
    all_paths = []
    trav(root, [], all_paths)

    if all_paths[0]:
        max = all_paths[0][1]
    else:
         return 0

    for path in all_paths:
         if path[1] > max:
              max = path[1]

    return max
    
def trav(node, current_path, all_paths):
        if not node:
            return
        
        current_path.append(node.value)
        
        if not node.left and not node.right:
            path_sum = sum(current_path)
            all_paths.append((list(current_path), path_sum))
        else:
            trav(node.left, current_path, all_paths)
            trav(node.right, current_path, all_paths)

        current_path.pop()



tree = TreeNode(5,
                 TreeNode(-22,
                   TreeNode(9),
                   TreeNode(50)),
                 TreeNode(11,
                   TreeNode(9),
                   TreeNode(2)))

print(max_sum(tree))