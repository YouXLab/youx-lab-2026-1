package Heranca_Polimorfismo.Entities;

public class Funcionario {
    private String nome;
    private Integer horas;
    private Double valorPorHora;

    public Funcionario(String nome, Integer horas, Double valorPorHora) {
        this.nome = nome;
        this.horas = horas;
        this.valorPorHora = valorPorHora;
    }

    public Double pagamento() {
       Double valorFinal = valorPorHora * horas;
       return valorFinal;
    }

    public String getNome() {
        return nome;
    }

    public Integer getHoras() {
        return horas;
    }

    public Double getValorPorHora() {
        return valorPorHora;
    }


}
