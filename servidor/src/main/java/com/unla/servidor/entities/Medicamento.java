package com.unla.servidor.entities;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

@Entity
@Table(name ="medicamento")
public class Medicamento {

    @Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "idMedicamento")
    private long idMedicamento;

    @Column(name = "codigo")
    private String codigo;

    @Column(name = "nombrecomercial")
    private String nombreComercial;

    @Column(name = "droga")
    private String droga;

    @ManyToOne(cascade = {CascadeType.PERSIST , CascadeType.MERGE , CascadeType.DETACH , CascadeType.REFRESH})
	@JoinColumn(name = "idTipo")
	private Tipo tipo;

    public Medicamento () {}

    public Medicamento(String codigo, String nombreComercial, String droga, Tipo tipo) {
        this.codigo = codigo;
        this.nombreComercial = nombreComercial;
        this.droga = droga;
        this.tipo = tipo;
    }

    public long getIdMedicamento() {
        return idMedicamento;
    }

    public void setIdMedicamento(long idMedicamento) {
        this.idMedicamento = idMedicamento;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getNombreComercial() {
        return nombreComercial;
    }

    public void setNombreComercial(String nombreComercial) {
        this.nombreComercial = nombreComercial;
    }

    public String getDroga() {
        return droga;
    }

    public void setDroga(String droga) {
        this.droga = droga;
    }

    public Tipo getTipo() {
        return tipo;
    }

    public void setTipo(Tipo tipo) {
        this.tipo = tipo;
    }

    @Override
    public String toString() {
        return "Medicamento [codigo=" + codigo + ", droga=" + droga + ", idMedicamento=" + idMedicamento
                + ", nombreComercial=" + nombreComercial + ", tipo=" + tipo.getNombre() + "]";
    }

    
    
}
