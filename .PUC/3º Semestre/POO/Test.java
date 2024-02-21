import java.util.ArrayList;
import java.util.Random;

public class Test {
    
    public static void main(String[] args) {
        System.out.println("---Par / Impar / Multiplo de 3---");
        
        ArrayList<Integer> lista = new ArrayList<>();
        ArrayList<Integer> multi3 = new ArrayList<>();
        ArrayList<Integer> par = new ArrayList<>();
        ArrayList<Integer> impar = new ArrayList<>();

        Random random = new Random();

        for (int i = 0; i < 10; i++) {

            int numeroAleatorio = random.nextInt(100) + 1;
            lista.add(numeroAleatorio);
            System.out.println(lista.get(i));
        }


        for (int valor : lista) {
            if (valor % 3 == 0) {
                multi3.add(valor);
            } 
            else if (valor % 2 == 0) {
                par.add(valor);
            } 
            else {
                impar.add(valor);
            }
        }
        
          System.out.println("Os números " + multi3 + " são multiplos de 3");  
          System.out.println("Os números " + par + " são pares");  
          System.out.println("Os números " + impar + "são impares");  
    }



}


