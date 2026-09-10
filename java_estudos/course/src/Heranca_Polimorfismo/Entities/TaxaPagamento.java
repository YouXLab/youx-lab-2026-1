package Heranca_Polimorfismo.Entities;

public abstract class TaxaPagamento {
    private String nome;
    private Double rendaAnual;

    public String getNome() {
        return nome;
    }

    public Double getRendaAnual() {
        return rendaAnual;
    }

    public TaxaPagamento(String nome, Double rendaAnual) {
        this.nome = nome;
        this.rendaAnual = rendaAnual;
    }

    public abstract Double valorFinal() ;

}
