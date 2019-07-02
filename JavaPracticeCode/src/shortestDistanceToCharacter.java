import javax.annotation.processing.SupportedSourceVersion;
import java.util.*;

public class shortestDistanceToCharacter {
    // two pointers : 1 to take care of e and another for other characters
    // input : string s, char c
    // output: array of distances from that character


    public int[] shortestToChar(String S, char C) {
        int strLength = S.length();
        int[] distList = new int[strLength];
        int charPosition = S.indexOf(C);
        if (charPosition == -1)
            return null;
        LinkedList<Integer> charOccurrence = new LinkedList();
        // store all the occurrences of the given character C.
        for (int i=0; i <strLength; i++) {
            if (C == S.charAt(i))
                charOccurrence.add(i);
        }
        for (int i=0; i <strLength; i++) {
            int diff = Integer.MAX_VALUE - 1;
            if (C == S.charAt(i)) distList[i] = 0;
            for (int j = 0; j<charOccurrence.size(); j++) {
                diff = Math.min(diff,Math.abs(charOccurrence.get(j)-i));
            }
            distList[i] = diff;
        }
        return distList;
    }

    public int[] productExceptSelf(int[] nums) {
        // This works for O(n^2) time
        int[] product = new int[nums.length];
        int len = nums.length;
        product[0] = 1;
        for (int i = 1; i < len; i++)
            product[i] = product[i - 1] * nums[i - 1];
        for (int i = len - 2, temp = 1; i >= 0; i--) {
            temp *= nums[i + 1];
            product[i] *= temp;
        }
        return product;
    }
//        for (int i = 0; i<nums.length; i++) {
//            int product1 = 0;
//            for (int j = 0; j <nums.length; j++) {
//                if (i != j)  {
//                   int temp = nums[j];
//                   product1 *= temp;
//                }
//            }
//            product[i] = product1;
//        }
//        return product;
//    }
    public List<Integer> topKFrequent(int[] nums, int k) {
        //Given a non-empty array of integers, return the k most frequent elements.
        HashMap<Integer, Integer> frequentElement = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            if (frequentElement.containsKey(nums[i])) {
                int value = frequentElement.get(nums[i]);
                value++;
                frequentElement.replace(nums[i],value);
            } else {
                frequentElement.put(nums[i],1);
            }
        }
        // init heap 'the less frequent element first'
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>
                ((n1, n2) -> frequentElement.get(n1) - frequentElement.get(n2));
        // keep k top frequent elements in the heap
        for (int n: frequentElement.keySet()) {
            heap.add(n);
            if (heap.size() > k)
                heap.poll();
        }
        LinkedList<Integer> kOccurrence = new LinkedList();
        while (!heap.isEmpty())
            kOccurrence.add(heap.poll());
        Collections.reverse(kOccurrence);
        return kOccurrence;
    }

    //Given a set of distinct integers, nums, return all possible subsets (the power set).
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> out = new ArrayList<List<Integer>>();
        out.add(new ArrayList<Integer>());

        for (int i = nums.length - 1; i >= 0; i--) {
            int maximum = out.size();
            System.out.println("Sie"+maximum);
            //Create new lists with all the lists already made + the current nums[i];
            for (int j = 0; j < maximum; j++) {
                System.out.println("Inside" +out.get(j));
                List<Integer> curr = new ArrayList<Integer>(out.get(j));
                System.out.println("Before Curr" +curr);
                curr.add(nums[i]);
                System.out.println("After Curr" +curr);
                out.add(curr);
            }
        }
        return out;
    }

    //Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
    //there are such that A[i] + B[j] + C[k] + D[l] is zero.
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        int ans  = 0;
        HashMap<Integer, Integer> matainSet= new HashMap<>();
        // as to get 0, handle half half.
        for (int i=0; i < A.length; i++ ) {
           for (int j=0; j<B.length; j++) {
               int ans1 = A[i] + B[j];
               if (matainSet.containsKey(ans1)) {
                   int sum = matainSet.get(ans1);
                   sum += 1;
                   matainSet.replace(ans1,sum);
               } else {
                   matainSet.put(ans1,1);
               }
           }
        }
        // Handle C and D set:
        for (int i=0; i < C.length; i++ ) {
            for (int j = 0; j < D.length; j++) {
                int ans2 = -C[i] - D[j];
                System.out.println("Ans 2 of C and D"+ans2);
                if (matainSet.containsKey(ans2)) {
                    ans += matainSet.get(ans2);
                }
            }
        }
        return ans;
    }

    //Given a non-empty array of integers, every element appears twice except for one. Find that single one.
    // It should have linear complexity
    public int singleNumber(int[] nums) {
        // Below method takes O(n) space
//        HashMap<Integer,Integer> checkNumber = new HashMap<>();
//        for (int i=0; i<nums.length; i++) {
//            if (checkNumber.containsKey(nums[i])) {
//                int appendValue = checkNumber.get(nums[i]);
//                appendValue++;
//                checkNumber.replace(nums[i],appendValue);
//            } else {
//                checkNumber.put(nums[i],1);
//            }
//        }
//        if(checkNumber.containsValue(1)) {
//            for (Object o : checkNumber.keySet()) {
//                if (checkNumber.get(o).equals(1)) {
//                    return (int)o;
//                }
//            }
//        }
        // This takes O(1) space complexity
        int ans = 0;
        for (int i=0; i<nums.length; i++) {
            ans ^= nums[i];
        }
        return ans;
    }

    //Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    public List<String> generateParenthesis(int n) {
            List<String> ans = new ArrayList();
            backtrack(ans, "", 0, 0, n);
            return ans;
        }

    public void backtrack(List<String> ans, String cur, int open, int close, int max){
        if (cur.length() == max * 2) {
            ans.add(cur);
            return;
        }

        if (open < max)
            backtrack(ans, cur+"(", open+1, close, max);
        if (close < open)
            backtrack(ans, cur+")", open, close+1, max);
    }

    // Given a n x n matrix where each of the rows and columns are sorted in ascending order,
    // find the kth smallest element in the matrix.
//    public int kthSmallest(int[][] matrix, int k) {
//
//        return 0;
//    }

    //Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    //Integers in each row are sorted in ascending from left to right.
    //Integers in each column are sorted in ascending from top to bottom.
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        if (row == 0 || matrix[0].length == 0) return false;
        for (int i=0; i<row; i++){
            int col = matrix[i].length;
            if (target >= matrix[i][0] && target <= matrix[i][col-1]){
                for(int j=0; j<matrix[i].length; j++) {
                    if (target == matrix[i][j]) return true;
                }
            } else continue;
        }
        return false;
    }
}

