import java.util.Scanner;

public class IMC {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Qual a sua altura? (Em CM)");
        double altura = teclado.nextDouble();

        System.out.print("Qual o seu sexo?\n [1] Masculino\n [2] Feminino");
        String sexo = teclado.nextLine();

        int num;

        if (sexo == "masulino"){
            num = 1;
        }

        else{
            num = 2;
        }

        double peso = 0;

        if (num == 1){
            peso = ((72.7 * altura) - 58);
        }
        else if (num == 2){
            peso = ((62.1 * altura) - 44.7);
        }
        else{
            
        }

        

        System.out.println("Seu peso ideal é: " + peso);




    }



}