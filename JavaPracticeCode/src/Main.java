import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
//        System.out.println("Hello World!");
//        String[] words = new String[]{"hi", "ab", "ca"};
//        String[] more = new String[]{"fi", "ab", "ca"};
//        System.out.println(merge(words, more));
//        String phrase = "Ratzs";
//        System.out.println(isPermutationOfPalindrome(phrase));
//        String phrase1 = "aaaabbbbbbbbbbbc";
//        System.out.println(Compressed(phrase1));
//        int [][] matrix = {{1, 0, 3}, {4, 5, 0}, {2, 3, 4}};
//        zeroMatrix(matrix);
//        String s1 = "abc";
//        String s2 = "bca";
//        System.out.println(isRotation(s1, s2));
//
//        // Ch-2 LinkedList Implementation
//        Node n1 = new Node(7);
//        Node n2 = new Node(5);
//        Node n3 = new Node(6);
//        Node n8 = new Node(8);
//        Node n4 = new Node(1);
//        Node n5 = new Node(8);
//        Node n6 = new Node(5);
//        Node n7 = new Node(6);
//        n1.next = n2;
//        n2.next = n3;
////        n3.next = n4;
//        n8.next = n4;
//        n4.next = n5;
//        n5.next = n6;
//        n6.next = n7;
//        Node.printLinkedList(Node.removeDups(n1));
//        Node.printLinkedList(Node.kthToLast(n1,3));
//        Node.printLinkedList(Node.deleteMiddleNode(n1));
//        //Node.partitionArrangement(n1, 2);
//        Node.printLinkedList(Node.sumLists(n1, n4));
//        System.out.println(Node.isPalindrome(n1));
//        Node.printLinkedList(Node.intersectingNode(n1, n4));
//        int[] nums = new int[]{1, 2, 3};
        shortestDistanceToCharacter c1 = new shortestDistanceToCharacter();
//        int output[] = c1.productExceptSelf(nums);
//        for (int i=0; i<output.length; i++) {
//            System.out.println(output[i]);
//        }
//        int[] A = new int[] {1, 2};
//        int[] B = new int[] {-2, -1};
//        int[] C = new int[] {-1, 2};
//        int[] D = new int[] {0, 2};
//        int finalOutput = c1.fourSumCount(A, B, C, D);
//        System.out.println(finalOutput);
//        List<List<Integer>> finalOutput = c1.subsets(nums);
//        finalOutput = c1.topKFrequent(nums, 2);
//        for (int i=0; i<finalOutput.size(); i++) {
//            System.out.println(finalOutput.get(i));
//        }

        c1.generateParenthesis(5);
    }

    public static ArrayList<String> merge(String[] words, String[] more) {
        ArrayList<String> sentence = new ArrayList<>();
        for (String w: words) {
            sentence.add(w);
        }
        for (String w: more) {
            sentence.add(w);
        }
        return sentence;
    }

    public static int getCharNumber(Character c) {
        int a = Character.getNumericValue('a');
        int z = Character.getNumericValue('z');

        int val = Character.getNumericValue(c);
        if (a <= val && val <= z) {
            return val - a;
        }
        return -1;
    }

    public static  boolean isPermutationOfPalindrome(String phrase) {
        int countOdd = 0;
        int[] table = new int[Character.getNumericValue('z') - Character.getNumericValue('a') + 1 ];
        for (char c : phrase.toCharArray()) {
            int x = getCharNumber(c);
            if (x != -1) {
                table[x]++;
                if (table[x] % 2 == 0) {
                    countOdd ++;
                } else {
                    countOdd --;
                }
            }
        }
        return countOdd <= 1;
    }

    public static String Compressed(String phrase) {
        int lenOfTheString = phrase.length();
        int countConsecutive = 0;
        StringBuilder compressedString = new StringBuilder();
        for (int i = 0; i < lenOfTheString; i++) {
            countConsecutive ++;
            if ( i + 1 >= phrase.length() || phrase.charAt(i) != phrase.charAt(i + 1)) {
                compressedString.append(phrase.charAt(i));
                compressedString.append(countConsecutive);
                countConsecutive = 0;
            }
        }
        return compressedString.length() > lenOfTheString ? phrase : compressedString.toString();
    }

    public static void zeroMatrix(int [][] matrix) {
        // set row and col to true
        boolean[] row = new boolean[matrix.length];
        boolean[] col = new boolean[matrix[0].length];

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    row[i] = true;
                    col[j] = true;
                }

            }
        }

        for (int i = 0; i < row.length; i++) {
            if (row[i]) nullifyRow(matrix, i);
        }

        for (int i = 0; i < col.length; i++) {
            if (col[i]) nullifyCol(matrix, i);
        }

        for (int i=0; i < row.length; i++) {
            for (int j=0; j< col.length; j++) {

            }
        }

    }

    public static void nullifyRow(int[][] matrix1, int row1) {
            for (int i = 0; i < matrix1[0].length; i++) {
                matrix1[row1][i] = 0;
            }
        }

    public static void nullifyCol(int[][] matrix2, int col1) {
            for (int i = 0; i < matrix2[0].length; i++) {
                matrix2[i][col1] = 0;
            }
        }

    public static boolean isRotation(String s1, String s2) {
        int len1 = s1.length();
        int len2 = s2.length();
        if (len1 == len2 && len1 > 0) {
            String s1s1 = s1 + s1;
            if (s1s1.contains(s2)) {
                return true;
            } else {
                return false;
                }
            }
            return false;
        }
    }

