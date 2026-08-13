package main

import (
	"container/heap"
	"fmt"
	"math"
	"sort"
	"strings"
)

func main() {

	// =========================================================
	// ARRAYS
	// =========================================================

	fmt.Println("============== ARRAYS ==============")

	var arr [5]int = [5]int{1, 2, 3, 4, 5}
	fmt.Println(arr)

	// access
	fmt.Println(arr[0])

	// update
	arr[0] = 100
	fmt.Println(arr)

	// length
	fmt.Println(len(arr))

	// =========================================================
	// SLICES
	// =========================================================

	fmt.Println("============== SLICES ==============")

	nums := []int{1, 2, 3, 4, 5}

	// append
	nums = append(nums, 6)

	// slicing
	fmt.Println(nums[1:4])

	// copy
	copySlice := make([]int, len(nums))
	copy(copySlice, nums)

	fmt.Println(copySlice)

	// remove element index 2
	index := 2
	nums = append(nums[:index], nums[index+1:]...)

	fmt.Println(nums)

	// =========================================================
	// LOOPING
	// =========================================================

	fmt.Println("============== LOOPS ==============")

	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	for index, value := range nums {
		fmt.Println(index, value)
	}

	// =========================================================
	// MAPS
	// =========================================================

	fmt.Println("============== MAPS ==============")

	mp := map[string]int{
		"apple":  10,
		"banana": 20,
	}

	fmt.Println(mp)

	// insert
	mp["orange"] = 30

	// get
	fmt.Println(mp["apple"])

	// check exists
	value, exists := mp["grape"]

	fmt.Println(value, exists)

	// delete
	delete(mp, "banana")

	for key, value := range mp {
		fmt.Println(key, value)
	}

	// =========================================================
	// SETS
	// =========================================================

	fmt.Println("============== SETS ==============")

	// Go has no native set
	set := make(map[int]bool)

	set[1] = true
	set[2] = true

	fmt.Println(set[1])

	delete(set, 1)

	// =========================================================
	// STRINGS
	// =========================================================

	fmt.Println("============== STRINGS ==============")

	str := "hello"

	fmt.Println(len(str))
	fmt.Println(strings.ToUpper(str))
	fmt.Println(strings.ToLower(str))
	fmt.Println(strings.Contains(str, "ll"))
	fmt.Println(strings.HasPrefix(str, "he"))
	fmt.Println(strings.HasSuffix(str, "lo"))

	words := strings.Split("a,b,c", ",")
	fmt.Println(words)

	joined := strings.Join(words, "-")
	fmt.Println(joined)

	// =========================================================
	// RUNE / CHARACTER
	// =========================================================

	fmt.Println("============== RUNES ==============")

	s := "hello"

	for _, ch := range s {
		fmt.Printf("%c ", ch)
	}

	fmt.Println()

	// =========================================================
	// SORTING
	// =========================================================

	fmt.Println("============== SORTING ==============")

	values := []int{5, 1, 9, 2, 7}

	sort.Ints(values)
	fmt.Println(values)

	sort.Slice(values, func(i, j int) bool {
		return values[i] > values[j]
	})

	fmt.Println(values)

	// =========================================================
	// STRUCTS
	// =========================================================

	fmt.Println("============== STRUCTS ==============")

	type Person struct {
		Name string
		Age  int
	}

	p := Person{
		Name: "Anthony",
		Age:  25,
	}

	fmt.Println(p)

	// =========================================================
	// POINTERS
	// =========================================================

	fmt.Println("============== POINTERS ==============")

	x := 10

	ptr := &x

	fmt.Println(*ptr)

	*ptr = 20

	fmt.Println(x)

	// =========================================================
	// FUNCTIONS
	// =========================================================

	fmt.Println("============== FUNCTIONS ==============")

	fmt.Println(add(2, 3))

	a, b := swap(10, 20)

	fmt.Println(a, b)

	// =========================================================
	// STACK
	// =========================================================

	fmt.Println("============== STACK ==============")

	stack := []int{}

	// push
	stack = append(stack, 10)
	stack = append(stack, 20)

	// peek
	fmt.Println(stack[len(stack)-1])

	// pop
	top := stack[len(stack)-1]
	stack = stack[:len(stack)-1]

	fmt.Println(top)
	fmt.Println(stack)

	// =========================================================
	// QUEUE
	// =========================================================

	fmt.Println("============== QUEUE ==============")

	queue := []int{}

	// enqueue
	queue = append(queue, 1)
	queue = append(queue, 2)

	// dequeue
	front := queue[0]
	queue = queue[1:]

	fmt.Println(front)
	fmt.Println(queue)

	// =========================================================
	// HEAP / PRIORITY QUEUE
	// =========================================================

	fmt.Println("============== HEAP ==============")

	h := &MinHeap{2, 1, 5}

	heap.Init(h)

	heap.Push(h, 3)

	fmt.Println(heap.Pop(h))

	// =========================================================
	// BINARY SEARCH
	// =========================================================

	fmt.Println("============== BINARY SEARCH ==============")

	arr2 := []int{1, 3, 5, 7, 9}

	index2 := sort.SearchInts(arr2, 5)

	fmt.Println(index2)

	// =========================================================
	// PREFIX SUM
	// =========================================================

	fmt.Println("============== PREFIX SUM ==============")

	input := []int{1, 2, 3, 4}

	prefix := make([]int, len(input)+1)

	for i := 0; i < len(input); i++ {
		prefix[i+1] = prefix[i] + input[i]
	}

	fmt.Println(prefix)

	// range sum [1,3]
	fmt.Println(prefix[4] - prefix[1])

	// =========================================================
	// 2D SLICE
	// =========================================================

	fmt.Println("============== 2D SLICE ==============")

	rows, cols := 3, 4

	grid := make([][]int, rows)

	for i := range grid {
		grid[i] = make([]int, cols)
	}

	fmt.Println(grid)

	// =========================================================
	// MATH
	// =========================================================

	fmt.Println("============== MATH ==============")

	fmt.Println(math.Max(10, 20))
	fmt.Println(math.Min(10, 20))
	fmt.Println(math.Abs(-10))

	// =========================================================
	// SLIDING WINDOW
	// =========================================================

	fmt.Println("============== SLIDING WINDOW ==============")

	windowNums := []int{1, 2, 3, 4, 5}

	left := 0
	sum := 0

	for right := 0; right < len(windowNums); right++ {

		sum += windowNums[right]

		for sum > 7 {
			sum -= windowNums[left]
			left++
		}

		fmt.Println(sum)
	}

	// =========================================================
	// TWO POINTERS
	// =========================================================

	fmt.Println("============== TWO POINTERS ==============")

	two := []int{1, 2, 3, 4, 5}

	l := 0
	r := len(two) - 1

	for l < r {

		fmt.Println(two[l], two[r])

		l++
		r--
	}

	// =========================================================
	// FREQUENCY COUNT
	// =========================================================

	fmt.Println("============== FREQUENCY COUNT ==============")

	freq := map[int]int{}

	for _, num := range []int{1, 2, 2, 3, 3, 3} {
		freq[num]++
	}

	fmt.Println(freq)

	// =========================================================
	// DEFER
	// =========================================================

	fmt.Println("============== DEFER ==============")

	defer fmt.Println("Runs at end")

	fmt.Println("Before defer")

	// =========================================================
	// GOROUTINES
	// =========================================================

	fmt.Println("============== GOROUTINES ==============")

	go sayHello()

	// =========================================================
	// CHANNELS
	// =========================================================

	fmt.Println("============== CHANNELS ==============")

	ch := make(chan int)

	go func() {
		ch <- 100
	}()

	fmt.Println(<-ch)

}

