
import java.util.*;

public class Main {

    public static void sortByDept(String[][] arr) {

        Arrays.sort(arr, new Comparator<String[]>() {
            @Override
            public int compare(String[] a, String[] b) {


                int dept = a[1].compareTo(b[1]);
                if (dept != 0) {
                    return dept;
                }
                double scoreA = Double.parseDouble(a[2]);
                double scoreB = Double.parseDouble(b[2]);

                if (scoreA != scoreB) {
                    return Double.compare(scoreB, scoreA);
                }
                return a[0].compareTo(b[0]);
            }
        });
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        String[][] arr = new String[n][3];

        for (int i = 0; i < n; i++) {

            String k = sc.nextLine();

            String[] parts = k.split(",");
            arr[i][0] = parts[0];
            arr[i][1] = parts[1];
            arr[i][2] = parts[2];
        }

        sortByDept(arr);

        for (int i = 0; i < n; i++) {
            System.out.println(
                    arr[i][0] + "," +
                            arr[i][1] + "," +
                            arr[i][2]
            );
        }
    }
}
