-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: acklandobjects.mysql.pythonanywhere-services.com    Database: acklandobjects$objects
-- ------------------------------------------------------
-- Server version	5.6.40-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `input_12_1`
--

DROP TABLE IF EXISTS `input_12_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_12_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_12_1`
--

LOCK TABLES `input_12_1` WRITE;
/*!40000 ALTER TABLE `input_12_1` DISABLE KEYS */;
INSERT INTO `input_12_1` VALUES (1,'Tes'),(2,'Scratches'),(3,'Color'),(4,'Crouching figure'),(5,'Messy'),(6,'COlor'),(7,'Scratches'),(8,'Brushy'),(9,'People'),(10,'Space'),(11,'Color'),(12,'Color'),(13,'Messy'),(14,'It’s messy '),(15,'Figures are crouching '),(16,'Sun'),(17,'Shadows and shapes');
/*!40000 ALTER TABLE `input_12_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_12_2`
--

DROP TABLE IF EXISTS `input_12_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_12_2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_12_2`
--

LOCK TABLES `input_12_2` WRITE;
/*!40000 ALTER TABLE `input_12_2` DISABLE KEYS */;
INSERT INTO `input_12_2` VALUES (1,'Very rough'),(2,'Smooth'),(3,'Rough '),(4,'Rough'),(5,'Rough'),(6,'It\'s really rough.'),(7,'Rough '),(8,'Bumpy'),(9,'Rough ');
/*!40000 ALTER TABLE `input_12_2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_12_3`
--

DROP TABLE IF EXISTS `input_12_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_12_3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_12_3`
--

LOCK TABLES `input_12_3` WRITE;
/*!40000 ALTER TABLE `input_12_3` DISABLE KEYS */;
/*!40000 ALTER TABLE `input_12_3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_13_1`
--

DROP TABLE IF EXISTS `input_13_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_13_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_13_1`
--

LOCK TABLES `input_13_1` WRITE;
/*!40000 ALTER TABLE `input_13_1` DISABLE KEYS */;
INSERT INTO `input_13_1` VALUES (1,'headdress test'),(2,'Headdress '),(3,'Headdress '),(4,'Headdress '),(5,'Jewelry'),(6,'Robes'),(7,'Necklace '),(8,'Jewelery'),(9,'Jewelry '),(10,'Jewelry');
/*!40000 ALTER TABLE `input_13_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_13_2`
--

DROP TABLE IF EXISTS `input_13_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_13_2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_13_2`
--

LOCK TABLES `input_13_2` WRITE;
/*!40000 ALTER TABLE `input_13_2` DISABLE KEYS */;
INSERT INTO `input_13_2` VALUES (1,'Stone '),(2,'Stone'),(3,'Stone '),(4,'Stone '),(5,'Stone'),(6,'Stone ');
/*!40000 ALTER TABLE `input_13_2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_13_3`
--

DROP TABLE IF EXISTS `input_13_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_13_3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_13_3`
--

LOCK TABLES `input_13_3` WRITE;
/*!40000 ALTER TABLE `input_13_3` DISABLE KEYS */;
INSERT INTO `input_13_3` VALUES (1,'Rich af'),(2,'Rich'),(3,'Wealthy '),(4,'Pretty'),(5,'Regal'),(6,'Beautiful ');
/*!40000 ALTER TABLE `input_13_3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_14_1`
--

DROP TABLE IF EXISTS `input_14_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_14_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_14_1`
--

LOCK TABLES `input_14_1` WRITE;
/*!40000 ALTER TABLE `input_14_1` DISABLE KEYS */;
INSERT INTO `input_14_1` VALUES (1,'Chaotic'),(2,'Wild'),(3,'Chaotic'),(4,'Chaos'),(5,'Chaos'),(6,'Chaos'),(7,'Chaotic'),(8,'Chaos'),(9,'Chaotic'),(10,'Swirly');
/*!40000 ALTER TABLE `input_14_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_14_2`
--

DROP TABLE IF EXISTS `input_14_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_14_2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_14_2`
--

LOCK TABLES `input_14_2` WRITE;
/*!40000 ALTER TABLE `input_14_2` DISABLE KEYS */;
INSERT INTO `input_14_2` VALUES (1,'Rough '),(2,'Thick'),(3,'Coarse'),(4,'Thick');
/*!40000 ALTER TABLE `input_14_2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_14_3`
--

DROP TABLE IF EXISTS `input_14_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_14_3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_14_3`
--

LOCK TABLES `input_14_3` WRITE;
/*!40000 ALTER TABLE `input_14_3` DISABLE KEYS */;
INSERT INTO `input_14_3` VALUES (1,'It’s bad'),(2,'Bad'),(3,'It’s bad'),(4,'Not good '),(5,'I don’t know');
/*!40000 ALTER TABLE `input_14_3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_15_1`
--

DROP TABLE IF EXISTS `input_15_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_15_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_15_1`
--

LOCK TABLES `input_15_1` WRITE;
/*!40000 ALTER TABLE `input_15_1` DISABLE KEYS */;
INSERT INTO `input_15_1` VALUES (1,'You appear to be praying '),(2,'You are praying '),(3,'Rough'),(4,'Chaotic'),(5,'Prayer'),(6,'A vision'),(7,'Prayer'),(8,'Divine intervention '),(9,'On your knees ');
/*!40000 ALTER TABLE `input_15_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_15_2`
--

DROP TABLE IF EXISTS `input_15_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_15_2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_15_2`
--

LOCK TABLES `input_15_2` WRITE;
/*!40000 ALTER TABLE `input_15_2` DISABLE KEYS */;
INSERT INTO `input_15_2` VALUES (1,'Rapt'),(2,'Sad'),(3,'Awe'),(4,'In awe'),(5,'Bow'),(6,'Scared ');
/*!40000 ALTER TABLE `input_15_2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_15_3`
--

DROP TABLE IF EXISTS `input_15_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_15_3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_15_3`
--

LOCK TABLES `input_15_3` WRITE;
/*!40000 ALTER TABLE `input_15_3` DISABLE KEYS */;
INSERT INTO `input_15_3` VALUES (1,'Ocean'),(2,'Museum '),(3,'In a church'),(4,'Church '),(5,'Church ');
/*!40000 ALTER TABLE `input_15_3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_16_1`
--

DROP TABLE IF EXISTS `input_16_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_16_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_16_1`
--

LOCK TABLES `input_16_1` WRITE;
/*!40000 ALTER TABLE `input_16_1` DISABLE KEYS */;
INSERT INTO `input_16_1` VALUES (1,'Tools'),(2,'Mother '),(3,'Big stick'),(4,'Sharp '),(5,'Wood'),(6,'Weapons '),(7,'Gnomes');
/*!40000 ALTER TABLE `input_16_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_16_2`
--

DROP TABLE IF EXISTS `input_16_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_16_2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_16_2`
--

LOCK TABLES `input_16_2` WRITE;
/*!40000 ALTER TABLE `input_16_2` DISABLE KEYS */;
INSERT INTO `input_16_2` VALUES (1,'On his head '),(2,'They way the figures are organized '),(3,'Symmetry'),(4,'Symmetry'),(5,'Two'),(6,'Two');
/*!40000 ALTER TABLE `input_16_2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_16_3`
--

DROP TABLE IF EXISTS `input_16_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_16_3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_16_3`
--

LOCK TABLES `input_16_3` WRITE;
/*!40000 ALTER TABLE `input_16_3` DISABLE KEYS */;
INSERT INTO `input_16_3` VALUES (1,'Magic'),(2,'A column'),(3,'Wood'),(4,'A column'),(5,'Architecture ');
/*!40000 ALTER TABLE `input_16_3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_17_1`
--

DROP TABLE IF EXISTS `input_17_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_17_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_17_1`
--

LOCK TABLES `input_17_1` WRITE;
/*!40000 ALTER TABLE `input_17_1` DISABLE KEYS */;
INSERT INTO `input_17_1` VALUES (1,'Impressionistic '),(2,'Harvest'),(3,'Grazing'),(4,'They are kneeling.');
/*!40000 ALTER TABLE `input_17_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `input_17_2`
--

DROP TABLE IF EXISTS `input_17_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `input_17_2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(4096) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `input_17_2`
--

LOCK TABLES `input_17_2` WRITE;
/*!40000 ALTER TABLE `input_17_2` DISABLE KEYS */;
INSERT INTO `input_17_2` VALUES (1,'Impressionistic '),(2,'Blurry'),(3,'Sketch ');
/*!40000 ALTER TABLE `input_17_2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-06 16:03:33
