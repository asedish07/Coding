import java.util.Scanner;
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int[] numlst = new int[n];
    for (int i=0; i<n; i++) {
      numlst[i] = sc.nextInt();
    }
    int M = 0, Y = 0;
    for (int i=0; i<n; i++) {
      Y += 10 * ((numlst[i] / 30) + 1);
      M += 15 * ((numlst[i] / 60) + 1);
    }
    if (M<Y) {
      System.out.printf("M %d", M);
    }
    else if (M == Y) {
      System.out.printf("Y M %d", Y);
    }
    else {
      System.out.printf("Y %d", Y);
    }
  }
}