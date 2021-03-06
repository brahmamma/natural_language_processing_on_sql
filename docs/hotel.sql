-- phpMyAdmin SQL Dump
-- version 3.3.2
-- http://www.phpmyadmin.net
--
-- Serveur: localhost
-- Généré le : Ven 29 Mars 2013 à 13:31
-- Version du serveur: 5.1.41
-- Version de PHP: 5.3.1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


drop database if exists hotel_sql;
create database hotel_sql;
use hotel_sql;



/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `hotel`
--

-- --------------------------------------------------------

--
-- Structure de la table `chambre`
--

CREATE TABLE IF NOT EXISTS `chambre` (
  `idchambre` int(11) NOT NULL AUTO_INCREMENT,
  `room` int(11) NOT NULL,
  PRIMARY KEY (`idChambre`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=6 ;

--
-- Contenu de la table `chambre`
--

INSERT INTO `chambre` (`idChambre`, `nbLit`) VALUES
(1, 201),
(2, 200),
(3, 402),
(4, 397),
(5, 212);

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE IF NOT EXISTS `client` (
  `idclient` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `surnom` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `age` int(11) NOT NULL,
  `adress` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`idClient`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=5 ;

--
-- Contenu de la table `client`
--

INSERT INTO `client` (`idClient`, `nom`, `prenom`, `age`, `adresse`, `telephone`) VALUES
(1, 'TERIEUR', 'Alain', 45, '23 rue de Amar DI', '0456677890'),
(2, 'TERIEUR', 'Alex', 23, '20 allee de Bowie Kend', '0456645891'),
(3, 'PAROLEDOR', 'Carla', 24, 'Salle Eugene, rue Fidele Annamour', '0978357689'),
(4, 'TOULETAN', 'Eugene', 66, '12 avenue du Bob Eau', '0672908767');

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

CREATE TABLE IF NOT EXISTS `reservation` (
  `idreservation` int(11) NOT NULL AUTO_INCREMENT,
  `idclient` int(11) NOT NULL,
  `idchambre` int(11) NOT NULL,
  `DateA` date NOT NULL,
  `DateD` date NOT NULL,
  PRIMARY KEY (`idReservation`, `idClient`, `idChambre`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=3 ;

--
-- Contenu de la table `reservation`
--

INSERT INTO `reservation` (`idReservation`, `idClient`, `idChambre`, `DateA`, `DateD`) VALUES
(1, 1, 1, '2013-03-14', '2013-03-28'),
(2, 3, 4, '2013-03-25', '2013-03-31');
