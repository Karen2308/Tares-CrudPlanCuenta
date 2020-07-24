-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.6-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para crud
CREATE DATABASE IF NOT EXISTS `crud` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `crud`;

-- Volcando estructura para tabla crud.grupo
CREATE TABLE IF NOT EXISTS `grupo` (
  `id_grupo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_grupo`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla crud.plancuenta
CREATE TABLE IF NOT EXISTS `plancuenta` (
  `id_pcuenta` int(11) NOT NULL AUTO_INCREMENT,
  `Codigo` varchar(50) DEFAULT NULL,
  `Grupo` int(11) DEFAULT NULL,
  `Descripcion` varchar(50) DEFAULT NULL,
  `Naturaleza` varchar(1) DEFAULT NULL,
  `Estado` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id_pcuenta`),
  KEY `FK__grupo` (`Grupo`),
  CONSTRAINT `FK__grupo` FOREIGN KEY (`Grupo`) REFERENCES `grupo` (`id_grupo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
