-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 28, 2021 at 05:05 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `minroob`
--

-- --------------------------------------------------------

--
-- Table structure for table `game_requests`
--

CREATE TABLE `game_requests` (
  `id` int(11) NOT NULL,
  `sender_player_id` int(11) NOT NULL,
  `receiver_player_id` int(11) NOT NULL,
  `timestamp` bigint(20) NOT NULL,
  `is_accepted` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `game_requests`
--

INSERT INTO `game_requests` (`id`, `sender_player_id`, `receiver_player_id`, `timestamp`, `is_accepted`) VALUES
(79, 30, 1, 1616943861, 1);

-- --------------------------------------------------------

--
-- Table structure for table `global_chat`
--

CREATE TABLE `global_chat` (
  `id` int(11) NOT NULL,
  `player_id` int(11) NOT NULL,
  `message` text NOT NULL,
  `timestamp` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `global_chat`
--

INSERT INTO `global_chat` (`id`, `player_id`, `message`, `timestamp`) VALUES
(211, 30, 's', 1616251100),
(212, 30, 's', 1616251120),
(213, 30, 's', 1616251995),
(214, 30, 's', 1616252032),
(215, 30, 'salam', 1616252035),
(216, 30, 'vaght shoma be kheir', 1616252044),
(217, 30, 'salam', 1616252093),
(218, 30, 'سلام وقت شما بخیر باشه. این پلتفرم بنظر خوب میاد برای چت', 1616252146),
(219, 30, 'از متون فارسی هم پشتیبانی میکنه و با خیال راحت میتونید فارسی چت کنید', 1616252162),
(220, 30, 'Dige Dige', 1616252208),
(221, 30, 'خیلی هم عالی', 1616252216),
(222, 30, 'Hiiii', 1616265966),
(223, 30, 'Hiiii', 1616266105),
(224, 30, 'salam', 1616266519),
(225, 30, 'khoni?', 1616266521),
(226, 30, 'Salaaam', 1616266627),
(227, 30, 'hal shoma chetore?', 1616266631),
(228, 30, 'Salam :D', 1616267018),
(229, 30, 'hal shoma chetore?', 1616267022),
(230, 30, '.', 1616267062),
(231, 30, 'Salam', 1616271849),
(232, 30, 'salam', 1616271888),
(233, 30, 'khobi?', 1616271893),
(234, 30, 'با نام و یاد خدا', 1616271989),
(235, 30, 'این پروژه صرفا برای تست میباشد', 1616271995),
(236, 30, 'سلام وقت شما بخیر باشه', 1616272093),
(237, 30, 'دیگه چخبر؟', 1616272096),
(238, 30, 'Test Message', 1616273164),
(239, 30, 'Salam', 1616273836),
(240, 30, 'Kasi hast?', 1616273838),
(241, 30, 'Salam', 1616274114),
(242, 30, 'salam', 1616274149),
(243, 30, 'Salam', 1616274709),
(244, 30, 'Salam', 1616274732),
(245, 30, 'Salam', 1616274764),
(246, 30, 'salam', 1616284749),
(247, 30, 'Salam', 1616287719),
(248, 30, 'سلام استاد وقت شما بخیر', 1616287723),
(249, 30, 'امیدوارم که حالتون خوب باشه', 1616287730),
(250, 30, 'این هم محصولی که بنده تولید کردم', 1616287737),
(251, 30, 'سلام سلام', 1616287995),
(252, 30, 'حال شما چطوره؟', 1616287997),
(253, 30, 'Salam ostad vaght shoma be kheir]', 1616288201),
(254, 30, 'Tet', 1616288245),
(255, 30, 'Test', 1616288246),
(256, 30, 'Alo 1 2 3', 1616288248),
(257, 30, 'Salam ostad', 1616323981),
(258, 30, 'vaght shoma bekheir', 1616323985),
(259, 30, 'Salam ostad', 1616324194),
(260, 30, 'سلام وقت شما بخیر', 1616324197),
(261, 30, 'salam', 1616338538),
(262, 30, 'vaght shoma be kheir', 1616338542),
(263, 30, 'امیدوارم حالتون خوب باشه', 1616338551),
(264, 30, 'امروز چطور بود؟', 1616338554),
(265, 30, 'روز خوبی داشتین؟', 1616338557),
(266, 30, 'ی.', 1616338558),
(267, 30, '.', 1616338559),
(268, 30, '.', 1616338560),
(269, 30, '.', 1616338560),
(270, 30, '.', 1616338560),
(271, 30, '.', 1616338560),
(272, 30, 'Salam', 1616340214),
(273, 30, 'Salam', 1616340598),
(274, 30, 'Salam', 1616340600),
(275, 30, 'Hi', 1616350614),
(276, 30, 'How Are you?', 1616350617),
(277, 30, 'salam', 1616353990),
(278, 30, 'حال شما چطوره؟', 1616353995),
(279, 30, '.', 1616534690),
(280, 30, 'SAlam', 1616621186),
(281, 30, 'Hal shoma chetore?', 1616621192),
(282, 32, 'salam', 1616857126),
(283, 32, 'khobid?', 1616857129),
(284, 30, '.', 1616859441),
(285, 30, '.', 1616859443),
(286, 30, 'lll', 1616859451),
(287, 30, '.', 1616860192),
(288, 30, 'salam', 1616860195),
(289, 30, 'khobi?', 1616860198),
(290, 30, '.', 1616861051),
(291, 30, '.', 1616861052),
(292, 30, '.', 1616861052),
(293, 30, '.', 1616861052),
(294, 30, '.', 1616861053),
(295, 30, '.', 1616861053),
(296, 30, '.', 1616861053),
(297, 30, '.', 1616861053),
(298, 30, '.', 1616861054),
(299, 30, '.', 1616861054),
(300, 30, '.', 1616861054),
(301, 30, '.', 1616861054),
(302, 30, '.', 1616861062),
(303, 30, '.', 1616861385),
(304, 30, '.', 1616861387),
(305, 30, '.', 1616861389),
(306, 30, '.', 1616861389),
(307, 30, '.', 1616861390),
(308, 30, '.', 1616861391),
(309, 30, '.', 1616861392),
(310, 30, 'Salam ostad', 1616861395),
(311, 30, 'vaght shoma be kheir bashe', 1616861401),
(312, 30, 'vaght shoma be kheir bashe', 1616861969),
(313, 32, 'sALAM', 1616862145),
(314, 32, 'Salam', 1616862149),
(315, 30, 'salam', 1616862151),
(316, 30, 'khobi?', 1616862153),
(317, 32, 'mrc to khoni?', 1616862158),
(318, 32, '.', 1616863374),
(319, 30, '.', 1616863376),
(320, 30, 'Salam', 1616863379),
(321, 30, 'Khobi?', 1616863381),
(322, 32, 'mrc', 1616863384),
(323, 32, 'to khobi?', 1616863386),
(324, 32, 'dsa', 1616863389),
(325, 30, 'dsadsa', 1616863391),
(326, 30, 'salam', 1616863393),
(327, 30, '.', 1616863399),
(328, 30, 'SAlam', 1616866283),
(329, 30, 'SAlam', 1616867208),
(330, 32, '.', 1616867835),
(331, 32, '.', 1616867837),
(332, 32, '.', 1616867838),
(333, 32, '.', 1616867838),
(334, 30, '.', 1616868318),
(335, 30, '.', 1616868321),
(336, 30, 'Salam', 1616868323),
(337, 30, 'Vaght Shoma be kheir', 1616868329),
(338, 30, 'haleton khobe?', 1616868368),
(339, 30, 'haleton khobe?', 1616868613),
(340, 30, '.', 1616871206),
(341, 30, 'Salam', 1616871207),
(342, 30, 'Hal shoma chetore?', 1616871212),
(343, 30, '.', 1616871214),
(344, 30, '.', 1616871214),
(345, 30, '.', 1616871215),
(346, 30, '.', 1616871215),
(347, 30, '.', 1616871225),
(348, 30, '.', 1616927509),
(349, 30, '.', 1616927554),
(350, 30, '.', 1616927567),
(351, 30, 'Salam', 1616927600),
(352, 30, 'khobi?', 1616927602),
(353, 30, '.', 1616927865),
(354, 30, '.', 1616927915),
(355, 30, '.', 1616927916),
(356, 30, 'salam', 1616927956),
(357, 30, '.', 1616928050),
(358, 1, '.', 1616928599),
(359, 38, 'salam', 1616943225),
(360, 38, 'khoni?', 1616943226),
(361, 38, '.', 1616943760),
(362, 38, 'Salam', 1616943764),
(363, 38, 'khoni?', 1616943769),
(364, 38, 'khobi?', 1616943771),
(365, 38, 'Salam', 1616943785),
(366, 38, 'Ehem', 1616943789);

-- --------------------------------------------------------

--
-- Table structure for table `hibernate_sequence`
--

CREATE TABLE `hibernate_sequence` (
  `next_val` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hibernate_sequence`
--

INSERT INTO `hibernate_sequence` (`next_val`) VALUES
(85);

-- --------------------------------------------------------

--
-- Table structure for table `minroob_game`
--

CREATE TABLE `minroob_game` (
  `id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  `map` text NOT NULL,
  `clicked_positions` text NOT NULL,
  `total_bombs` int(11) NOT NULL,
  `turn_player_id` int(11) NOT NULL,
  `player_one_id` int(11) NOT NULL,
  `player_two_id` int(11) NOT NULL,
  `player_one_score` int(11) NOT NULL DEFAULT 0,
  `player_two_score` int(11) NOT NULL DEFAULT 0,
  `winer_id` int(11) DEFAULT NULL,
  `is_finished` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `minroob_game`
--

INSERT INTO `minroob_game` (`id`, `game_id`, `map`, `clicked_positions`, `total_bombs`, `turn_player_id`, `player_one_id`, `player_two_id`, `player_one_score`, `player_two_score`, `winer_id`, `is_finished`) VALUES
(77, 53, '[[-1, 1, 1, -1, -1, -1, -1, 1], [-1, -1, -1, -1, 1, 1, -1, -1], [-1, -1, 1, 1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, -1, 1], [-1, 1, -1, -1, 1, -1, -1, -1], [1, -1, 1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, -1, 1], [-1, -1, -1, -1, 1, 1, -1, -1]]', '[[true, true, true, true, true, true, true, true], [true, true, true, true, true, true, true, true], [true, true, true, true, true, true, true, true], [true, true, true, true, true, true, true, true], [true, true, true, true, true, true, true, false], [true, true, true, true, true, true, true, true], [true, true, true, true, true, true, true, true], [true, true, true, true, true, true, true, false]]', 17, 30, 1, 30, 5, 17, 30, 1),
(78, 54, '[[-1, 1, 1, -1, -1, -1, 1, -1], [-1, 1, -1, 1, -1, -1, -1, -1], [1, -1, -1, -1, -1, -1, -1, 1], [-1, -1, 1, 1, -1, -1, -1, -1], [-1, -1, 1, -1, -1, -1, -1, 1], [1, -1, -1, -1, -1, -1, -1, 1], [-1, 1, -1, -1, -1, -1, 1, -1], [1, -1, -1, -1, -1, -1, 1, -1]]', '[[true, true, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 30, 1, 30, 0, 3, 30, 1),
(79, 55, '[[-1, 1, -1, -1, 1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, 1, -1], [-1, 1, -1, -1, -1, 1, -1, -1], [-1, -1, -1, -1, 1, -1, -1, 1], [-1, -1, 1, -1, -1, -1, 1, -1], [1, -1, -1, -1, -1, -1, 1, -1], [-1, -1, -1, -1, 1, -1, 1, -1], [1, -1, -1, -1, 1, -1, -1, 1]]', '[[false, true, true, true, true, true, true, true], [false, false, false, false, true, true, true, true], [false, true, false, true, true, true, false, true], [false, true, false, false, true, false, false, true], [false, false, true, true, false, false, true, false], [true, false, true, false, true, false, true, false], [true, false, true, true, true, false, true, false], [false, false, false, false, true, false, true, true]]', 17, 1, 1, 30, 2, 14, 30, 1),
(80, 56, '[[-1, -1, -1, 1, -1, 1, -1, -1], [1, 1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, 1, 1], [1, -1, 1, -1, -1, -1, -1, -1], [1, -1, -1, -1, -1, -1, 1, -1], [-1, 1, -1, 1, -1, -1, 1, -1], [-1, -1, -1, -1, -1, 1, -1, 1], [1, -1, -1, -1, 1, -1, -1, -1]]', '[[false, false, false, false, false, false, false, true], [false, false, false, false, true, false, false, false], [false, false, false, false, false, false, false, true], [false, false, true, false, false, false, true, true], [false, false, false, false, false, true, true, true], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 1, 1, 30, 1, 2, 1, 1),
(82, 58, '[[-1, 1, -1, -1, -1, -1, 1, -1], [1, 1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, 1, -1, -1], [-1, -1, 1, -1, 1, -1, -1, -1], [-1, -1, -1, -1, 1, 1, -1, -1], [-1, 1, -1, 1, -1, -1, 1, -1], [1, -1, -1, -1, -1, -1, -1, 1], [-1, -1, -1, -1, 1, -1, -1, 1]]', '[[false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 1, 1, 30, 0, 0, 1, 1),
(83, 59, '[[1, 1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, -1, 1], [1, -1, -1, -1, -1, -1, 1, -1], [1, -1, -1, -1, -1, -1, -1, 1], [-1, 1, 1, -1, -1, -1, -1, -1], [-1, -1, -1, 1, -1, -1, -1, 1], [1, -1, -1, -1, -1, -1, 1, 1], [1, -1, -1, -1, -1, -1, 1, -1]]', '[[false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 1, 1, 30, 0, 0, 1, 1),
(84, 61, '[[-1, -1, -1, 1, 1, -1, 1, -1], [1, -1, -1, -1, -1, 1, -1, -1], [-1, -1, -1, 1, -1, -1, 1, -1], [-1, -1, 1, -1, -1, -1, 1, -1], [-1, 1, 1, -1, -1, -1, -1, -1], [-1, -1, 1, -1, 1, -1, -1, -1], [-1, -1, 1, -1, -1, 1, -1, -1], [1, -1, -1, -1, -1, -1, 1, -1]]', '[[false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 32, 32, 30, 0, 0, 30, 1),
(85, 67, '[[-1, -1, -1, 1, -1, -1, -1, 1], [-1, -1, 1, 1, -1, -1, -1, -1], [-1, -1, -1, 1, -1, -1, 1, -1], [-1, 1, -1, -1, -1, -1, -1, 1], [-1, 1, -1, 1, -1, 1, -1, -1], [-1, -1, -1, -1, -1, -1, 1, 1], [1, -1, -1, 1, -1, -1, -1, -1], [-1, -1, 1, 1, -1, -1, -1, -1]]', '[[false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 30, 30, 32, 0, 0, 32, 1),
(86, 68, '[[-1, -1, -1, -1, -1, -1, 1, 1], [1, -1, -1, -1, -1, 1, -1, -1], [-1, -1, -1, -1, -1, -1, 1, 1], [-1, -1, -1, 1, -1, 1, 1, -1], [-1, -1, 1, -1, 1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, -1, 1], [1, -1, -1, -1, -1, -1, -1, 1], [1, -1, -1, -1, -1, -1, -1, 1]]', '[[false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 30, 30, 32, 0, 0, 32, 1),
(87, 66, '[[-1, 1, -1, -1, 1, -1, -1, -1], [-1, -1, -1, 1, -1, 1, -1, -1], [1, -1, -1, -1, -1, 1, -1, -1], [-1, -1, -1, -1, 1, 1, -1, -1], [1, -1, -1, -1, -1, 1, -1, -1], [-1, -1, -1, -1, 1, 1, -1, -1], [1, 1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, 1, 1, 1, -1, -1]]', '[[false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 32, 32, 30, 0, 0, 32, 1),
(88, 69, '[[-1, 1, -1, 1, -1, 1, -1, -1], [-1, -1, 1, -1, -1, 1, -1, -1], [1, 1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, 1, -1, 1], [-1, -1, 1, -1, -1, -1, 1, -1], [1, -1, -1, -1, -1, -1, 1, -1], [-1, -1, 1, -1, -1, 1, -1, -1], [-1, -1, 1, -1, -1, -1, 1, -1]]', '[[false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 1, 1, 30, 0, 0, 1, 1),
(89, 70, '[[1, -1, 1, -1, -1, -1, -1, -1], [-1, 1, 1, -1, -1, -1, 1, -1], [-1, -1, -1, -1, 1, -1, 1, -1], [1, -1, -1, -1, -1, -1, 1, -1], [-1, -1, 1, -1, 1, -1, -1, -1], [-1, 1, -1, -1, -1, -1, 1, -1], [-1, -1, -1, -1, -1, 1, 1, -1], [-1, -1, -1, -1, -1, -1, 1, 1]]', '[[false, false, false, false, true, true, true, true], [false, true, true, true, false, true, true, true], [true, true, true, true, true, true, true, true], [true, false, true, true, false, true, true, false], [false, false, true, true, true, false, true, true], [true, true, true, true, true, true, true, true], [false, false, true, false, true, true, true, false], [false, false, true, false, true, true, true, false]]', 17, 30, 30, 1, 9, 5, 30, 1),
(90, 71, '[[-1, 1, 1, -1, -1, -1, -1, -1], [1, -1, -1, 1, -1, -1, -1, -1], [-1, -1, -1, 1, -1, -1, 1, -1], [1, -1, 1, -1, -1, -1, -1, -1], [1, 1, -1, -1, -1, -1, -1, -1], [1, -1, -1, -1, -1, 1, -1, -1], [-1, -1, -1, -1, -1, -1, 1, 1], [-1, 1, 1, -1, -1, 1, -1, -1]]', '[[true, true, true, false, false, true, false, true], [true, true, true, true, true, false, true, false], [true, true, true, true, false, true, true, false], [true, true, true, true, false, true, true, false], [true, true, true, false, true, true, false, true], [true, true, true, true, true, true, false, true], [true, true, true, true, true, true, true, true], [true, true, true, true, false, true, true, true]]', 17, 1, 1, 30, 9, 8, 1, 1),
(91, 72, '[[-1, -1, 1, 1, -1, -1, -1, -1], [-1, -1, 1, -1, 1, -1, 1, -1], [-1, 1, -1, -1, -1, -1, -1, 1], [1, -1, -1, -1, 1, -1, -1, -1], [-1, -1, -1, 1, 1, -1, -1, -1], [-1, -1, 1, 1, -1, -1, -1, -1], [1, -1, -1, -1, 1, -1, -1, -1], [1, -1, 1, -1, -1, -1, -1, -1]]', '[[false, true, false, true, false, false, false, false], [false, true, true, false, true, false, true, true], [false, false, true, true, true, false, true, true], [false, true, true, true, true, true, true, false], [false, true, true, true, true, true, true, false], [true, true, false, true, true, true, true, true], [true, true, true, true, false, false, true, false], [true, true, true, true, true, false, false, false]]', 17, 30, 1, 30, 3, 9, 30, 1),
(92, 73, '[[-1, 1, -1, -1, -1, -1, -1, 1], [-1, -1, -1, -1, -1, 1, 1, -1], [1, -1, -1, -1, -1, -1, 1, -1], [-1, -1, -1, 1, -1, 1, -1, -1], [-1, 1, -1, 1, -1, -1, -1, -1], [1, -1, -1, 1, -1, -1, -1, -1], [-1, 1, -1, 1, 1, -1, -1, -1], [-1, 1, -1, -1, -1, -1, 1, -1]]', '[[false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 1, 1, 30, 0, 0, 1, 1),
(93, 76, '[[-1, -1, -1, 1, -1, -1, 1, -1], [1, 1, -1, -1, 1, -1, -1, -1], [1, -1, -1, -1, -1, -1, 1, -1], [1, -1, -1, -1, -1, -1, -1, 1], [-1, -1, -1, -1, 1, 1, -1, -1], [-1, -1, 1, -1, 1, -1, -1, -1], [-1, 1, -1, 1, -1, -1, -1, -1], [-1, 1, -1, -1, 1, -1, -1, -1]]', '[[false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 1, 1, 30, 0, 0, 1, 1),
(94, 77, '[[-1, -1, 1, -1, -1, -1, -1, 1], [-1, -1, -1, -1, 1, -1, -1, 1], [-1, 1, -1, -1, -1, -1, -1, 1], [-1, -1, -1, 1, -1, 1, -1, -1], [-1, 1, -1, 1, -1, -1, -1, -1], [-1, -1, -1, 1, -1, -1, 1, 1], [1, -1, -1, -1, -1, -1, -1, 1], [-1, -1, 1, -1, -1, -1, -1, 1]]', '[[false, true, true, true, true, false, true, true], [false, true, true, true, true, false, true, true], [false, true, false, false, false, false, true, true], [false, true, false, true, true, true, false, false], [false, true, false, true, true, true, false, false], [false, true, false, true, true, true, true, false], [false, false, false, false, false, false, false, false], [false, true, true, true, false, true, false, true]]', 17, 30, 1, 30, 5, 9, 30, 1),
(95, 78, '[[-1, 1, -1, 1, -1, -1, 1, -1], [-1, 1, -1, 1, -1, -1, -1, -1], [1, -1, -1, -1, -1, -1, 1, -1], [-1, 1, -1, -1, -1, 1, -1, -1], [-1, -1, -1, -1, 1, -1, -1, 1], [-1, -1, -1, -1, -1, 1, 1, -1], [1, -1, -1, -1, -1, -1, -1, 1], [-1, -1, -1, -1, -1, -1, 1, 1]]', '[[false, false, false, false, false, false, false, false], [true, true, true, true, false, false, false, false], [true, true, true, true, false, true, true, true], [true, true, true, true, true, true, true, true], [false, true, true, true, true, true, true, true], [false, false, true, true, false, true, true, true], [true, true, false, true, true, true, true, true], [true, true, true, false, false, true, true, true]]', 17, 30, 30, 1, 9, 5, 30, 1),
(96, 79, '[[-1, -1, -1, -1, 1, 1, -1, -1], [-1, -1, -1, 1, -1, -1, 1, -1], [1, 1, -1, -1, -1, -1, 1, -1], [-1, -1, -1, 1, 1, -1, -1, -1], [-1, -1, 1, -1, -1, -1, 1, -1], [-1, 1, -1, -1, 1, -1, -1, -1], [-1, -1, -1, -1, 1, -1, -1, 1], [-1, -1, -1, 1, -1, -1, 1, -1]]', '[[false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false], [false, false, false, false, false, false, false, false]]', 17, 30, 30, 1, 0, 0, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `players`
--

CREATE TABLE `players` (
  `id` bigint(20) NOT NULL,
  `is_online` bit(1) DEFAULT NULL,
  `last_update_time` bigint(20) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `socket_token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `players`
--

INSERT INTO `players` (`id`, `is_online`, `last_update_time`, `name`, `password`, `username`, `socket_token`) VALUES
(1, b'1', 0, 'Test', '123456789', 'Test', 'dsadsadsa-dsadasdsa-dsadsadsa'),
(30, b'1', 1616079830258, 'Behzad', '13799215', 'TheSanardev', 'b42106f6-e72d-434e-8548-10896880ccbb'),
(32, b'0', 0, 'Alireza', '12345', 'TheAlireza', 'fdfsvmdkvzdmvkds;VMSDKV-fdsvsDVDS'),
(33, b'0', 1616937775, 'ali', '13721580', 'AliArabic', 'b45c7ac1-8fc8-11eb-bf08-9c5c8e0f94c5'),
(34, b'0', 1616942388, 'Test Test', '12345', 'TheTest', '7226ba45-8fd3-11eb-8189-9c5c8e0f94c5'),
(35, b'0', 1616942572, 'TheArabic', '12345', 'AliArabic2', 'df95f01b-8fd3-11eb-9236-9c5c8e0f94c5'),
(36, b'0', 1616942825, 'teste', '12345', 'TheAli', '76619ca9-8fd4-11eb-93ed-9c5c8e0f94c5'),
(38, b'0', 1616942908, 'teste', '12345', 'TheAlii', 'a854699e-8fd4-11eb-9752-9c5c8e0f94c5');

-- --------------------------------------------------------

--
-- Table structure for table `private_chats`
--

CREATE TABLE `private_chats` (
  `id` int(11) NOT NULL,
  `sender_player_id` int(11) NOT NULL,
  `receiver_player_id` int(11) NOT NULL,
  `message` text CHARACTER SET utf8 NOT NULL,
  `timestamp` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `private_chats`
--

INSERT INTO `private_chats` (`id`, `sender_player_id`, `receiver_player_id`, `message`, `timestamp`) VALUES
(1, 1, 2, 'vfdgfdgfd', 2452014045),
(2, 1, 30, 'hello', 1616326074),
(3, 1, 30, 'hello', 1616326252),
(4, 30, 1, 'Salam', 1616337594),
(5, 30, 1, 'Test', 1616337829),
(6, 30, 1, 'Hello', 1616337830),
(7, 30, 1, 'ای بابا', 1616337940),
(8, 30, 1, 'ای ننه', 1616338057),
(9, 30, 1, 'چه گیری کردیم', 1616338064),
(10, 30, 1, 'به قرآن', 1616338079),
(11, 30, 1, '.', 1616338708),
(12, 30, 1, '.', 1616338709),
(13, 30, 1, '.', 1616338709),
(14, 30, 1, '.', 1616338709),
(15, 30, 1, '.', 1616338710),
(16, 30, 1, 'اصلا یه وضعی', 1616338714),
(17, 30, 1, 'نگم برات', 1616338715),
(18, 30, 1, 'سیدست یسشد یستشنید شسنتی دسشتنی سدشیت نشسدیستشنی دشستین شسدی شستین شسدیت شنسدی شستی ش', 1616338746),
(19, 30, 1, 'یسش دیشستیدشستنی شسدیست شنید شستنیدشس تنی دشستی دشستی شسدت ینشس', 1616338870),
(20, 30, 1, 'یشس یتسشنید شستنی دشست یشدست ینشسد یستشن یدشستین سش', 1616338872),
(21, 30, 1, 'یدسشتین شسدیستشندیستشنیدشست یسشد یستشند یستی دسش', 1616338874),
(22, 30, 1, 'یسشد یتشنسدی سشتی دسشتین شسدتین سشدیستید سشتنی', 1616338877),
(23, 30, 1, 'یسشدیستشن دیسشنتید شستیدشستنیدشست ی', 1616338879),
(24, 30, 1, 'یدسشتیسشدیتنسشیدشستیدسش', 1616338881),
(25, 30, 1, 'Ehem', 1616340194),
(26, 30, 1, 'چیزی برای گفتن داری؟', 1616340197),
(27, 30, 30, 'Salam', 1616610065),
(28, 30, 1, 'سلام', 1616611522),
(29, 30, 1, ',', 1616611547),
(30, 30, 1, '.', 1616611967),
(31, 30, 1, 'ALm', 1616621203),
(32, 30, 1, 'Salam', 1616621205),
(33, 30, 1, 'Hehe', 1616622512),
(34, 30, 1, 'kheili bahale', 1616622516),
(35, 30, 1, 'Haji', 1616661719),
(36, 30, 1, 'Pashmam', 1616661721),
(37, 1, 30, 'hello', 1616661734),
(38, 30, 1, 'chetoriii', 1616661741),
(39, 1, 30, 'قربونت تو خوبی؟', 1616661750),
(40, 30, 1, 'فدات', 1616661755),
(41, 30, 1, 'Salam', 1616703951),
(42, 30, 32, 'SALAM', 1616704535),
(43, 30, 32, 'سشمشئ', 1616704539),
(44, 32, 30, 'salam', 1616704549),
(45, 32, 30, 'khobi?', 1616704551),
(46, 30, 32, 'قربونت برم من خوبم تو چطوری', 1616704561),
(47, 32, 30, '.', 1616704566),
(48, 30, 32, 's', 1616704568),
(49, 1, 30, '.', 1616874444),
(50, 1, 30, '.', 1616874445),
(51, 1, 30, 'd', 1616874533),
(52, 1, 30, 'd', 1616874534),
(53, 30, 1, '.', 1616874549),
(54, 1, 30, '.', 1616874607),
(55, 30, 1, '.', 1616874613),
(56, 30, 1, '.', 1616874614),
(57, 30, 1, 'Salam', 1616874617),
(58, 1, 30, '.', 1616874680),
(59, 1, 30, '.', 1616874682),
(60, 30, 1, '.', 1616874916),
(61, 30, 1, '.', 1616874917),
(62, 1, 30, 'salam', 1616874919),
(63, 1, 30, 'khobi?', 1616874921),
(64, 30, 1, 'Salam', 1616928314),
(65, 30, 1, 'Chetori tooo', 1616928317),
(66, 30, 1, 'Brim soragh game', 1616928323),
(67, 38, 1, 'salam', 1616943249),
(68, 38, 1, 'khobi?', 1616943251),
(69, 1, 30, 'Salammmm', 1616943870),
(70, 1, 30, 'chetoriii', 1616943872);

-- --------------------------------------------------------

--
-- Table structure for table `socket_data`
--

CREATE TABLE `socket_data` (
  `id` bigint(20) NOT NULL,
  `connection_id` varchar(255) DEFAULT NULL,
  `player_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `waiting_games`
--

CREATE TABLE `waiting_games` (
  `id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  `timestamp` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `game_requests`
--
ALTER TABLE `game_requests`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `global_chat`
--
ALTER TABLE `global_chat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `minroob_game`
--
ALTER TABLE `minroob_game`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `players`
--
ALTER TABLE `players`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `UKp1chj5w2v1nune5xmmd94u1yj` (`username`);

--
-- Indexes for table `private_chats`
--
ALTER TABLE `private_chats`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socket_data`
--
ALTER TABLE `socket_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `waiting_games`
--
ALTER TABLE `waiting_games`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `game_requests`
--
ALTER TABLE `game_requests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=80;

--
-- AUTO_INCREMENT for table `global_chat`
--
ALTER TABLE `global_chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=367;

--
-- AUTO_INCREMENT for table `minroob_game`
--
ALTER TABLE `minroob_game`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT for table `players`
--
ALTER TABLE `players`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `private_chats`
--
ALTER TABLE `private_chats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT for table `waiting_games`
--
ALTER TABLE `waiting_games`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