// =========================================================
// FUNCTIONS
// =========================================================

func add(a int, b int) int {
	return a + b
}

func swap(a int, b int) (int, int) {
	return b, a
}

// =========================================================
// HEAP IMPLEMENTATION
// =========================================================

type MinHeap []int

func (h MinHeap) Len() int {
	return len(h)
}

func (h MinHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {

	old := *h

	n := len(old)

	item := old[n-1]

	*h = old[:n-1]

	return item
}

// =========================================================
// GOROUTINE FUNCTION
// =========================================================

func sayHello() {
	fmt.Println("Hello from goroutine")
}

// MOST IMPORTANT GO DSA PATTERNS
// Arrays/Slices
// two pointers
// sliding window
// prefix sum
// Kadane
// binary search
// HashMap
// frequency counting
// grouping
// caching
// Heap
// top K
// scheduling
// Dijkstra
// Stack
// monotonic stack
// DFS
// parsing
// Queue
// BFS
// level traversal
// Trees
// DFS recursive
// BFS iterative
// Graphs
// adjacency list
// BFS
// DFS
// union find
// topological sort
// GO INTERVIEW SUPER IMPORTANT
// Slices

// Understand deeply:

// nums := []int{1,2,3}

// sub := nums[1:]

// sub[0] = 100

// fmt.Println(nums)

// Because slices share underlying arrays.

// Interfaces

// Very important for backend interviews.

// type Animal interface {
// 	Speak()
// }
// Goroutines
// go func() {

// }()
// Channels
// ch := make(chan int)

// ch <- 1
// x := <- ch


TREES
package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(root *TreeNode) {

	if root == nil {
		return
	}

	fmt.Println(root.Val)

	dfs(root.Left)
	dfs(root.Right)
}

func main() {

	root := &TreeNode{Val: 1}

	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 3}

	dfs(root)
}
TREE BFS (LEVEL ORDER)
func levelOrder(root *TreeNode) {

	if root == nil {
		return
	}

	queue := []*TreeNode{root}

	for len(queue) > 0 {

		size := len(queue)

		for i := 0; i < size; i++ {

			node := queue[0]
			queue = queue[1:]

			fmt.Println(node.Val)

			if node.Left != nil {
				queue = append(queue, node.Left)
			}

			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}
}
BINARY SEARCH TREE
type BSTNode struct {
	Val   int
	Left  *BSTNode
	Right *BSTNode
}

func insert(root *BSTNode, val int) *BSTNode {

	if root == nil {
		return &BSTNode{Val: val}
	}

	if val < root.Val {
		root.Left = insert(root.Left, val)
	} else {
		root.Right = insert(root.Right, val)
	}

	return root
}
GRAPH

Adjacency List

graph := map[int][]int{
	1: {2,3},
	2: {4},
	3: {5},
}
GRAPH DFS
func dfs(node int, graph map[int][]int, visited map[int]bool) {

	if visited[node] {
		return
	}

	visited[node] = true

	fmt.Println(node)

	for _, nei := range graph[node] {
		dfs(nei, graph, visited)
	}
}
GRAPH BFS
func bfs(start int, graph map[int][]int) {

	queue := []int{start}

	visited := map[int]bool{
		start: true,
	}

	for len(queue) > 0 {

		node := queue[0]
		queue = queue[1:]

		fmt.Println(node)

		for _, nei := range graph[node] {

			if !visited[nei] {

				visited[nei] = true

				queue = append(queue, nei)
			}
		}
	}
}
UNION FIND (DISJOINT SET)

Very common.

type UnionFind struct {
	parent []int
	rank   []int
}

func NewUF(n int) *UnionFind {

	parent := make([]int, n)
	rank := make([]int, n)

	for i := 0; i < n; i++ {
		parent[i] = i
	}

	return &UnionFind{
		parent: parent,
		rank: rank,
	}
}

Find:

func (uf *UnionFind) Find(x int) int {

	if uf.parent[x] != x {
		uf.parent[x] = uf.Find(uf.parent[x])
	}

	return uf.parent[x]
}

Union:

func (uf *UnionFind) Union(x, y int) {

	px := uf.Find(x)
	py := uf.Find(y)

	if px == py {
		return
	}

	if uf.rank[px] < uf.rank[py] {

		uf.parent[px] = py

	} else if uf.rank[px] > uf.rank[py] {

		uf.parent[py] = px

	} else {

		uf.parent[py] = px
		uf.rank[px]++
	}
}
TRIE
type TrieNode struct {
	children map[rune]*TrieNode
	end      bool
}

type Trie struct {
	root *TrieNode
}

Constructor:

func Constructor() Trie {

	return Trie{
		root: &TrieNode{
			children: make(map[rune]*TrieNode),
		},
	}
}

Insert:

func (t *Trie) Insert(word string) {

	node := t.root

	for _, ch := range word {

		if node.children[ch] == nil {

			node.children[ch] = &TrieNode{
				children: make(map[rune]*TrieNode),
			}
		}

		node = node.children[ch]
	}

	node.end = true
}
BACKTRACKING TEMPLATE

Permutations / Combinations

func backtrack(path []int, nums []int, used []bool) {

	if len(path) == len(nums) {

		fmt.Println(path)

		return
	}

	for i := 0; i < len(nums); i++ {

		if used[i] {
			continue
		}

		used[i] = true

		path = append(path, nums[i])

		backtrack(path, nums, used)

		path = path[:len(path)-1]

		used[i] = false
	}
}
MONOTONIC STACK

Next Greater Element

stack := []int{}

for i := 0; i < len(nums); i++ {

	for len(stack) > 0 &&
		nums[stack[len(stack)-1]] < nums[i] {

		idx := stack[len(stack)-1]

		stack = stack[:len(stack)-1]

		ans[idx] = nums[i]
	}

	stack = append(stack, i)
}
TOPOLOGICAL SORT (KAHN)
graph := make(map[int][]int)

indegree := make([]int, n)

Build graph:

for _, edge := range edges {

	u := edge[0]
	v := edge[1]

	graph[u] = append(graph[u], v)

	indegree[v]++
}

BFS:

queue := []int{}

for i := 0; i < n; i++ {

	if indegree[i] == 0 {
		queue = append(queue, i)
	}
}

for len(queue) > 0 {

	node := queue[0]
	queue = queue[1:]

	for _, nei := range graph[node] {

		indegree[nei]--

		if indegree[nei] == 0 {
			queue = append(queue, nei)
		}
	}
}
GO GENERICS (GO 1.18+)

Very important now.

func Print[T any](value T) {
	fmt.Println(value)
}

Usage:

Print[int](10)

Print[string]("hello")

Generic Max:

type Number interface {
	~int | ~float64
}

func Max[T Number](a, b T) T {

	if a > b {
		return a
	}

	return b
}
POINTER RECEIVER VS VALUE RECEIVER

Value Receiver

func (p Person) Update() {
	p.Name = "new"
}

Changes copy only.

Pointer Receiver

func (p *Person) Update() {
	p.Name = "new"
}

Changes original struct.

Senior Go interviews ask this frequently.

DEFER PANIC RECOVER
func test() {

	defer func() {

		if r := recover(); r != nil {

			fmt.Println("Recovered:", r)
		}

	}()

	panic("something broke")
}


// https://claude.ai/chat/eb665e39-cc06-4e68-bfe1-71677127412b
package main

import (
	"container/heap"
	"container/list"
	"fmt"
	"math"
	"sort"
	"strings"
)

// ============================================================
// ARRAYS / SLICES
// ============================================================

func arraysAndSlices() {
	fmt.Println("**** ARRAYS / SLICES ****")

	// Fixed-size array
	arr := [5]int{1, 2, 3, 4, 5}
	fmt.Println(arr)

	// Slice (dynamic, like Python list)
	s := []int{1, 2, 3, 4, 5, 6, 7}

	// Append (like Python list.append)
	s = append(s, 10)

	// Insert at index 2 (Go has no built-in insert)
	s = append(s[:2+1], s[2:]...)
	s[2] = 21

	// Remove element at index (like Python list.remove by index)
	idx := 2
	s = append(s[:idx], s[idx+1:]...)

	// Slicing (like Python s[1:4])
	sub := s[1:4]
	fmt.Println("Subslice:", sub)

	// Iterate
	for i, v := range s {
		fmt.Println(i, v)
	}

	// 2D slice (like Python [[0]*n for _ in range(m)])
	m, n := 3, 4
	grid := make([][]int, m)
	for i := range grid {
		grid[i] = make([]int, n)
	}
	fmt.Println("2D grid:", grid)

	// Map equivalent of Python list comprehension → squares
	numbers := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	squares := make([]int, len(numbers))
	for i, v := range numbers {
		squares[i] = v * v
	}
	fmt.Println("Squares:", squares)

	// Filter (even numbers)
	var evens []int
	for _, v := range numbers {
		if v%2 == 0 {
			evens = append(evens, v)
		}
	}
	fmt.Println("Evens:", evens)

	// Reduce (sum) — no built-in, use a loop
	sum := 0
	for _, v := range numbers {
		sum += v
	}
	fmt.Println("Sum:", sum)

	// Sort ascending
	sort.Ints(s)

	// Sort descending
	sort.Sort(sort.Reverse(sort.IntSlice(s)))

	// Sort by custom key (like Python sorted(tuples, key=lambda x: x[1]))
	type Pair struct {
		Name  string
		Value int
	}
	pairs := []Pair{{"apple", 1}, {"banana", 2}, {"cherry", 3}}
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].Name > pairs[j].Name // descending by name
	})
	fmt.Println("Sorted pairs:", pairs)

	// zip equivalent
	names := []string{"Alice", "Bob", "Charlie"}
	ages := []int{30, 25, 35}
	for i := range names {
		fmt.Printf("Name: %s, Age: %d\n", names[i], ages[i])
	}

	// enumerate equivalent → use range (gives index + value)
	fruits := []string{"apple", "banana", "cherry"}
	for index, fruit := range fruits {
		fmt.Println(index, fruit)
	}

	// Python's any() / all() equivalents
	hasPositive := false
	for _, v := range numbers {
		if v > 0 {
			hasPositive = true
			break
		}
	}
	fmt.Println("Has positive:", hasPositive)

	allPositive := true
	for _, v := range numbers {
		if v <= 0 {
			allPositive = false
			break
		}
	}
	fmt.Println("All positive:", allPositive)
}

