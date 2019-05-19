import java.util.Scanner;

public class practice {

	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);

		/*
	  	#예시
	  	#입력할 진법(2/8/10/16) : 16
	  	#입력값 : ff
	  	#변환할 진법(2/8/10/16) : 2
	  	#결과 : ff(16) -> 0b11111111(2)
		 */

		System.out.print("입력할 진법(2/8/10/16) : ");
		int a = scan.nextInt();
		scan.nextLine();
		System.out.print("입력값 : ");
		String b = scan.nextLine();
		int b1 = Integer.parseInt(b, a);
		String b2 = Integer.toString(b1, a);
		System.out.print("변환할 진법(2/8/10/16) : ");
		int c = scan.nextInt();
		String d = Integer.toString(b1, c);
		System.out.println( "결과 : " + b2 + "(" + a + ")" + "->" + d + "(" + c + ")");
		// 결과 : ff(16) -> 0b11111111(2)
	}

}
