public class QuickSort {

    public static void sort(int[] vetor, int inicio, int fim) { //array , 0, array.lenght -1
        if(fim > inicio) {
            int indexPivo = dividir(vetor, inicio, fim);
            sort(vetor, inicio, indexPivo - 1);
            sort(vetor, indexPivo + 1, fim);
        }
    }

    private static int dividir(int[] vetor, int inicio, int fim) {
        int pivo, pontEsq, pontDir = fim;
        pontEsq = inicio + 1;
        pivo = vetor[inicio];

        while(pontEsq <= pontDir) {
            while(pontEsq <= pontDir && vetor[pontEsq] <= pivo) {
                pontEsq++;
            }

            while(pontDir >= pontEsq && vetor[pontDir] > pivo) {
                pontDir--;
            }

            if(pontEsq < pontDir) {
                trocar(vetor, pontDir, pontEsq);
                pontEsq++;
                pontDir--;
            }
        }

        trocar(vetor, inicio, pontDir);
        return pontDir;
    }

    private static void trocar(int[] vetor, int i, int j) {
        int temp = vetor[i];
        vetor[i] = vetor[j];
        vetor[j] = temp;
    }
}