// ============================================================
// STACKS  (use a slice)
// ============================================================

func stacksDemo() {
	fmt.Println("**** STACKS ****")

	stack := []string{}

	// Push
	stack = append(stack, "23")
	stack = append(stack, "44")

	// Peek top
	top := stack[len(stack)-1]

	// Pop
	popped := stack[len(stack)-1]
	stack = stack[:len(stack)-1]

	fmt.Printf("top=%s popped=%s size=%d\n", top, popped, len(stack))
}

// ============================================================
// LINKED LIST  (use container/list or custom struct)
// ============================================================

// Custom singly-linked list node
type ListNode struct {
	Val  int
	Next *ListNode
}

func linkedListDemo() {
	fmt.Println("**** LINKED LIST ****")

	// Using container/list (doubly linked)
	ll := list.New()
	ll.PushBack(20)
	ll.PushBack(23)
	ll.PushFront(44)

	// Traverse
	for e := ll.Front(); e != nil; e = e.Next() {
		fmt.Print(e.Value, " ")
	}
	fmt.Println()

	// Remove last
	ll.Remove(ll.Back())

	// Custom singly-linked list
	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 3}

	// Traverse custom list
	for curr := head; curr != nil; curr = curr.Next {
		fmt.Print(curr.Val, " ")
	}
	fmt.Println()
}

