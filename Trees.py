#SEGMENT TREES

# Segment Tree for Range Sum Queries (0-indexed, no None defaults)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg_tree = [0] * (4 * self.n)
        self.build(arr, 0, self.n - 1, 0)

    # Build the tree recursively
    def build(self, arr, left, right, node_index):
        if left == right:
            self.seg_tree[node_index] = arr[left]
            return
        mid = (left + right) // 2
        self.build(arr, left, mid, 2 * node_index + 1)
        self.build(arr, mid + 1, right, 2 * node_index + 2)
        self.seg_tree[node_index] = self.seg_tree[2 * node_index + 1] + self.seg_tree[2 * node_index + 2]

    # Internal update function
    def _update(self, index, value, left, right, node_index):
        if left == right:
            self.seg_tree[node_index] = value
            return
        mid = (left + right) // 2
        if index <= mid:
            self._update(index, value, left, mid, 2 * node_index + 1)
        else:
            self._update(index, value, mid + 1, right, 2 * node_index + 2)
        self.seg_tree[node_index] = self.seg_tree[2 * node_index + 1] + self.seg_tree[2 * node_index + 2]

    # Public update function
    def update(self, index, value):
        self._update(index, value, 0, self.n - 1, 0)

    # Internal query function
    def _query(self, query_left, query_right, left, right, node_index):
        if query_right < left or query_left > right:  # No overlap
            return 0
        if query_left <= left and right <= query_right:  # Complete overlap
            return self.seg_tree[node_index]
        mid = (left + right) // 2
        left_sum = self._query(query_left, query_right, left, mid, 2 * node_index + 1)
        right_sum = self._query(query_left, query_right, mid + 1, right, 2 * node_index + 2)
        return left_sum + right_sum

    # Public query function
    def query(self, query_left, query_right):
        return self._query(query_left, query_right, 0, self.n - 1, 0)


# Example usage
arr = [1, 3, 5, 7, 9, 11]
seg = SegmentTree(arr)
print("Sum [1,3]:", seg.query(1, 3))  # 3+5+7=15
seg.update(1, 10)
print("After update sum [1,3]:", seg.query(1, 3))  # 10+5+7=22

       




# QUAD TREES



# FENWICK TREES