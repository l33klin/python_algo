# https://leetcode-cn.com/problems/max-consecutive-ones-iii/


class Node():
    def __init__(self, index):
        self.index = index
        self.next = None


class LinkTab():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def put_node(self, index):
        if not self.head:
            self.head = Node(index)
            self.tail = self.head
        else:
            self.tail.next = Node(index)
            self.tail = self.tail.next
        self.len += 1
    
    def pop_node(self):
        if not self.head:
            return None
        tmp = self.head.index
        self.head = self.head.next
        self.len -= 1
        return tmp


class Solution:
    
    def longestOnes(self, A: list[int], K: int) -> int:
        fill_link = LinkTab()
        left_fill = K
        max_len = 0
        
        start = 0
        cur_len = 0
        for i in range(len(A)):
            if A[i] == 1:
                cur_len += 1
            else:
                if left_fill > 0:
                    left_fill -= 1
                    fill_link.put_node(i)
                    cur_len += 1
                elif K > 0:
                    if fill_link.head.index == start:
                        fill_link.pop_node()
                        fill_link.put_node(i)
                        start += 1
                    else:
                        max_len = cur_len if cur_len > max_len else max_len
                        start = fill_link.pop_node() + 1
                        fill_link.put_node(i)
                        cur_len = i - start + 1
                else:
                    max_len = cur_len if cur_len > max_len else max_len
                    cur_len = 0
        max_len = cur_len if cur_len > max_len else max_len
        return max_len


class SolutionV2:
    
    def longestOnes(self, A: list[int], K: int) -> int:
        max_len = 0
        left = 0
        cur_len = 0
        for i in range(len(A)):
            if A[i] == 1:
                cur_len += 1
                continue
            else:
                if K > 0:
                    K -= 1
                    cur_len += 1
                else:
                    max_len = cur_len if cur_len > max_len else max_len
                    for j in range(left, i):
                        left = j + 1
                        if A[j] == 0:
                            break
                        else:
                            cur_len -= 1
        max_len = cur_len if cur_len > max_len else max_len
        return max_len
                    


if __name__ == '__main__':
    la = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(SolutionV2().longestOnes(la, k))
