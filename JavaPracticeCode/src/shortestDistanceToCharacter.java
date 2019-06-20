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
                int count = value++;
                frequentElement.replace(nums[i],value,count);
            } else {
                frequentElement.put(nums[i],1);
            }
        }
        LinkedList<Integer> kOccurrence = new LinkedList();
        for( Integer key: frequentElement.keySet() ) {
            if (frequentElement.get(key) >= k) {
//                System.out.println(key);
                kOccurrence.add(key);
            }
        }

        return kOccurrence;
    }
}
