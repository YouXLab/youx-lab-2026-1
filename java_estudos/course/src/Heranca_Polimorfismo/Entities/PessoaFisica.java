package Heranca_Polimorfismo.Entities;

import java.util.ArrayList;
import java.util.List;

public class PessoaFisica extends TaxaPagamento {

    private Double gastosSaude;

    public PessoaFisica(String nome, Double rendaAnual,Double gastosSaude) {
        super(nome, rendaAnual);
        this.gastosSaude = gastosSaude;
    }

    public Double getGastosSaude() {
        return gastosSaude;
    }


    @Override
    public  Double valorFinal() {
        Double imposto = 0.0;
        if (getRendaAnual() < 20000.00) {
            imposto  = getRendaAnual() * 0.15;
        }
        else if (getRendaAnual() >= 20000.00) {
            imposto = getRendaAnual() * 0.25;
        }
        if (getGastosSaude() > 0) {
            imposto = imposto - (getGastosSaude() * 0.50);
        }

        return imposto;

    }




}
