import unittest
from solution.solution import ListItem, LargestList, max_non_neighbor_sum

class LargestListTests(unittest.TestCase):
    def test(self):
        l = LargestList(4)
        arr = [2, 3, 1, 4]
        for i in range(len(arr)):
            l.tryAdd(ListItem(i, arr[i]))
        
        print(f"List: {l.list}")
        self.assertEqual(l[0].value, 4) # 4
        self.assertEqual(l[0].idx, 3) # idx of 4
        
        self.assertEqual(l[1].value, 3) # 3
        self.assertEqual(l[1].idx, 1) # idx of 3
        
        self.assertEqual(l[2].value, 2) # 2
        self.assertEqual(l[2].idx, 0) # idx of 2

        self.assertEqual(l[3].value, 1) # 1
        self.assertEqual(l[3].idx, 2) # idx of 1

# class SolutionTests(unittest.TestCase):
#     def test_example(self):
#         answer = max_non_neighbor_sum([2, 4, 6, 2, 5])
#         self.assertEqual(answer, 13)

#     def test_zeros(self):
#         answer = max_non_neighbor_sum([0, 0, 0, 0])
#         self.assertEqual(answer, 0)

#     def test_simple(self):
#         answer = max_non_neighbor_sum([1, 2, 3])
#         self.assertEqual(answer, 4)

#     def test_neighboring_largest_sum(self):
#         answer = max_non_neighbor_sum([1, 3, 2])
#         self.assertEqual(answer, 3)

#     def test_negative_answer(self):
#         answer = max_non_neighbor_sum([0, -1, -3, -9, -13])
#         self.assertEqual(answer, -3)

#     def test_arbitrary(self):
#         answer = max_non_neighbor_sum([4, 425, 1230, 90, -1000000, 3, 15])
#         self.assertEqual(answer, 1245)

#     # TODO: change name once I handle this
#     def test_unhandled_edge_case(self):
#         answer = max_non_neighbor_sum([3, 10, 5, 2])
#         self.assertEqual(12, answer)




if __name__ == "__main__":
    unittest.main()