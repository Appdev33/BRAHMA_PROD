package DatStructuresStreams;

import java.util.Arrays;
import java.util.List;
import java.util.function.Supplier;
import java.util.stream.DoubleStream;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.util.stream.Stream;

public class StreamsApi {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		List<Integer> al  = Arrays.asList(1,3,5,7,9,11,13,15,17,19);
		
		System.out.println(al.stream().reduce( (a,b) ->a+b));
		
		System.out.println(al.stream().reduce( (x,y) -> x>y ?x:y));
		
		System.out.println(al.stream().limit(7).skip(2).reduce((x,y) -> x>y ?x:y));
		
		System.out.println(al.stream().limit(7).skip(5).reduce((x,y) -> x+y));  //11,13
		
		
		System.out.println(al.stream().anyMatch(x->x>5)); 
		System.out.println(al.stream().allMatch(x->x>5)); 
		System.out.println(al.stream().noneMatch(x->x>50)); 
		
		
		System.out.println(al.stream().filter(x -> x > 10).findAny());

		System.out.println(al.stream().filter(x -> x > 10).findFirst());
		
		String strs[] = {"10","0001","111001","1","0"};
		
		int zeros = (int) strs[1].chars().filter(ch -> ch == '0').count();
		System.out.println(zeros);
		
		Stream<String> stringStream = Stream.of("adam" , "eve", "barca", "lots");
		stringStream.forEach(System.out::println);
		
		long count = Stream.iterate(1,x->x*2)
		.limit(10).count();
		System.out.println(count);
		
//		Stream.generate((Supplier<? extends T>) al).count();
		
		System.out.println(IntStream.rangeClosed(1,20).sum());
		System.out.println(LongStream.rangeClosed(1,20));
		IntStream.rangeClosed(1,20).asDoubleStream().forEach(System.out::print);
		System.out.println("###############");
		Stream.iterate(1, x->x*2).limit(10).forEach(System.out::println);
		

	}

}
