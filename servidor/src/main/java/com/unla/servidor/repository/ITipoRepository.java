package com.unla.servidor.repository;

import com.unla.servidor.entities.Tipo;
import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ITipoRepository extends JpaRepository<Tipo,Serializable>{

    public Tipo findByNombre(String nombre);
    
}
