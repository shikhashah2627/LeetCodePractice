import java.util.ArrayList;

// Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
class Solution {
        public ArrayList<Integer> inorder (TreeNode root, ArrayList< Integer > arr){
            if (root == null) return arr;
            inorder(root.left, arr);
            arr.add(root.val);
            inorder(root.right, arr);
            return arr;
        }

        public int kthSmallest (TreeNode root,int k){
            ArrayList<Integer> nums = inorder(root, new ArrayList<Integer>());
            return nums.get(k - 1);
        }

        TreeNode next = null;
        public void flatten(TreeNode root) {
            if(root == null)
                return;
            flatten(root.right);
            flatten(root.left);
            root.right = next;
            root.left = null;
//            System.out.println(next.val);
            next = root;
        }
    }


