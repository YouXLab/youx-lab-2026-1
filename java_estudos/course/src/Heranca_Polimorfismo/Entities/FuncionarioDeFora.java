package Heranca_Polimorfismo.Entities;

import java.util.ArrayList;
import java.util.List;

public class FuncionarioDeFora extends Funcionario {

    private Double despesas;

    public FuncionarioDeFora(String nome, Integer horas, Double valorPorHora, Double despesas) {
        super(nome, horas, valorPorHora);
        this.despesas = despesas;
    }

    @Override // Serve pra avisar se o metodo herdado e o correto.
    public Double pagamento() {
        return (getHoras() * getValorPorHora() + (despesas * 1.1) );

    }


}
