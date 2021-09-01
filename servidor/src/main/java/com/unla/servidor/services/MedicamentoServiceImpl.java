package com.unla.servidor.services;

import java.util.List;

import com.unla.servidor.entities.Medicamento;
import com.unla.servidor.entities.Tipo;
import com.unla.servidor.repository.IMedicamentoRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class MedicamentoServiceImpl implements IMedicamentoService{
    
    @Autowired
    private IMedicamentoRepository medicamento;

    @Transactional(readOnly = true)
    public List<Medicamento> getAll(){
        return medicamento.findAll();
    }

    @Transactional
    public List<Medicamento> listarPorTipo(Tipo tipo){
        return medicamento.findByTipo(tipo);
    }

    @Transactional
    public Medicamento save(Medicamento m){
        return medicamento.save(m);
    }

    //falta implementar buscar por comienzo de letra de nombre comercial

}
