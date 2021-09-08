drop database if exists `Distribuidos`;
create database if not exists `Distribuidos`;
use `Distribuidos`;

drop table if exists `medicamentos`;
drop table if exists `tipo`;

select a.Id_medicamento, a.Numero, a.Comercial, a.Descripcion, a.Id_tipo, b.Nombre from medicamentos a
inner join tipo b ON a.id_tipo = b.Id_tipo where a.comercial like 'P%';

select * from medicamentos a order by Id_medicamento desc limit 1;
select Id_tipo from tipo a order by Id_tipo desc limit 1;

CREATE TABLE IF NOT EXISTS `tipo` (
  `Id_tipo` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `Activo` INT(1) NULL DEFAULT NULL,
  `Nombre` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`Id_tipo`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;

insert into tipo values (1, 1, 'algo');

CREATE TABLE IF NOT EXISTS `medicamentos` (
  `Id_medicamento` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `Numero` VARCHAR(255) NULL DEFAULT NULL,
  `Comercial` VARCHAR(255) NULL DEFAULT NULL,
  `Descripcion` VARCHAR(255) NULL DEFAULT NULL,
  `Id_tipo` BIGINT(20) NULL DEFAULT NULL,
  PRIMARY KEY (`Id_medicamento`),
  INDEX `FK1868un1r7ff8n2b9kkomyp4be` (`id_tipo` ASC),
  CONSTRAINT `FK1868un1r7ff8n2b9kkomyp4be`
    FOREIGN KEY (`Id_tipo`)
    REFERENCES `tipo` (`Id_tipo`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;

select * from medicamentos;
select * from tipo;

insert into medicamentos 
values (1,'abc-121','algo', 'registro', 1);

CREATE TABLE IF NOT EXISTS `producto` (
  `Id_producto` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `Codigo` varchar(255) NULL DEFAULT NULL,
  PRIMARY KEY (`Id_producto`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;

insert into producto values (4,'ABC-1111-9');

select * from producto;

drop table producto;
drop table medicamentos;
drop table tipo;

insert into producto(Codigo) values
 ('DCR-88578-9'),('PAS-11111-5'),('OCR-55565-7'),('PAQ-88697-4'),('WNA-25713-8');
