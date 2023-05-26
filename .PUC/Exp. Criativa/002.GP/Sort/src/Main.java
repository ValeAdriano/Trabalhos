import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        CriaArray arrays = new CriaArray();
        Scanner input = new Scanner(System.in);

        System.out.print("Digite o tamanho dos arrays: ");
        String tamanhoString = input.next();
        System.out.println("");

        int tamanho = Integer.parseInt(tamanhoString);

        int[] quaseOrdenado = arrays.quaseOrdenado(tamanho);
        int[] desordenado = arrays.desordenado(tamanho);
        int[] decrescente = arrays.decrescente(tamanho);

        int[] qo = quaseOrdenado;
        int[] ds = desordenado;
        int[] dc = decrescente;

        long tempo1;
        long tempo2;

        System.out.println("//--------------------------------------------------//");
        System.out.println("Tempo dos algoritmos com conjuntos quase ordenados:");

        try {
            tempo1 = System.currentTimeMillis();
            QuickSort.sort(qo, 0, qo.length - 1);
            tempo2 = System.currentTimeMillis();
            System.out.println("Tempo do QuickSort: " + (tempo2 - tempo1) + " ms");
        }
        catch (StackOverflowError error) {
            System.out.println("Erro de Stack Overflow no QuickSort");
        }

        tempo1 = System.currentTimeMillis();
        ShellSort.sort(qo);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do ShellSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        HeapSort.sort(qo);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do HeapSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        MergeSort.sort(qo, qo.length-1);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do MergeSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        InsertSort.sort(qo);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do InsertSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        SelectionSort.sort(qo);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do SelectionSort: " + (tempo2 - tempo1) + " ms");

        System.out.println("//--------------------------------------------------//");

        System.out.println("Tempo dos algoritmos com conjuntos desordenados:");

        try {
            tempo1 = System.currentTimeMillis();
            QuickSort.sort(ds, 0, qo.length - 1);
            tempo2 = System.currentTimeMillis();
            System.out.println("Tempo do QuickSort: " + (tempo2 - tempo1) + " ms");
        }
        catch (StackOverflowError error) {
            System.out.println("Erro de Stack Overflow no QuickSort");
        }

        tempo1 = System.currentTimeMillis();
        ShellSort.sort(ds);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do ShellSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        HeapSort.sort(ds);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do HeapSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        MergeSort.sort(ds, qo.length-1);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do MergeSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        InsertSort.sort(ds);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do InsertSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        SelectionSort.sort(ds);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do SelectionSort: " + (tempo2 - tempo1) + " ms");

        System.out.println("//--------------------------------------------------//");

        System.out.println("Tempo dos algoritmos com conjuntos decrescente:");

        try {
            tempo1 = System.currentTimeMillis();
            QuickSort.sort(dc, 0, qo.length - 1);
            tempo2 = System.currentTimeMillis();
            System.out.println("Tempo do QuickSort: " + (tempo2 - tempo1) + " ms");
        }
        catch (StackOverflowError error) {
            System.out.println("Erro de Stack Overflow no QuickSort");
        }

        tempo1 = System.currentTimeMillis();
        ShellSort.sort(dc);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do ShellSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        HeapSort.sort(dc);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do HeapSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        MergeSort.sort(dc, qo.length-1);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do MergeSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        InsertSort.sort(dc);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do InsertSort: " + (tempo2 - tempo1) + " ms");

        tempo1 = System.currentTimeMillis();
        SelectionSort.sort(dc);
        tempo2 = System.currentTimeMillis();
        System.out.println("Tempo do SelectionSort: " + (tempo2 - tempo1) + " ms");

        System.out.println("//--------------------------------------------------//");
    }
}