// ============================================================
// QUEUE  (use a slice or container/list)
// ============================================================

func queueDemo() {
	fmt.Println("**** QUEUE ****")

	queue := []int{1, 2, 3, 4, 5}

	// Enqueue
	queue = append(queue, 6)

	// Dequeue (popleft)
	front := queue[0]
	queue = queue[1:]
	fmt.Println("Dequeued:", front)

	// Peek front
	_ = queue[0]

	// Print even elements
	for _, v := range queue {
		if v%2 == 0 {
			fmt.Println(v)
		}
	}
}

// ============================================================
// PRIORITY QUEUE / HEAPS  (use container/heap)
// ============================================================

// Min-heap (implements heap.Interface)
type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// Max-heap: negate values on push/pop (same trick as Python)
type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // reversed
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func heapDemo() {
	fmt.Println("**** PRIORITY QUEUE / HEAPS ****")

	// Min-heap
	minH := &MinHeap{21, 26, 1, 2}
	heap.Init(minH)
	heap.Push(minH, 5)
	fmt.Println("Min heap:", *minH)

	removed := heap.Pop(minH).(int)
	fmt.Println("Removed (min):", removed)

	// Peek (min element without removing)
	fmt.Println("Peek:", (*minH)[0])

	// Max-heap
	maxH := &MaxHeap{}
	heap.Push(maxH, 3)
	heap.Push(maxH, 1)
	heap.Push(maxH, 5)
	fmt.Println("Max heap pop:", heap.Pop(maxH).(int)) // 5

	// Heapify an existing slice
	nums := &MinHeap{10, 5, 3, 8, 2}
	heap.Init(nums)
	fmt.Println("Heapified:", *nums)

	// nLargest (like Python heapq.nlargest)
	// Sort and take tail:
	data := []int{5, 1, 3, 10, 7, 2}
	sort.Sort(sort.Reverse(sort.IntSlice(data)))
	fmt.Println("3 largest:", data[:3])

	// nSmallest
	sort.Ints(data)
	fmt.Println("3 smallest:", data[:3])
}

// ============================================================
// MAP / DICT
// ============================================================

