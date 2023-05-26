import java.util.Random;

public class CriaArray {
    Random random = new Random();

    public int[] quaseOrdenado(int i){
        int[] array = new int[i];
        int porcento = (i * 8)/100;
        int guard;

        for(int j = 0; j < i; j++){
            array[j] = j + 1;
        }

        for(int j = 0; j < porcento; j++){
            guard = array[j];
            while (array[j] == guard)
                array[j] = random.nextInt(i * 100);
        }

        return array;
    }

    public int[] desordenado(int i){
        int[] array = new int[i];

        for(int j = 0; j < i; j++){
            array[j] = random.nextInt(i * 100);
        }
        return array;
    }

    public int[] decrescente(int i){
        int[] array = new int[i];
        int preenche = i;

        for(int j = 0; j < i; j++){
            array[j] = preenche;
            preenche--;
        }

        return array;
    }
}
