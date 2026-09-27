
public class Solution {
    public TreeNode InvertTree(TreeNode root) {
        if (root == null)
            return root;
        
        (root.right, root.left) = (root.left, root.right);
        InvertTree(root.right);
        InvertTree(root.left);
        
        return root;
    }
}
