
drop database if exists city_sql;
create database city_sql;
use city_sql;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";



CREATE TABLE `city` (
  `id` int(11) NOT NULL,
  `cityname` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `city` (`id`, `cityName`) VALUES
(1, 'Pune'),
(2, 'Hillwood'),
(3, 'San Jose'),
(4, 'simla'),
(5, 'Patna');

-- --------------------------------------------------------

--
-- Table structure for table `emp`
--

CREATE TABLE `emp` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `cityId` int(11) NOT NULL,
  `score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `emp`
--

INSERT INTO `emp` (`id`, `name`, `cityId`, `score`) VALUES
(1, 'sai', 1, 5),
(2, 'matthew', 2, 4),
(3, 'jeremy', 3, 6),
(4, 'Rajesh', 4, 4),
(5, 'Daniel', 5, 6),
(6, 'Alien', 1, 2),
(7, 'phoenix', 2, 9),
(8, 'aryan', 3, 4),
(9, 'Anastasio', 4, 3),
(10, 'Marie', 5, 6);



ALTER TABLE `city`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`);
  
ALTER TABLE `emp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cityId` (`cityId`);


ALTER TABLE `emp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

ALTER TABLE `emp`
  ADD CONSTRAINT `emp_ibfk_1` FOREIGN KEY (`cityId`) REFERENCES `city` (`id`);

