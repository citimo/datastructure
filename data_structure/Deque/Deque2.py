# 回文检测器
from Deque1 import Deque
def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)
    
    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    
    return stillEqual

if __name__ == '__main__':
    print(palchecker("lsdkjfskf"))
    print(palchecker("toot"))
