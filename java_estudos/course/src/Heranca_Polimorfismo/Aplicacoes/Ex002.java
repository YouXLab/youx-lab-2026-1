package Heranca_Polimorfismo.Aplicacoes;

import Heranca_Polimorfismo.Entities.Produto;
import Heranca_Polimorfismo.Entities.ProdutoImportado;
import Heranca_Polimorfismo.Entities.ProdutoUsado;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Ex002 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        List<Produto>  produto = new ArrayList<>();

        System.out.println("Entre com os numero de produtos: ");
        Integer n = sc.nextInt();

        for (int i = 0; i<n ; i++) {
            System.out.println("Dados do #" + (i+1) + " produto:" );
            System.out.println("Tipo do produto (c/i/u): ");
            sc.nextLine();
            String resposta = sc.nextLine();

            System.out.println("Nome: ");
            String nome = sc.nextLine();
            System.out.println("Preco: ");
            Double preco = sc.nextDouble();


            if (resposta.equals("c")) {
                produto.add(new Produto(nome,preco));
            }

            else if (resposta.equals("i")) {
                System.out.println("Taxa de Alfandegaria: ");
                Double taxasDeAlfandegaria = sc.nextDouble();
                produto.add(new ProdutoImportado(nome,preco,taxasDeAlfandegaria));
            }

            else if (resposta.equals("u")) {
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
                System.out.println("Data de Fabricacao (DD/MM/YYYY): ");
                LocalDate  dataDeFabricacao = LocalDate.parse(sc.next(),formatter);
                produto.add(new ProdutoUsado(nome,preco,dataDeFabricacao));

            }

        }

        System.out.println("Etiquetas de Preco: ");

        for (Produto prod : produto) {
            System.out.println(prod.etiquetaPreco());
        }

    }


}