func mapsDemo() {
	fmt.Println("**** MAP / DICT ****")

	// Create
	myMap := map[string]int{"Apple": 50, "Banana": 30, "Orange": 20}

	// Access with default (like Python dict.get(key, default))
	val, ok := myMap["Banana"]
	if !ok {
		val = 0 // default
	}
	fmt.Println("Banana:", val)

	// Add / update
	myMap["Mango"] = 60

	// Delete (like Python del dict[key] or dict.pop(key))
	delete(myMap, "Orange")

	// Iterate
	for key, value := range myMap {
		fmt.Printf("Key: %s, Value: %d\n", key, value)
	}

	// Filter (value > 25)
	filtered := map[string]int{}
	for k, v := range myMap {
		if v > 25 {
			filtered[k] = v
		}
	}
	fmt.Println("Filtered:", filtered)

	// Contains key check (like Python "key" in dict)
	_, exists := myMap["Apple"]
	fmt.Println("Has Apple:", exists)

	// Frequency counter (like Python Counter)
	words := []string{"apple", "banana", "apple", "orange"}
	count := map[string]int{}
	for _, w := range words {
		count[w]++
	}
	fmt.Println("Word count:", count)

	// Two-sum using a map
	numbers := []int{2, 7, 11, 15}
	target := 9
	seen := map[int]int{}
	for i, num := range numbers {
		if j, found := seen[target-num]; found {
			fmt.Println("Two-sum indices:", j, i)
		}
		seen[num] = i
	}

	// Nested maps
	users := map[string]map[string]any{
		"alice": {"age": 25, "city": "NY"},
		"bob":   {"age": 30, "city": "LA"},
	}
	fmt.Println("Alice city:", users["alice"]["city"])

	// Sort by key (Go maps are unordered, like Python pre-3.7)
	keys := make([]string, 0, len(myMap))
	for k := range myMap {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	fmt.Println("Sorted keys:", keys)
}

// ============================================================
// SET  (use map[T]struct{})
// ============================================================

func setDemo() {
	fmt.Println("**** SET ****")

	// Create set
	mySet := map[int]struct{}{}
	for i := 0; i < 100; i++ {
		mySet[i] = struct{}{}
	}

	// Add
	mySet[999] = struct{}{}

	// Delete (like Python set.discard)
	delete(mySet, 99)

	// Contains
	_, has := mySet[50]
	fmt.Println("Has 50:", has)

	// Set operations
	a := map[int]struct{}{1: {}, 2: {}, 3: {}}
	b := map[int]struct{}{2: {}, 3: {}, 4: {}}

	// Union
	union := map[int]struct{}{}
	for k := range a {
		union[k] = struct{}{}
	}
	for k := range b {
		union[k] = struct{}{}
	}

	// Intersection
	inter := map[int]struct{}{}
	for k := range a {
		if _, ok := b[k]; ok {
			inter[k] = struct{}{}
		}
	}

	// Difference (a - b)
	diff := map[int]struct{}{}
	for k := range a {
		if _, ok := b[k]; !ok {
			diff[k] = struct{}{}
		}
	}

	fmt.Println("Union:", union, "Intersection:", inter, "Difference:", diff)

	// String set
	strSet := map[string]struct{}{"apple": {}, "banana": {}}
	strSet["cherry"] = struct{}{}
	fmt.Println("String set:", strSet)
}

// ============================================================
// STRUCTS  (Go's OOP — no classes, just structs + methods)
// ============================================================

type Person struct {
	Name string
	Age  int
}

// Method (like Python instance method, receiver = self)
func (p Person) Greet() string {
	return fmt.Sprintf("Hi, I'm %s and I'm %d years old.", p.Name, p.Age)
}

// Pointer receiver (mutates the struct, like Python self modification)
func (p *Person) Birthday() {
	p.Age++
}

// Embedding (like Python inheritance)
type Employee struct {
	Person         // embedded — inherits Greet()
	Company string
}

func structsDemo() {
	fmt.Println("**** STRUCTS ****")

	p := Person{Name: "Alice", Age: 30}
	fmt.Println(p.Greet())
	p.Birthday()
	fmt.Println("After birthday:", p.Age)

	e := Employee{Person: Person{"Bob", 25}, Company: "Acme"}
	fmt.Println(e.Greet()) // inherited from Person
	fmt.Println("Company:", e.Company)
}

// ============================================================
// INTERFACES  (like Python duck-typing / ABCs)
// ============================================================

type Shape interface {
	Area() float64
	Perimeter() float64
}

type Circle struct{ Radius float64 }
type Rectangle struct{ Width, Height float64 }

func (c Circle) Area() float64      { return math.Pi * c.Radius * c.Radius }
func (c Circle) Perimeter() float64 { return 2 * math.Pi * c.Radius }

func (r Rectangle) Area() float64      { return r.Width * r.Height }
func (r Rectangle) Perimeter() float64 { return 2 * (r.Width + r.Height) }

func printShape(s Shape) {
	fmt.Printf("Area: %.2f, Perimeter: %.2f\n", s.Area(), s.Perimeter())
}

func interfacesDemo() {
	fmt.Println("**** INTERFACES ****")
	printShape(Circle{5})
	printShape(Rectangle{3, 4})

	// Type assertion (like Python isinstance)
	var s Shape = Circle{3}
	if c, ok := s.(Circle); ok {
		fmt.Println("It's a circle with radius:", c.Radius)
	}

	// Type switch
	shapes := []Shape{Circle{2}, Rectangle{3, 4}}
	for _, sh := range shapes {
		switch v := sh.(type) {
		case Circle:
			fmt.Println("Circle radius:", v.Radius)
		case Rectangle:
			fmt.Println("Rectangle:", v.Width, "x", v.Height)
		}
	}
}

// ============================================================
// CLOSURES  (like Python closures / lambdas)
// ============================================================

// Python: lambda x: x ** 2
var square = func(x int) int { return x * x }

// Closure capturing outer variable
func makeAdder(n int) func(int) int {
	return func(x int) int { return x + n }
}

// Decorator equivalent (higher-order function)
func withLogging(fn func(int) int) func(int) int {
	return func(x int) int {
		fmt.Printf("calling with %d\n", x)
		result := fn(x)
		fmt.Printf("result: %d\n", result)
		return result
	}
}

func closuresDemo() {
	fmt.Println("**** CLOSURES ****")
	fmt.Println(square(5))

	add5 := makeAdder(5)
	fmt.Println(add5(3)) // 8

	loggedSquare := withLogging(square)
	loggedSquare(4)

	// Anonymous function (immediately invoked, like Python lambda called inline)
	result := func(a, b int) int { return a + b }(3, 4)
	fmt.Println("Inline anon func:", result)

	// Map equivalent using a closure
	numbers := []int{1, 2, 3, 4, 5}
	doubled := make([]int, len(numbers))
	mapFn := func(x int) int { return x * 2 }
	for i, v := range numbers {
		doubled[i] = mapFn(v)
	}
	fmt.Println("Doubled:", doubled)

	// Filter equivalent
	var filtered []int
	for _, v := range numbers {
		if v%2 == 0 {
			filtered = append(filtered, v)
		}
	}
	fmt.Println("Filtered evens:", filtered)

	// Reduce equivalent
	reduce := func(nums []int, fn func(int, int) int) int {
		acc := nums[0]
		for _, v := range nums[1:] {
			acc = fn(acc, v)
		}
		return acc
	}
	product := reduce(numbers, func(a, b int) int { return a * b })
	fmt.Println("Product:", product)
}

// ============================================================
// GOROUTINES & CHANNELS  (Go's concurrency — no Python equiv)
// ============================================================

func goroutinesDemo() {
	fmt.Println("**** GOROUTINES & CHANNELS ****")

	// Basic goroutine (like Python threading.Thread but lighter)
	done := make(chan bool)
	go func() {
		fmt.Println("Hello from goroutine!")
		done <- true
	}()
	<-done // wait

	// Buffered channel
	ch := make(chan int, 3)
	ch <- 1
	ch <- 2
	ch <- 3
	close(ch)
	for v := range ch {
		fmt.Println("Channel value:", v)
	}

	// Fan-out pattern
	jobs := make(chan int, 5)
	results := make(chan int, 5)

	// Worker goroutine
	go func() {
		for j := range jobs {
			results <- j * j
		}
		close(results)
	}()

	for i := 1; i <= 5; i++ {
		jobs <- i
	}
	close(jobs)

	for r := range results {
		fmt.Println("Result:", r)
	}

	// select (like Python asyncio.wait)
	ch1 := make(chan string, 1)
	ch2 := make(chan string, 1)
	ch1 <- "one"
	ch2 <- "two"
	select {
	case msg := <-ch1:
		fmt.Println("Received from ch1:", msg)
	case msg := <-ch2:
		fmt.Println("Received from ch2:", msg)
	}
}

// ============================================================
// ERRORS  (Go has no exceptions — explicit error returns)
// ============================================================

// Python: raise ValueError("bad input")
// Go: return error values

type ValidationError struct {
	Field   string
	Message string
}

func (e *ValidationError) Error() string {
	return fmt.Sprintf("validation error: %s — %s", e.Field, e.Message)
}

func divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, &ValidationError{Field: "b", Message: "cannot divide by zero"}
	}
	return a / b, nil
}

