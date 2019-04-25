-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-04-2019 a las 06:37:57
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `servicioautomotriz`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `automoviles`
--

CREATE TABLE `automoviles` (
  `placa` varchar(25) COLLATE utf8_bin NOT NULL,
  `modelo` varchar(10) COLLATE utf8_bin NOT NULL,
  `marca` varchar(25) COLLATE utf8_bin NOT NULL,
  `linea` varchar(25) COLLATE utf8_bin NOT NULL,
  `color` varchar(25) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `automoviles`
--

INSERT INTO `automoviles` (`placa`, `modelo`, `marca`, `linea`, `color`) VALUES
('YGZ-65-97', '2016', 'Chevrolet', 'Matiz', 'Azul'),
('YGE-78-98', '2015', 'Nissan', 'Pulsar', 'Blanco'),
('YPA-87-99', '2017', 'Kia', 'Ceed', 'Azul'),
('YHP-98-65', '2012', 'Renault', 'Sandero', 'Rojo'),
('PYE-55-99', '2014', 'Toyota', 'Avanza', 'Blanco'),
('PNL-45-78', '2005', 'Chevrolet', 'Chevy', 'Naranja'),
('TYG-23-55', '2015', 'Ford', 'Fiesta', 'Rojo'),
('YGT-88-77', '2002', 'Honda', 'Civic', 'Gris');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
