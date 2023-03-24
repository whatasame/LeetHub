/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(); // Head is empty
        ListNode originHeadAddr = head;

        while(!(list1 == null && list2 == null)){
            if(list1 != null && list2 != null){ // Both exist
                if(list1.val < list2.val){
                    head.next = list1;
                    list1 = list1.next;
                } else {
                    head.next = list2;    
                    list2 = list2.next;
                }
            } else if (list1 != null){ // Only list1 remain
                head.next = list1;
                list1 = list1.next;
            } else if (list2 != null){ // Only list2 remain
                head.next = list2;
                list2 = list2.next;
            }             

            head = head.next;
        }   

        return originHeadAddr.next;
    }

}