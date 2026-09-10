package Heranca_Polimorfismo.Aplicacoes;

import Heranca_Polimorfismo.Entities.PessoaFisica;
import Heranca_Polimorfismo.Entities.PessoaJuridica;
import Heranca_Polimorfismo.Entities.TaxaPagamento;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Ex003 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Entre com o numero de Contribuintes: ");
        Integer n = sc.nextInt();
        sc.nextLine();

        List<TaxaPagamento> taxaPagamentos = new ArrayList<>();


        for (int i = 1 ; i<=n ; i++) {
            System.out.println("Dados do # " + i + " contribuinte: ");
            System.out.println("Pessoa Fisica ou Juridica (f/j): ");
            String resposta = sc.nextLine();

            System.out.println("Nome: ");
            String nome = sc.nextLine();
            System.out.println("renda anual: ");
            Double rendaAnual = sc.nextDouble();

            if (resposta.equals("f")) {
                System.out.println("Gastos com saude: ");
                sc.nextLine();
                Double gastosSaude = sc.nextDouble();
                sc.nextLine();

                taxaPagamentos.add(new PessoaFisica(nome,rendaAnual,gastosSaude));
            }

            if (resposta.equals("j")) {
                System.out.println("Numeros de Funcionarios: ");
                sc.nextLine();
                Integer numFuncionarios = sc.nextInt();
                sc.nextLine();

                taxaPagamentos.add(new PessoaJuridica(nome,rendaAnual,numFuncionarios));
            }
        }

        double totalImpostos = 0.0;

        System.out.println("    ");
        System.out.println("Impostos Pagos: ");
        for (TaxaPagamento taxa: taxaPagamentos) {
            System.out.println("Nome: " + taxa.getNome() + " $ " + taxa.valorFinal());
            totalImpostos += taxa.valorFinal();
            }


        System.out.println("    ");
        System.out.println("Total de Impostos: ");
        System.out.println(totalImpostos);






    }
}
