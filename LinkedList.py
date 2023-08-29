import numpy as np
from typing import List, Tuple
from functools import reduce


class Node:
    def __init__(self, val=None, next_obj=None):
        self.val = val
        self.next = next_obj


class LinkedList(Node):
    def __init__(self, node=None, depth=0):
        self.head = node
        self.depth = depth
        self.last = self._get_last()
        super().__init__(node.val, node.next)

    def __from_list(self, lst):
        if len(lst) > 0:
            return Node(lst[0], self.__from_list(lst[1:]))

    def from_list(self, lst: List) -> None:
        assert len(lst) > 0
        lst = np.flip(lst)
        self.head = Node(lst[0])
        if len(lst[1:]) > 0:
            for el in lst[1:]:
                self.push(el)

    def push(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self._get_last()

    def __add(self, value, head):
        if head:
            if not head.next:
                return Node(head.val, Node(value))
            current = head.val
            return Node(current, self.__add(value, head.next))

    def add(self, value, inplace=False):
        if inplace:
            self.head = self.__add(value, self.head)
            self._get_last()
            return

        return LinkedList(self.__add(value, self.head))

    def __get_index(self, ind: int, head: Node = None) -> Node:
        if ind >= 1 and head and head.next:
            head = head.next
            return self.__get_index(ind - 1, head)
        else:
            return head

    def get_index(self, ind):
        ind = ind if ind <= self.depth else self.depth + 1
        return LinkedList(self.__get_index(ind, self.head), depth=self.depth - ind)

    def __remove(self, ind, node, i=0):
        if ind == 0:
            return node.next
        elif i == ind:
            node = node.next
            return node
        elif node.next and i < ind:
            return Node(node.val, self.__remove(ind, node.next, i + 1))

    def remove(self, ind, inplace=False):
        assert ind <= self.depth
        if inplace:
            self.head = self.__remove(ind, self.head)
            self._get_last()
            return
        else:
            head = self.head
            return LinkedList(self.__remove(ind, head))

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_val = current.next
            current.next = prev
            prev = current
            current = next_val
        return prev

    def _reverse(self):
        self.head = self.reverse()

    def slice(self, f, t):
        if t < f:
            return LinkedList(self.get_until(f).get_index(t).reverse())
        return LinkedList(self.get_until(t).get_index(f))

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print("")

    def __replace(self, ind: int, node, i: int = 0, replace=None):
        if node.next:
            next_obj = node.next
            if i == ind:
                return LinkedList(Node(replace, next_obj))
            elif i <= self.depth:
                return Node(node.val, self.__replace(ind, next_obj, i + 1, replace))

    def replace_index(self, ind: int, replace):
        current = self.head
        if ind > self.depth:
            new = self.add(replace)
        else:
            new = self.__replace(ind, current, replace=replace)

        return LinkedList(new)

    def __get_until(self, ind, head: Node = None):
        if ind > 0:
            curr_val = head.val
            next_val = head.next
            head = next_val
            return Node(curr_val, self.__get_until(ind - 1, head))

    def get_until(self, ind):
        if ind <= 0: return LinkedList(Node())
        ind = ind if ind <= self.depth else self.depth + 1
        return LinkedList(self.__get_until(ind, self.head), depth=ind)

    def _get_last(self):
        head = self.head
        d = 0
        while head.next:
            head = head.next
            d += 1

        self.depth = d
        return head

    def _split_bins(self):
        d = self.depth + 1
        if d > 1:
            prev = self.get_until(d // 2)
            forw = self.get_index(d // 2)
            return prev._split_bins(), forw._split_bins()

        return self.head

    def merge_sort(self):
        a, b = self._split_bins()
        check_tup = lambda x: isinstance(x, tuple)

        def merge_loop(a, b):
            # print(f"Merging results of {a}, {b}")
            r = []
            if a and b:
                if a[0].val < b[0].val:
                    r.append(a[0].val)
                    a.pop(0)
                else:
                    r.append(b[0].val)
                    b.pop(0)
                # print("While A and B are not None, result is:", r)
            elif not a or not b:
                # print("One of the args is None!")
                if not a and not b:
                    # print("All arguments are None!!!")
                    return

                n = b if not a else a
                # print(f"Returning argument which is NOT None, {n}")
                return n

            return r + merge_loop(a, b)

        def compare(a, b):
            # print("COMPARING A and B: ", a, b)
            if all(map(lambda x: not check_tup(x), [a, b])):
                # print(f"Both nums, returning {[a, b] if a < b else [b, a]}")
                return [a.val, b.val] if a.val < b.val else [b.val, a.val]
            elif any(map(lambda x: not check_tup(x), [a, b])):
                # print("One of arguments is not tuple, defining it")
                tup_el = merge_sort(*a) if isinstance(a, tuple) else merge_sort(*b)
                val_el = a if not isinstance(a, tuple) else b

                out = []
                for i in range(len(tup_el)):
                    if tup_el[i].val < val_el.val:
                        out.append(tup_el[i])
                    else:
                        out.append(val_el)
                        for e in tup_el[i:]:
                            out.append(e)
                        return out

                out.append(val_el)
                # print(f"One is num, returning {out}")
                return out
            else:
                # print(f"Both arguments are tuples: {a}, {b}")
                ins = []
                for tup in [a, b]:
                    ins.append(merge_sort(*tup))

                res = merge_loop(*ins)
                # print(f"Going to return {res}")
                return res

        return compare(a, b)


if __name__ == "__main__":
    llist = LinkedList(Node(-100,
                            Node(1,
                                 Node(100,
                                      Node(500),
                                      )
                                 )))


    def flatten_tuples(t):
        for x in t:
            if isinstance(x, tuple):
                yield from flatten_tuples(x)
            else:
                yield x


    def flatten(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, tuple):
                res = flatten_tuples(res)
            return list(res)

        return wrapper


    def _split_bins(llist):
        d = llist.depth + 1
        if d > 1:
            prev = llist.get_until(d // 2)
            forw = llist.get_index(d // 2)
            return _split_bins(prev), _split_bins(forw)

        return llist.head.val


    def merge_sort(objs):
        if any([isinstance(el, tuple) for el in objs]):
            for el in objs:
                if len(el) > 1:
                    pass


    @flatten
    def split_bins(llist):
        return _split_bins(llist)


    print("Initial state")
    llist = LinkedList(Node())
    llist.from_list([14, 27, -1, -234, 73, 1, 0])
    llist.print_list()
    print(llist.merge_sort())
    # print(llist.depth)
    #llist.remove(3, inplace=True)



    # llist.add(0, inplace=True)
    # llist.add(0.1, inplace=True)
    # llist.add(3, inplace=True)
    # llist.push(1)
    # i = (llist.depth + 1) // 2
    # print(llist.depth, i)
    # print("List after adding and pushing")
    # llist.print_list()
    # print("List after replacement")
    # llist.replace_index(4, 100).print_list()
    # print(f"All elements until {i}")
    # llist.get_until(i).print_list()
    # print("Depth:", llist.get_until(i).depth)
    # print(f"All elements after {i}")
    # llist.get_index(i).print_list()
    # print("Depth:", llist.get_index(i).depth)
    # print("Sliced list")
    # llist.slice(0, 4).print_list()
    # print("List final state")
    # llist.print_list()

    def merge_sort(a, b):
        check_tup = lambda x: isinstance(x, tuple)

        def merge_loop(a, b):
            # print(f"Merging results of {a}, {b}")
            r = []
            if a and b:
                if a[0] < b[0]:
                    r.append(a[0])
                    a.pop(0)
                else:
                    r.append(b[0])
                    b.pop(0)
                # print("While A and B are not None, result is:", r)
            elif not a or not b:
                # print("One of the args is None!")
                if not a and not b:
                    # print("All arguments are None!!!")
                    return

                n = b if not a else a
                # print(f"Returning argument which is NOT None, {n}")
                return n

            return r + merge_loop(a, b)

        def compare(a, b):
            # print("COMPARING A and B: ", a, b)
            if all(map(lambda x: not check_tup(x), [a, b])):
                # print(f"Both nums, returning {[a, b] if a < b else [b, a]}")
                return [a, b] if a < b else [b, a]
            elif any(map(lambda x: not check_tup(x), [a, b])):
                # print("One of arguments is not tuple, defining it")
                tup_el = merge_sort(*a) if isinstance(a, tuple) else merge_sort(*b)
                val_el = a if not isinstance(a, tuple) else b

                out = []
                for i in range(len(tup_el)):
                    if tup_el[i] < val_el:
                        out.append(tup_el[i])
                    else:
                        out.append(val_el)
                        for e in tup_el[i:]:
                            out.append(e)
                        return out

                out.append(val_el)
                # print(f"One is num, returning {out}")
                return out
            else:
                # print(f"Both arguments are tuples: {a}, {b}")
                ins = []
                for tup in [a, b]:
                    ins.append(merge_sort(*tup))

                res = merge_loop(*ins)
                # print(f"Going to return {res}")
                return res

        return compare(a, b)


    # print(_split_bins(llist))
    # print(
    #     merge_sort(*_split_bins(llist))
    # )
    # lst = [13, 56, 1, 34, -5, 6, 20, 182, 5, -19442]
    # llist2 = LinkedList(Node())
    # llist2.from_list(lst)
    # llist2.print_list()
    # print(merge_sort(*_split_bins(llist2)))

    def test_MS():
        print("CHECKING IN RANGE OF SIZES FROM 1 to 100")
        # for _ in range(1000):
        #     print(f"Iteration number: {_}")
        #     size = np.random.randint(2, 101)
        #     rnd = np.random.choice(range(-10000, 10000), size)
        #     # print(rnd)
        #     llist = LinkedList(Node())
        #     llist.from_list(rnd)
        #     res = merge_sort(*_split_bins(llist))
        #     if sorted(rnd) != res:
        #         return False

        print("CHECKING IN RANGE OF SIZES FROM 1 to 1000")
        for _ in range(10):
            print(f"Iteration number: {_}")
            size = np.random.randint(2, 100)
            rnd = np.random.choice(range(-10000, 10000), size)
            # print(rnd)
            llist = LinkedList(Node())
            llist.from_list(rnd)
            res = merge_sort(*_split_bins(llist))
            if sorted(rnd) != res:
                return False

        return True

    # print(test_MS())
