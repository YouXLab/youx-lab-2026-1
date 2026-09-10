package Heranca_Polimorfismo.Aplicacoes;

import Heranca_Polimorfismo.Entities.Funcionario;
import Heranca_Polimorfismo.Entities.FuncionarioDeFora;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Ex001 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        List<Funcionario> lista = new ArrayList<>();

        System.out.println("Entre com o numero de funcionarios: ");
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i<n ; i++) {
            System.out.println("Dados do " + (i+1) + " cliente: ");
            System.out.println("Funcionario de fora? (s/n) ");
            sc.nextLine();
            String resposta = sc.nextLine();
            System.out.println("Nome: ");
            String nome = sc.nextLine();
            System.out.println("Horas: ");
            Integer horas = sc.nextInt();
            System.out.println("Valor por hora: ");
            Double valorPorHora = sc.nextDouble();

            if (resposta.equals("n")) {
                lista.add(new Funcionario(nome,horas,valorPorHora));
            }


            else if (resposta.equals("s")) {
                System.out.println("Despesa adicional: ");
                Double despesas = sc.nextDouble();
                lista.add(new FuncionarioDeFora(nome,horas,valorPorHora,despesas));
            }

        }

        System.out.println("PAGAMENTOS: ");

        for (Funcionario func : lista) {
            System.out.println(func.getNome() + " - $ " + func.pagamento());
        }


    }
}
