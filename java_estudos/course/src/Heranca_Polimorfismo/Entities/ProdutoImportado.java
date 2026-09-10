package Heranca_Polimorfismo.Entities;

public class ProdutoImportado extends Produto {

     private Double taxasDeAlfandegaria;

    public ProdutoImportado(String nome, Double preco,Double taxasDeAlfaganderia) {
        super(nome, preco);
        this.taxasDeAlfandegaria = taxasDeAlfaganderia;
    }

    public Double getTaxasDeAlfandegaria() {
        return taxasDeAlfandegaria;
    }

    public Double precoTotal() {
        return getPreco() + getTaxasDeAlfandegaria();
    }

    @Override
    public String etiquetaPreco() {
        return getNome() + " $ " + precoTotal() + "(Taxas de Alfandegaria: $ " + getTaxasDeAlfandegaria() +")";

     }

}