func errorsDemo() {
	fmt.Println("**** ERRORS ****")

	result, err := divide(10, 2)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("10 / 2 =", result)
	}

	_, err = divide(10, 0)
	if err != nil {
		fmt.Println("Error:", err)
		// Type assertion on error (like Python except ValueError)
		if ve, ok := err.(*ValidationError); ok {
			fmt.Println("Field that failed:", ve.Field)
		}
	}
}

// ============================================================
// SORTING  (like Python sort / bisect)
// ============================================================

func sortingDemo() {
	fmt.Println("**** SORTING ****")

	// sort.Ints, sort.Strings, sort.Float64s
	nums := []int{5, 2, 9, 1, 7}
	sort.Ints(nums)
	fmt.Println("Ascending:", nums)

	sort.Sort(sort.Reverse(sort.IntSlice(nums)))
	fmt.Println("Descending:", nums)

	// Custom comparator (like Python sorted(key=lambda))
	words := []string{"banana", "apple", "cherry", "kiwi"}
	sort.Slice(words, func(i, j int) bool {
		return len(words[i]) < len(words[j]) // sort by length
	})
	fmt.Println("By length:", words)

	// cmp_to_key equivalent: just write the Less func directly
	// For stable sort:
	sort.SliceStable(words, func(i, j int) bool {
		return words[i] < words[j]
	})

	// Binary search (like Python bisect.bisect_left)
	sorted := []int{1, 3, 4, 4, 7}
	target := 4
	// sort.SearchInts returns the smallest index where sorted[i] >= target
	leftIdx := sort.SearchInts(sorted, target)
	fmt.Println("bisect_left index:", leftIdx) // 2

	// bisect_right: first index where sorted[i] > target
	rightIdx := sort.SearchInts(sorted, target+1)
	fmt.Println("bisect_right index:", rightIdx) // 4

	// Check if value exists
	if leftIdx < len(sorted) && sorted[leftIdx] == target {
		fmt.Println("Value found at index:", leftIdx)
	}
}

// ============================================================
// STRINGS  (like Python str methods)
// ============================================================

