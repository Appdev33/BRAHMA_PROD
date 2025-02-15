//package DP;
//
//public class tree {
//
//	public static void main(String[] args) {
//		// TODO Auto-generated method stub
////		System.out.println(diameter());
//	}
//	
//
////Diameter of a tree
//	class Solution {
//	      public int solve(TreeNode root,int maxt[]){
//	        if(root==null) {
//	            return 0;
//	        }
//	        int maxn=Integer.MIN_VALUE;
//	       
//	        
//	        int l= solve(root.left,maxt);
//	        int r= solve(root.right,maxt);
//	        
//	        
//	        int pass= 1+l+r;
//	        int notpass= 1+ Math.max(l,r); //height 
//	       maxn= Math.max(pass,notpass);
//	       maxt[0]=Math.max(maxt[0],maxn);
//	        return notpass;
//	    
//	        }
//	    public int diameterOfBinaryTree(TreeNode root) {
//	         // int res=Integer.MIN_VALUE;
//	        int maxt[]={Integer.MIN_VALUE};
//	         solve(root,maxt);
//	        return maxt[0]-1;
//	      
//	    }
//	}
//
//// max path sum in tree any node to any node   
//	
////class Solution {
////    int max=Integer.MIN_VALUE;;
////    public int maxPathSum(TreeNode root) {
////         if(root==null)
////             return 0;
////        solve(root);
////        return max;
////    }
////
//// 
////private static int solve(TreeNode root)
////{
////    if(root==null)
////        return 0;
////    int l=solve(root.left);
////    int r=solve(root.right);
////    max=Math.max(max , Math.max(Math.max(Math.max(l,r)+root.val,root.val) , root.val+l+r));
////    
////    return Math.max(Math.max(l,r)+root.val,root.val);
////    }
////}
//
//
////max path sum in tree leAF node to LEAF node
//
//