// -------- Linked List ---------- //
class Node {
    Node next = null;
    int data;

    public Node(int d) {
        data = d;
    }

    public static Node removeDups(Node n) {
        HashSet<Integer> set1 = new HashSet<Integer>();
        // You need to keep track of the head element.
        Node head = n;
        // Pointer that is needed when duplicate element needs to be removed.
        Node previous = null;
        while (n != null) {
            if(set1.contains(n.data)) {
                previous.next = n.next;
            } else {
                set1.add(n.data);
                previous = n;
            }
            n = n.next;
        }
        return head;
    }

    public static void printLinkedList(Node n) {
        while (n != null) {
            System.out.println(n.data);
            n = n.next;
        }
    }

    public static Node kthToLast(Node n, int k) {
        Node p1 = n;
        Node p2 = n;

        for (int i = 0; i < k; i++) {
            if (p1.next == null) return null;
            p1 = p1.next;
        }

        while (p1 != null) {
            p1 = p1.next;
            //System.out.println("Value of p2 data = " + p2.data);
            p2 = p2.next;
        }
        return p2;
    }

    public static Node deleteMiddleNode(Node n) {
        Node head = n;
        Node p1 = n;
        int midCount = 0;
        while (p1 != null) {
            p1 = p1.next;
            midCount ++;
        }
        // need to get the mid value.
        midCount /= 2;
        System.out.println("Mid value is : " + midCount);
        // next element should already be pointed.
        Node next = n.next;
        while (n != null) {
            midCount --;
            if (midCount == 0) {
                n.data = next.data;
                n.next = next.next;
            }
            n = n.next;
            next = next.next;
        }

        return head;
    }

    public static Node sumLists(Node n1, Node n2) {
        ArrayList<Integer> sumList1 = new ArrayList<>();
        Node n3 = n1;
        Node n4 = n3;
        int sum = 0, carry = 0, element = 0;
        while(n1!=null) {
            sum = (n1.data + n2.data)%10;
            element = sum + carry;
            sumList1.add(element);
            //System.out.println(element);
            carry = (n1.data + n2.data)/10;
            n1 = n1.next;
            n2 = n2.next;
        }
        for (Integer num : sumList1) {
            n3.data = num;
            n3 = n3.next;
        }
        return n4;
    }
    // check if the given list is palindrome.
    public static boolean isPalindrome(Node n1) {
        Node n2 = null;
        while (n1 != null) {
            Node n3 = new Node(n1.data);
            n3.next = n2;
            n2 = n3;
            n1 = n1.next;
        }
        // check half list
        while (n1 != null && n2 != null) {
            if (n1.data != n2.data) return false;
            n1 = n1.next;
            n2 = n2.next;
        }
        return n1 == null && n2 == null;
    }

    public static Node intersectingNode(Node n1, Node n2) {
        if (n1 == null || n2 == null) return null;
        Node n1Copy = n1;
        Node n2Copy = n2;
        // get the size of both the lists.
        int sizen1 = 1, sizen2 = 1;
        while (n1.next != null) {
            sizen1 ++;
            n1 = n1.next;
        }
        while (n2.next != null) {
            sizen2 ++;
            n2 = n2.next;
        }
//        System.out.println("Length of n1: " + sizen1);
//        System.out.println("Length of n2: " + sizen2);
        // check if the tail element is same.
        if (n1.data != n2.data) return null;
        // find which list is longer since we need to move the pointer with that steps.
        Node shorter = sizen1 < sizen2 ? n1Copy : n2Copy;
        Node longer = sizen1 < sizen2 ? n2Copy : n1Copy;
        int sizeDiff = Math.abs(sizen1 - sizen2);
//        System.out.println(sizeDiff);
        // start from the equal length
        while (sizeDiff > 0 && longer != null) {
//            System.out.println(longer.data);
            longer = longer.next;
            sizeDiff --;
        }
        // Move both the pointers until they collide.
        while (shorter.data != longer.data) {
            //System.out.println("Short data: " + shorter.data + "Longer data: " + longer.data);
            shorter = shorter.next;
            longer =  longer.next;
        }
        return longer;
    }


}
