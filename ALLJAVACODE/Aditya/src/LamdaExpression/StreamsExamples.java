package LamdaExpression;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class StreamsExamples {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int sum = IntStream.rangeClosed(0, 100).sum();
		System.out.println(sum);
		List<Integer> al = Arrays.asList(1,1,1,2,3,4,5,11,6,7,8,9);
		
		List<Integer> unique = al.stream().distinct().collect(Collectors.toList());
		System.out.println(unique);
	}
}
