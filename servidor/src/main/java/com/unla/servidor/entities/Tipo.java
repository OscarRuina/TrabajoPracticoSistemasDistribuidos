package com.unla.servidor.entities;
import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name = "tipo")
public class Tipo {

    @Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "idTipo")
    private long idTipo;

    @Column(name = "nombre")
    private String nombre;

    @Column(name = "activo")
    private boolean activo;

    @OneToMany(fetch = FetchType.LAZY , mappedBy = "tipo" , cascade = {CascadeType.PERSIST , CascadeType.MERGE , CascadeType.DETACH , CascadeType.REFRESH})
	private Set<Medicamento> medicamentos;

    public Tipo () {}

    public Tipo(String nombre) {
        this.nombre = nombre;
        this.activo = true;
    }

    public long getIdTipo() {
        return idTipo;
    }

    public void setIdTipo(long idTipo) {
        this.idTipo = idTipo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public boolean isActivo() {
        return activo;
    }

    public void setActivo(boolean activo) {
        this.activo = activo;
    }

    @Override
    public String toString() {
        return "Tipo [activo=" + activo + ", idTipo=" + idTipo + ", nombre=" + nombre + "]";
    }
    
}
