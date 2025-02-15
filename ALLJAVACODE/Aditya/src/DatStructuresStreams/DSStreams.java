package DatStructuresStreams;

import java.util.ArrayDeque;
import java.util.ArrayList;

// FORMAT cmd+shift+F

import java.util.Arrays;
import java.util.BitSet;
import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.OptionalInt;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Random;
import java.util.Set;
import java.util.Stack;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


public class DSStreams {

	public static void main(String[] args) {
		System.out.println("**********************ARRAYS*************************");

		int array[] = new int[5];
		
		for (int i = 0; i < array.length; i++) {
			array[i] = i + 3;
		}

		int ar[][] = new int[2][3];

		for (int i[] : ar)
			Arrays.fill(i, -1);

		char ar2[][] = { { 'a', 'b' }, { 'c', 'd' }, { 'e', 'b' } };

		Arrays.sort(array);
		for (int i : array) {
			System.out.print(i + " ");
		}

		IntStream stream = Arrays.stream(array);
		stream.forEach(System.out::print);
		
		List list = Arrays.asList(array);
		System.out.println(list);
		
		ArrayList al2 = new ArrayList<>(Arrays.asList(array) );
		
		ArrayList al = new ArrayList<>();
		Collections.addAll(al, array);
		
		ArrayList<Integer> al3 = Arrays.stream(array) // Stream of int
                .boxed() // Convert to Integer
                .collect(Collectors.toCollection(ArrayList::new)); // Collect to ArrayList
		
		
		List<Integer> listSt = Arrays.asList(1, 3, 4, 5, 6);
		System.out.println();
		System.out.println();
		System.out.println("**********************STACKS*************************");
		
//		STACKS
		Stack<Integer> st = new Stack<>();
		Random random = new Random();
		
		IntStream randomStream = random.ints(10,0,12);
		randomStream.forEach(st::push);
		
		st.push(43);
		System.out.print(st.peek()+"--"+st.pop()+"???"+st.search(20)+" ");
//		st.forEach(System.out::print); 
		st.forEach(element -> System.out.print(element+  " "));

	
		OptionalInt indexOpt = IntStream.range(0, st.size())
	            .filter(i -> st.get(i) == 20)
	            .findFirst(); 
		System.out.println();
		System.out.println();
		
		System.out.println("**********************LINKED LISTS*************************");
		LinkedList<Integer> ll = new LinkedList<>();
		
		ll.add(23);
		ll.addFirst(11);
		ll.addLast(90);
		ll.add(1, 9999);
		System.out.println(ll);
		ll.addAll(st);
		System.out.println(ll);
		
		ll.remove();
		ll.removeFirst();
		ll.removeLast();
		
		System.out.println(ll);
		System.out.println(ll.getFirst()+"      "+ll.getLast() +" "+ ll.get(2));
		
		List<Integer> filterdNumbers = ll.stream().filter(x -> x>=50).map(x -> x*x*x).collect(Collectors.toList());
		System.out.println(filterdNumbers);

		System.out.println("**********************QUEUE *************************");
		
		Queue<Integer> queue = new LinkedList<>();
		
		queue.addAll(ll);
		queue.offer(2322);
		System.out.println(queue);
		System.out.println(queue.size() +" " + queue.contains(90)+ " "+ queue.poll() + " "+ queue.peek() +queue.poll() );
		
		System.out.println("**********************PRIORITY QUEUE/ HEAPS *************************");
		PriorityQueue<Integer> minHeap = new PriorityQueue<>();	
		minHeap.addAll(listSt);
		System.out.println(minHeap);
				
		
		PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
//		PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b)-> a-b);
		IntStream.generate(() -> random.nextInt(100)) // Random numbers between 0 and 99
        .limit(10)                          // Limit to 10 numbers
        .forEach(maxHeap::add); 
		
		System.out.println(maxHeap);
		System.out.println(maxHeap.poll() +" " + minHeap.size() + " " + maxHeap.peek());
		
		
		System.out.println("**********************DEQUEUE *************************");
		
		Deque<Integer> dq = new ArrayDeque<>();
		
		dq.addFirst(22);
		dq.addFirst(11);
		dq.addLast(23);
		dq.addLast(89);
		
		System.out.println(dq);
		System.out.println(dq.peekFirst() + " " +	dq.peekLast());
		
		dq.removeFirst();
		dq.removeLast();
		
		dq.removeIf(x->x<0);
		System.out.println(dq);
		
		System.out.println("**********************MAP/DICT *************************");
		
		Map<String, Integer> map = new HashMap<>();
		map.put("a", 1);
		map.put("b", 2);
		map.put("c", 3);
		map.put("d", 4);
		
		System.out.println("Price of a: " + map.get("a"));  // Output: 50

        System.out.println("Contains key 'd'? " + map.containsKey("d"));  // Output: true
        
        map.remove("b");
        
        for(Map.Entry<String, Integer> entry : map.entrySet() ) {
        	System.out.print(entry.getKey());
        	System.out.println(entry.getValue());
        }
        
        System.out.println(map);
        
        Map<String, Integer> filteredMap = map.entrySet()
                .stream()
                .filter(entry -> entry.getValue() > 25)
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));

		
		filteredMap.forEach((k, v) -> System.out.println("Key: " + k + ", Value: " + v));
		System.out.println("-----------------");
		
		for (String key : map.keySet()) {
		    System.out.println("Key: " + key);
		}
		for (Integer value : map.values()) {
		    System.out.println("Value: " + value);
		}
		
		map.forEach((key, value) -> {
		    System.out.println("Key: " + key + ", Value: " + value);
		});
		
		System.out.println("**********************TREE MAP *************************");
		
		TreeMap<String, Integer> tm = new TreeMap<>();
		tm.put("Apple", 50);
		tm.put("Banana", 30);
		tm.put("Orange", 20);
		tm.put("Grapes", 40);
		
		System.out.println(tm);
		
		for(Map.Entry<String, Integer> entry: map.entrySet()) {
			System.out.println(entry.getKey() + " " + entry.getValue());
		}
		for(int i: tm.values()) {
			System.out.println(i);
		}
		
		System.out.println("**********************HASH SET *************************");
		
		Set<Integer> set = new HashSet<>();
		set.addAll(ll);
		
		set.forEach(item->System.out.print(item+" "));
		
		Set<Integer> filteredSet = set.stream()
				.filter(x->x>10)
				.collect(HashSet::new, HashSet::add, HashSet::addAll);
		
		System.out.println(filteredSet);
		
		System.out.println("**********************TREE SET *************************");
		
		TreeSet<Integer> ts = new TreeSet<>();
		
		IntStream randomStream2 = random.ints(10,0 ,12);
		randomStream2.forEach(ts::add);
		
		System.out.println(ts);
		
		System.out.println("First element: " + ts.first()); // Output: 2
	    System.out.println("Last element: " + ts.last()); // Output: 10
		
		System.out.println("**********************BIT SET *************************");
		
		BitSet bitSet1 = new BitSet();
        BitSet bitSet2 = new BitSet();
        

        // Set bits at specific positions
        bitSet1.set(1);
        bitSet1.set(3);
        bitSet1.set(5);

        bitSet2.set(2);
        bitSet2.set(3);
        bitSet2.set(6);

        System.out.println("BitSet1: " + bitSet1);  // Output: {1, 3, 5}
        System.out.println("BitSet2: " + bitSet2);  // Output: {2, 3, 6}

        // AND operation between BitSet1 and BitSet2
        bitSet1.and(bitSet2);
        System.out.println("After AND: " + bitSet1);  // Output: {3}

        // Set a bit and check its value
        bitSet1.set(4);
        System.out.println("Bit at index 4: " + bitSet1.get(4));  // Output: true

        // Flip a bit
        bitSet1.flip(3);
        System.out.println("After flipping index 3: " + bitSet1);  // Output: {4}

        // Get cardinality (number of set bits)
        System.out.println("Cardinality: " + bitSet1.cardinality());  // Output: 1

        // Clear all bits
        bitSet1.clear();
        System.out.println("After clear: " + bitSet1);  // Output: {}
		
	}

}
