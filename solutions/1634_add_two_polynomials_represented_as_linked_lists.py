class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        head = PolyNode()
        node = head
        while poly1 and poly2:
            if poly1.power == poly2.power:
                if poly1.coefficient + poly2.coefficient != 0:
                    node.next = PolyNode(poly1.coefficient+poly2.coefficient, poly1.power)
                    node = node.next
                poly1 = poly1.next
                poly2 = poly2.next
            elif poly1.power > poly2.power:
                node.next = PolyNode(poly1.coefficient, poly1.power)
                node = node.next
                poly1 = poly1.next
            else:
                node.next = PolyNode(poly2.coefficient, poly2.power)
                node = node.next
                poly2 = poly2.next
        node.next = poly1 if poly1 else poly2
        return head.next
