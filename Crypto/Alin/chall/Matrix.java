import java.util.Scanner;

public class Matrix {
    static Scanner input = new Scanner(System.in);

    public static int[][] multiply(int[][] a, int[][] b){
        int x = a.length;
        int y = b[0].length;
        int z = y;
        int[][] result = new int[x][y];
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                for (int k = 0; k < z; k++) {
                    result[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return result;
    }

    public static int[][][] string_to_matrix(String text){
        
        int[][][] matrix = new int[text.length() / 9][3][3];
        for (int i = 0; i < text.length(); i += 9){
            int[][] matrices = new int[3][3];
            for (int j = 0; j < 9; j++) matrices[j / 3][j % 3] = (int)text.charAt(i + j);
            matrix[i / 9] = matrices;
        }
        return matrix;
    }

    public static void main(String[] args) {
        System.out.print("plaintext: ");
        String plaintext = input.nextLine();

        if (plaintext.length() % 9 != 0) 
            plaintext += "?".repeat(9 - (plaintext.length() % 9));
        
        int[] cipher = new int[plaintext.length()];

        int[][][] mat = string_to_matrix(plaintext);

        for (int i = 0; i < mat.length; i++){
            int[][] A = mat[i];
            int[][] B = mat[0];
            int[][] C = multiply(A, B);
            for (int j = 0; j < 3; j++){
                for (int k = 0; k < 3; k++){
                    cipher[i * 9 + j * 3 + k] = C[j][k];
                }
            }
        }

        System.out.print("ciphertext: ");
        for (int i = 0; i < cipher.length; i++){
            System.out.print(cipher[i] + " ");
        }
    }
}
