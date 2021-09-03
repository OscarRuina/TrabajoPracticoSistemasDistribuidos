package com.unla.servidor.repository;
import java.io.Serializable;
import java.util.List;

import com.unla.servidor.entities.Medicamento;
import com.unla.servidor.entities.Tipo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface IMedicamentoRepository extends JpaRepository<Medicamento,Serializable>{

    public List<Medicamento> findByTipo(Tipo tipo);
    
}
