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
    int cnt = 0;
    public ListNode mergekl(ListNode[] lists, int i1, int i2){
        ListNode tmp;
        
        if(lists[i1]==null){
            return lists[i2];
        }else if(lists[i2]==null){
            return lists[i1];
        }else{
            if(lists[i1].val>lists[i2].val) {
                tmp = new ListNode(lists[i2].val);
                lists[i2] = lists[i2].next;
                tmp.next = mergekl(lists, i1, i2);
            }
            else {
                tmp = new ListNode(lists[i1].val);
                lists[i1] = lists[i1].next;
                tmp.next = mergekl(lists, i1, i2);
            }
        }
        return tmp;
    }
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==0) return null;
        if(lists.length==1) return lists[0];
        int len = lists.length;
        while(len != 0){
            for(int i = 0; i<len;i+=2){
                if(i+1>=len) break;
                System.out.println(cnt++);
                lists[i/2] = mergekl(lists, i, i+1);
            }
            if(len%2==1) lists[0] = mergekl(lists, 0, len-1);
            len/=2;
        }
        

        return lists[0];
    }
}
/*
[....] -[......] [.......]
4 2 1
5 2
*/