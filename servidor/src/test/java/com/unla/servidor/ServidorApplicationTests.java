package com.unla.servidor;

import java.util.List;

import com.unla.servidor.entities.Medicamento;
//import com.unla.servidor.entities.Tipo;
import com.unla.servidor.services.MedicamentoServiceImpl;
import com.unla.servidor.services.TipoServiceImpl;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ServidorApplicationTests {

	@Autowired
	private TipoServiceImpl tipo;

	@Autowired
	private MedicamentoServiceImpl medi;

	//Tipo t = new Tipo("crema");
	//Tipo t1 = tipo.traerTipoPorNombre("aerosol");
	Medicamento m = new Medicamento("12345","amoxol","amoxilina",tipo.traerTipoPorNombre("aerosol"));

	@Test
	void contextLoads() {
	}
	//Test de tipo
	/*@Test
	public void insertarTipo(){
		tipo.save(t);
	}

	@Test
	public void bajaLogica(){
		tipo.baja(tipo.traerTipoPorNombre("aerosol"));
	}*/

	//Test de medicamento
	@Test
	public void insertarMedicamento(){
		medi.save(m);
	}

	@Test
	public List<Medicamento> traerPorTipo(){
		return medi.listarPorTipo(tipo.traerTipoPorNombre("aerosol"));
	}
}
