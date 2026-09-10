package Heranca_Polimorfismo.Entities;

public class PessoaJuridica extends TaxaPagamento{

    private Integer numFuncionarios;

    public PessoaJuridica(String nome, Double rendaAnual, Integer numFuncionarios) {
        super(nome, rendaAnual);
        this.numFuncionarios = numFuncionarios;
    }

    public Integer getNumFuncionarios() {
        return numFuncionarios;
    }

    @Override
    public  Double valorFinal() {
        Double imposto = 0.0;

        if (getNumFuncionarios() < 10) {
            imposto = getRendaAnual() * 0.16;
        }

        if (getNumFuncionarios() > 10) {
            imposto = getRendaAnual() * 0.14;

        }

        return imposto;


    }
}