func stringsDemo() {
	fmt.Println("**** STRINGS ****")

	s := "hello world"

	fmt.Println(strings.ToUpper(s))             // HELLO WORLD
	fmt.Println(strings.ToLower("HELLO"))        // hello
	fmt.Println(strings.TrimSpace("  hi  "))     // hi
	fmt.Println(strings.Contains(s, "world"))    // true
	fmt.Println(strings.HasPrefix(s, "hello"))   // true (startswith)
	fmt.Println(strings.HasSuffix(s, "world"))   // true (endswith)
	fmt.Println(strings.Replace(s, "l", "L", -1)) // replaceAll
	fmt.Println(strings.Count(s, "l"))           // 3
	fmt.Println(strings.Index(s, "o"))           // 4
	fmt.Println(strings.Split("a,b,c", ","))     // [a b c]
	fmt.Println(strings.Join([]string{"a", "b"}, ",")) // a,b
	fmt.Println(len(s))                          // 11

	// String slicing (like Python s[1:4])
	fmt.Println(s[1:4]) // ell

	// Reverse a string
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	fmt.Println("Reversed:", string(runes))

	// Rune vs byte (Go strings are UTF-8)
	// Use []rune for Unicode-safe operations
	emoji := "hello 🌍"
	fmt.Println("Bytes:", len(emoji))       // byte count
	fmt.Println("Runes:", len([]rune(emoji))) // character count

	// String builder (like Python "".join([...]))
	var sb strings.Builder
	for _, word := range []string{"Go", "is", "fast"} {
		sb.WriteString(word)
		sb.WriteString(" ")
	}
	fmt.Println(strings.TrimSpace(sb.String()))

	// String → []byte and back
	b := []byte(s)
	b[0] = 'H'
	fmt.Println(string(b)) // Hello world

	// isDigit / isAlpha equivalents (from unicode package)
	// import "unicode"
	// unicode.IsDigit(r), unicode.IsLetter(r), unicode.IsUpper(r), unicode.IsLower(r)

	// Rotate string right by k (like Python s[-k:] + s[:-k])
	rotateString := func(x string, k int) string {
		n := len(x)
		if n == 0 {
			return x
		}
		k = ((k % n) + n) % n // handle negatives
		return x[n-k:] + x[:n-k]
	}
	fmt.Println(rotateString("abcdef", 2)) // efabcd
}

// ============================================================
// DEFAULT / GROUPED MAPS  (like Python defaultdict)
// ============================================================

func defaultDictDemo() {
	fmt.Println("**** DEFAULT / GROUPED MAPS ****")

	// defaultdict(int) equivalent — just use map[string]int, zero value is 0
	count := map[string]int{}
	words := []string{"apple", "banana", "apple", "orange"}
	for _, w := range words {
		count[w]++ // no KeyError, zero value is 0
	}
	fmt.Println("Word count:", count)

	// defaultdict(list) equivalent
	group := map[int][]string{}
	for _, word := range words {
		group[len(word)] = append(group[len(word)], word)
	}
	fmt.Println("Grouped by length:", group)
}

// ============================================================
// ORDERED MAP  (Go maps are unordered; maintain insertion order manually)
// ============================================================

type OrderedMap struct {
	keys   []string
		m      map[string]int
}

func NewOrderedMap() *OrderedMap {
	return &OrderedMap{m: map[string]int{}}
}

func (om *OrderedMap) Set(key string, val int) {
	if _, ok := om.m[key]; !ok {
		om.keys = append(om.keys, key)
	}
	om.m[key] = val
}

func (om *OrderedMap) Get(key string) (int, bool) {
	v, ok := om.m[key]
	return v, ok
}

func (om *OrderedMap) Items() []struct {
	Key string
	Val int
} {
	out := make([]struct{ Key string; Val int }, len(om.keys))
	for i, k := range om.keys {
		out[i] = struct{ Key string; Val int }{k, om.m[k]}
	}
	return out
}

func orderedMapDemo() {
	fmt.Println("**** ORDERED MAP ****")
	om := NewOrderedMap()
	om.Set("apple", 3)
	om.Set("banana", 2)
	om.Set("orange", 4)

	for _, item := range om.Items() {
		fmt.Printf("%s: %d\n", item.Key, item.Val)
	}
}

// ============================================================
// GENERICS  (Go 1.18+ — like Python type hints + flexibility)
// ============================================================

// Generic Map function (like Python map())
func Map[T, U any](s []T, f func(T) U) []U {
	result := make([]U, len(s))
	for i, v := range s {
		result[i] = f(v)
	}
	return result
}

// Generic Filter
func Filter[T any](s []T, f func(T) bool) []T {
	var result []T
	for _, v := range s {
		if f(v) {
			result = append(result, v)
		}
	}
	return result
}

// Generic Reduce
func Reduce[T, U any](s []T, init U, f func(U, T) U) U {
	acc := init
	for _, v := range s {
		acc = f(acc, v)
	}
	return acc
}

func genericsDemo() {
	fmt.Println("**** GENERICS (Go 1.18+) ****")

	nums := []int{1, 2, 3, 4, 5}

	squared := Map(nums, func(x int) int { return x * x })
	fmt.Println("Squared:", squared)

	evens := Filter(nums, func(x int) bool { return x%2 == 0 })
	fmt.Println("Evens:", evens)

	sum := Reduce(nums, 0, func(acc, x int) int { return acc + x })
	fmt.Println("Sum:", sum)

	// Works with strings too
	words := []string{"hello", "world", "go"}
	upper := Map(words, strings.ToUpper)
	fmt.Println("Upper:", upper)
}

// ============================================================
// CODING SHORTCUTS  (common interview patterns)
// ============================================================

