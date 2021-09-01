package com.unla.servidor.services;

import java.util.List;



import com.unla.servidor.entities.Tipo;
import com.unla.servidor.repository.ITipoRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class TipoServiceImpl implements ITipoService{

    @Autowired
    private ITipoRepository tipo;

    @Transactional(readOnly = true)
    public List<Tipo> getAll(){
        return tipo.findAll();
    }

    @Transactional(readOnly = true)
    public Tipo traerTipoPorNombre(String nombre){
        return tipo.findByNombre(nombre);
    }

    @Transactional
    public Tipo save(Tipo t){
        return tipo.save(t);
    }

    @Transactional
    public Tipo baja(Tipo t){
        t.setActivo(false);
        return tipo.save(t);
    }
    
}
