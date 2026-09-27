/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public int MaxDepth(TreeNode root) {
        return MeasureDepth(root, 0);
    }

    private int MeasureDepth(TreeNode root, int currentDepth) {
        if (root == null)
            return currentDepth;
        if (root.right == null)
            return MeasureDepth(root.left, currentDepth + 1);
        if (root.left == null)
            return MeasureDepth(root.right, currentDepth + 1);
        return Math.Max(MeasureDepth(root.left, currentDepth + 1), MeasureDepth(root.right, currentDepth + 1));
    }

}