func codingShortcuts() {
	fmt.Println("**** CODING SHORTCUTS ****")

	// Infinity
	posInf := math.MaxInt
	negInf := math.MinInt
	floatInf := math.Inf(1)
	fmt.Println(posInf, negInf, floatInf)

	// Swap without temp
	a, b := 3, 7
	a, b = b, a
	fmt.Println("Swapped:", a, b)

	// Multiple return values (unique to Go)
	minMax := func(nums []int) (int, int) {
		mn, mx := nums[0], nums[0]
		for _, v := range nums[1:] {
			if v < mn {
				mn = v
			}
			if v > mx {
				mx = v
			}
		}
		return mn, mx
	}
	mn, mx := minMax([]int{3, 1, 4, 1, 5, 9})
	fmt.Println("Min:", mn, "Max:", mx)

	// defer (like Python context managers / finally)
	defer fmt.Println("Deferred: runs at end of function")

	// Pointer basics (Go has pointers, Python doesn't)
	x := 42
	ptr := &x   // address of x
	*ptr = 100  // dereference and modify
	fmt.Println("Modified via pointer:", x)

	// init a 2D DP table (like Python [[0]*(n+1) for _ in range(m+1)])
	m, n := 3, 4
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	fmt.Println("DP table row 0:", dp[0])

	// zfill equivalent: fmt.Sprintf
	fmt.Printf("zfill: %05d\n", 42)  // 00042

	// String padding
	fmt.Printf("rjust: %10s\n", "abc")  // right-justify
	fmt.Printf("ljust: %-10s|\n", "abc") // left-justify

	// Bitmask operations (same as Python)
	fmt.Println("AND:", 5&3)   // 1
	fmt.Println("OR:", 5|3)    // 7
	fmt.Println("XOR:", 5^3)   // 6
	fmt.Println("LEFT:", 1<<3) // 8
	fmt.Println("RIGHT:", 8>>2) // 2
}

// ============================================================
// MEMOIZATION  (like Python @lru_cache)
// ============================================================

// Manual memoization with a map (Go has no built-in decorator)
func memoDemo() {
	fmt.Println("**** MEMOIZATION ****")

	cache := map[int]int{}

	var fib func(n int) int
	fib = func(n int) int {
		if n <= 1 {
			return n
		}
		if v, ok := cache[n]; ok {
			return v
		}
		result := fib(n-1) + fib(n-2)
		cache[n] = result
		return result
	}

	fmt.Println("Fib(10):", fib(10))
	fmt.Println("Fib(30):", fib(30))

	// Generic memoize wrapper (Go 1.18+)
	memoize := func(fn func(int) int) func(int) int {
		cache := map[int]int{}
		return func(n int) int {
			if v, ok := cache[n]; ok {
				return v
			}
			result := fn(n)
			cache[n] = result
			return result
		}
	}

	expensiveSquare := memoize(func(x int) int {
		return x * x
	})
	fmt.Println("Memoized square(7):", expensiveSquare(7))
}

// ============================================================
// ITERTOOLS EQUIVALENTS
// ============================================================

func itertoolsDemo() {
	fmt.Println("**** ITERTOOLS EQUIVALENTS ****")

	// permutations([1,2,3], 2)
	var permutations func([]int, int) [][]int
	permutations = func(arr []int, r int) [][]int {
		if r == 0 {
			return [][]int{{}}
		}
		var result [][]int
		for i, v := range arr {
			rest := append(append([]int{}, arr[:i]...), arr[i+1:]...)
			for _, p := range permutations(rest, r-1) {
				result = append(result, append([]int{v}, p...))
			}
		}
		return result
	}
	fmt.Println("Perms of [1,2,3] r=2:", permutations([]int{1, 2, 3}, 2))

	// combinations([1,2,3], 2)
	var combinations func([]int, int) [][]int
	combinations = func(arr []int, r int) [][]int {
		if r == 0 {
			return [][]int{{}}
		}
		var result [][]int
		for i, v := range arr {
			for _, c := range combinations(arr[i+1:], r-1) {
				result = append(result, append([]int{v}, c...))
			}
		}
		return result
	}
	fmt.Println("Combos of [1,2,3] r=2:", combinations([]int{1, 2, 3}, 2))

	// chain([1,2],[3,4]) → just append slices
	a := []int{1, 2}
	b2 := []int{3, 4}
	chained := append(a, b2...)
	fmt.Println("Chained:", chained)

	// zip (already shown in arrays section)

	// groupby equivalent
	data := []struct{ Key, Val string }{{"a", "1"}, {"a", "2"}, {"b", "3"}}
	grouped := map[string][]string{}
	for _, d := range data {
		grouped[d.Key] = append(grouped[d.Key], d.Val)
	}
	fmt.Println("Grouped:", grouped)
}

// ============================================================
// MAIN
// ============================================================

func main() {
	arraysAndSlices()
	stacksDemo()
	linkedListDemo()
	queueDemo()
	heapDemo()
	mapsDemo()
	setDemo()
	structsDemo()
	interfacesDemo()
	closuresDemo()
	goroutinesDemo()
	errorsDemo()
	sortingDemo()
	stringsDemo()
	defaultDictDemo()
	orderedMapDemo()
	genericsDemo()
	codingShortcuts()
	memoDemo()
	itertoolsDemo()
}
// https://claude.ai/chat/eb665e39-cc06-4e68-bfe1-71677127412b


// https://chatgpt.com/c/6a193d56-8560-83a3-a65e-5911bf9c4b5d