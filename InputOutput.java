import java.util.Scanner;
public class InputOutput {
    public static void main(String[] arge) {

        /* Print/Output a line with line break
         
Use "sout" shortcurt/
      System.out.println("This prints and breaks line");
      / Print the word without line break */
      System.out.print("This will not break the line");
      System.out.print("This line will continue\n");

        /* Output formating
         
System.out.printf()
%s String, %d integral, %f floating point, %b boolean
This will not break the line too/
  System.out.printf("The next word is %s", "New word");
  System.out.printf("The next int is %d", 10);
  / You can use multiple formatter */
  System.out.printf("Multiple %f %b", 10.9f, false);

        /* User input using Scanner 
         
first import the Scanner class
import java.util.scanner: // at the top of the line*/
    Scanner scan = new Scanner(System.in); // System.in is used as input
    System.out.println("The following takes one word from sentence");
    String oneword = scan.next();
    System.out.println(oneword);
    System.out.println("The following takes whole sentence");
    String wholeSentence = scan.nextLine();
    System.out.println(wholeSentence);
    System.out.println("The following takes int");
    int intInput = scan.nextInt();
    System.out.println(intInput);
    System.out.println("The following takes boolean");
    boolean booleanInput = scan.nextBoolean();
    System.out.println(booleanInput);
    scan.close();}
}