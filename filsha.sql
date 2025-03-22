-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 17, 2025 at 01:46 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `filsha`
--

-- --------------------------------------------------------

--
-- Table structure for table `activity_log`
--

CREATE TABLE `activity_log` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `action` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `activity_log`
--

INSERT INTO `activity_log` (`id`, `user_id`, `action`, `description`, `timestamp`) VALUES
(1, 1, 'user_login', 'User florenz logged in.', '2025-01-12 02:25:33'),
(2, 1, 'file_deletion', 'File filsha.sql deleted.', '2025-01-12 02:25:38'),
(3, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-12 02:28:10'),
(4, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-12 02:31:52'),
(5, 2, 'user_login', 'User hanz logged in.', '2025-01-12 02:35:45'),
(6, 2, 'file_upload', 'File wallpaper.jpg uploaded and shared with florenz.', '2025-01-12 02:35:59'),
(7, 1, 'user_login', 'User florenz logged in.', '2025-01-12 02:37:01'),
(8, 1, 'file_download', 'File wallpaper.jpg downloaded.', '2025-01-12 02:37:03'),
(9, 1, 'user_login', 'User florenz logged in.', '2025-01-12 04:58:18'),
(10, 1, 'user_login', 'User florenz logged in.', '2025-01-12 05:05:43'),
(11, 1, 'user_login', 'User florenz logged in.', '2025-01-12 05:11:39'),
(12, 1, 'user_login', 'User florenz logged in.', '2025-01-12 05:14:37'),
(13, 1, 'file_upload', 'File react.html uploaded and shared with hanz.', '2025-01-12 05:14:48'),
(14, 1, 'file_deletion', 'File react.html deleted.', '2025-01-12 05:14:53'),
(15, 1, 'user_login', 'User florenz logged in.', '2025-01-12 05:32:38'),
(16, 1, 'file_upload', 'File filsha.sql uploaded and shared with hanz.', '2025-01-12 05:47:45'),
(17, 1, 'file_upload', 'File secure_file_transfer.sql uploaded and shared with hanz.', '2025-01-12 05:53:08'),
(18, 1, 'file_download', 'File filsha.sql downloaded.', '2025-01-12 05:53:24'),
(19, 1, 'user_login', 'User florenz logged in.', '2025-01-12 06:03:46'),
(20, 1, 'user_login', 'User florenz logged in.', '2025-01-12 06:04:14'),
(21, 1, 'user_login', 'User florenz logged in.', '2025-01-12 06:07:41'),
(22, 1, 'file_download', 'File wallpaper.jpg downloaded.', '2025-01-12 06:14:21'),
(23, 1, 'user_login', 'User florenz logged in.', '2025-01-12 06:18:21'),
(24, 1, 'file_deletion', 'File filsha.sql deleted.', '2025-01-12 06:18:25'),
(25, 1, 'file_deletion', 'File secure_file_transfer.sql deleted.', '2025-01-12 06:18:30'),
(26, 1, 'user_login', 'User florenz logged in.', '2025-01-12 06:26:13'),
(27, 1, 'file_upload', 'File react.html uploaded and shared with hanz.', '2025-01-12 06:26:26'),
(28, 1, 'file_deletion', 'File react.html deleted.', '2025-01-12 06:26:30'),
(29, 1, 'user_login', 'User florenz logged in.', '2025-01-12 06:28:52'),
(30, 1, 'user_login', 'User florenz logged in.', '2025-01-12 06:33:21'),
(31, 1, 'user_login', 'User florenz logged in.', '2025-01-12 06:37:11'),
(32, 2, 'user_login', 'User hanz logged in.', '2025-01-12 06:39:07'),
(33, 1, 'user_login', 'User florenz logged in.', '2025-01-12 06:43:51'),
(34, 2, 'user_login', 'User hanz logged in.', '2025-01-12 06:45:31'),
(35, 2, 'file_deletion', 'File wallpaper.jpg deleted.', '2025-01-12 06:45:35'),
(36, 2, 'file_upload', 'File secure_file_transfer.sql uploaded and shared with florenz.', '2025-01-12 06:46:17'),
(37, 1, 'user_login', 'User florenz logged in.', '2025-01-12 06:49:00'),
(38, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-13 00:15:22'),
(39, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-13 01:48:15'),
(40, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-13 01:54:00'),
(41, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-13 02:01:33'),
(42, 2, 'user_login', 'User hanz logged in.', '2025-01-13 02:46:18'),
(43, 1, 'user_login', 'User florenz logged in.', '2025-01-13 02:56:59'),
(44, 1, 'user_login', 'User florenz logged in.', '2025-01-13 02:58:31'),
(45, 1, 'user_login', 'User florenz logged in.', '2025-01-24 12:49:42'),
(46, 1, 'user_login', 'User florenz logged in.', '2025-01-24 12:50:00'),
(47, 1, 'user_login', 'User florenz logged in.', '2025-01-24 12:51:07'),
(48, 1, 'user_login', 'User florenz logged in.', '2025-01-24 12:52:26'),
(49, 1, 'user_login', 'User florenz logged in.', '2025-01-24 12:54:23'),
(50, 1, 'user_login', 'User florenz logged in.', '2025-01-24 12:55:30'),
(51, 1, 'user_login', 'User florenz logged in.', '2025-01-24 12:55:37'),
(52, 1, 'user_login', 'User florenz logged in.', '2025-01-24 13:00:48'),
(53, 1, 'user_login', 'User florenz logged in.', '2025-01-24 13:00:53'),
(54, 1, 'user_login', 'User florenz logged in.', '2025-01-24 13:01:33'),
(55, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-27 06:15:50'),
(56, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-27 06:22:18'),
(57, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-27 06:31:39'),
(58, 8, 'user_login', 'User renz logged in.', '2025-01-27 06:45:18'),
(59, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-27 06:50:51'),
(60, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-28 06:13:13'),
(61, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-28 06:30:03'),
(62, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-28 07:46:03'),
(63, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-28 12:25:33'),
(64, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-28 12:30:41'),
(65, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-29 11:43:13'),
(66, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-29 11:47:15'),
(67, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-29 11:47:29'),
(68, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-31 02:53:23'),
(69, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-31 02:59:00'),
(70, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-31 22:56:36'),
(71, NULL, 'admin_login', 'Admin admin logged in.', '2025-01-31 23:09:40'),
(72, 23, 'file_upload', 'File secure_file_transfer.sql uploaded and shared with florenz.olarte.', '2025-01-31 23:31:49'),
(73, 23, 'file_upload', 'File setup.exe uploaded and shared with florenz.olarte.', '2025-02-02 05:46:14'),
(74, 23, 'file_deletion', 'File setup.exe deleted.', '2025-02-02 05:46:21'),
(75, 23, 'file_deletion', 'File secure_file_transfer.sql deleted.', '2025-02-02 05:46:25'),
(76, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 05:57:49'),
(77, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 06:08:52'),
(78, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 06:12:43'),
(79, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 06:24:28'),
(80, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 06:40:43'),
(81, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 06:41:05'),
(82, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 06:41:26'),
(83, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 06:45:08'),
(84, 27, 'file_upload', 'File mongodb-windows-x86_64-8.0.4-signed.msi uploaded and shared with john_mark.olarte.', '2025-02-02 08:16:45'),
(85, 27, 'file_deletion', 'File mongodb-windows-x86_64-8.0.4-signed.msi deleted.', '2025-02-02 08:25:04'),
(86, 27, 'file_upload', 'File ngrok-v3-stable-windows-amd64.zip uploaded and shared with john_mark.olarte.', '2025-02-02 08:30:36'),
(87, 27, 'file_deletion', 'File ngrok-v3-stable-windows-amd64.zip deleted.', '2025-02-02 08:33:12'),
(88, 27, 'file_upload', 'File secure_file_transfer.sql uploaded and shared with john_mark.olarte.', '2025-02-02 08:49:53'),
(89, 27, 'file_deletion', 'File secure_file_transfer.sql deleted.', '2025-02-02 08:51:40'),
(90, 27, 'file_upload', 'File secure_file_transfer.sql uploaded and shared with john_mark.olarte.', '2025-02-02 08:52:04'),
(91, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 11:47:10'),
(92, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 11:55:50'),
(93, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 12:02:54'),
(94, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 12:14:29'),
(95, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-02 12:17:23'),
(96, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-03 04:34:03'),
(97, 36, 'file_upload', 'File iw6sp64_ship.exe uploaded and shared with florenz.', '2025-02-03 04:42:49'),
(98, 36, 'file_upload', 'File a10tabletin.bik uploaded and shared with florenz.olarte.', '2025-02-03 04:43:26'),
(99, 36, 'file_deletion', 'File a10tabletin.bik deleted.', '2025-02-03 04:43:37'),
(100, 36, 'file_upload', 'File users.sql uploaded and shared with florenz.olarte.', '2025-02-03 10:20:28'),
(101, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-03 10:37:51'),
(102, 37, 'file_upload', 'File users.sql uploaded and shared with florenz.olarte.', '2025-02-03 10:40:29'),
(103, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-03 12:55:07'),
(104, 38, 'file_upload', 'File templates-20250203T104801Z-001.zip uploaded and shared with florenz.olarte.', '2025-02-03 13:07:26'),
(105, 38, 'file_deletion', 'File templates-20250203T104801Z-001.zip deleted.', '2025-02-03 13:07:35'),
(106, 38, 'file_upload', 'File templates-20250203T104801Z-001.zip uploaded and shared with florenz.', '2025-02-03 13:08:29'),
(107, 38, 'file_upload', 'File templates-20250203T104801Z-001.zip uploaded and shared with florenz.olarte.', '2025-02-03 13:08:38'),
(108, 38, 'file_deletion', 'File templates-20250203T104801Z-001.zip deleted.', '2025-02-03 13:19:46'),
(109, 38, 'file_upload', 'File templates-20250203T104801Z-001.zip uploaded and shared with florenz.olarte.', '2025-02-03 13:19:58'),
(110, 38, 'file_upload', 'File static-20250203T143602Z-001.zip uploaded and shared with florenz.olarte.', '2025-02-04 04:16:28'),
(111, 38, 'file_deletion', 'File static-20250203T143602Z-001.zip deleted.', '2025-02-04 10:38:34'),
(112, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-04 10:39:05'),
(113, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-04 10:47:04'),
(114, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-04 10:56:06'),
(115, 38, 'file_upload', 'File secure-file-transfer.zip uploaded and shared with florenz.olarte.', '2025-02-04 15:36:09'),
(116, 38, 'file_download', 'File secure-file-transfer.zip downloaded.', '2025-02-04 15:37:03'),
(117, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-05 11:53:50'),
(118, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-05 11:55:43'),
(119, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-05 12:00:13'),
(120, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-05 12:01:42'),
(121, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-05 12:41:04'),
(122, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-05 12:41:50'),
(123, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-05 15:09:19'),
(124, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-05 15:16:48'),
(125, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-05 15:36:40'),
(126, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-05 23:20:35'),
(127, 43, 'file_upload', 'File admin_pic.png uploaded and shared with florenz.olarte.', '2025-02-05 23:29:14'),
(128, 44, 'file_upload', 'File FilSha-sample-20250205T102312Z-001.zip uploaded and shared with florenz.olarte.', '2025-02-06 01:11:13'),
(129, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-06 02:33:16'),
(130, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-07 00:01:21'),
(131, 43, 'file_deletion', 'File admin_pic.png deleted.', '2025-02-07 00:04:17'),
(132, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-07 07:07:49'),
(133, 43, 'file_upload', 'File admin_pic.png uploaded and shared with florenz.olarte.', '2025-02-09 01:53:30'),
(134, 43, 'file_upload', 'File admin_pic.png uploaded and shared with florenz.olarte.', '2025-02-09 03:38:56'),
(135, 43, 'file_deletion', 'File admin_pic.png deleted.', '2025-02-09 03:39:11'),
(136, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-09 03:40:04'),
(137, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-09 05:53:55'),
(138, 43, 'file_deletion', 'File admin_pic.png deleted.', '2025-02-09 05:57:35'),
(139, 43, 'file_upload', 'File OllamaSetup.exe uploaded and shared with florenz.olarte.', '2025-02-09 05:58:03'),
(140, 43, 'file_deletion', 'File OllamaSetup.exe deleted.', '2025-02-09 06:25:06'),
(141, 43, 'file_upload', 'File secure-file-transfer.zip uploaded and shared with florenz.olarte.', '2025-02-09 11:44:39'),
(142, 43, 'file_upload', 'File imagefile62.pak uploaded and shared with florenz.olarte.', '2025-02-09 11:47:31'),
(143, 43, 'file_deletion', 'File imagefile62.pak deleted.', '2025-02-09 11:50:28'),
(144, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-09 12:27:45'),
(145, 45, 'file_upload', 'File FilSha-sample-20250205T102312Z-001.zip uploaded and shared with florenz.olarte.', '2025-02-09 12:35:38'),
(146, 43, 'file_upload', 'File wallpaper.jpg uploaded and shared with hanz.alido1.', '2025-02-09 12:36:47'),
(147, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-09 12:45:59'),
(148, 43, 'file_deletion', 'File wallpaperflare.com_wallpaper.jpg deleted.', '2025-02-10 05:44:57'),
(149, 43, 'file_deletion', 'File wallpaper.jpg deleted.', '2025-02-10 05:45:06'),
(150, 43, 'file_download', 'File secure-file-transfer.zip downloaded.', '2025-02-10 05:47:06'),
(151, 43, 'file_deletion', 'File secure-file-transfer.zip deleted.', '2025-02-10 05:59:23'),
(152, 43, 'file_download', 'File LINUX COMMANDS - comptia-1.docx downloaded.', '2025-02-10 07:00:48'),
(153, 43, 'file_deletion', 'File ngrok-v3-stable-windows-amd64.zip deleted.', '2025-02-10 07:17:33'),
(154, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-10 14:16:57'),
(155, 43, 'file_deletion', 'File LINUX COMMANDS - comptia-1.docx deleted.', '2025-02-10 14:22:30'),
(156, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-11 10:41:51'),
(157, 43, 'file_deletion', 'File ALLMO$T - Boyfriend.mp3 deleted.', '2025-02-12 01:41:35'),
(158, 43, 'file_deletion', 'File FilSha.zip deleted.', '2025-02-16 12:13:27'),
(159, 43, 'file_deletion', 'File addUser.html deleted.', '2025-02-16 12:13:31'),
(160, 43, 'file_deletion', 'File addUser.html deleted.', '2025-02-16 12:13:36'),
(161, 43, 'file_deletion', 'File userLogin.html deleted.', '2025-02-17 01:49:13'),
(162, 43, 'file_deletion', 'File AdminDashboard.html deleted.', '2025-02-17 01:49:17'),
(163, 43, 'file_deletion', 'File adminLogin.html deleted.', '2025-02-17 01:49:21'),
(164, 43, 'file_deletion', 'File Fileshare.html deleted.', '2025-02-17 01:49:25'),
(165, 43, 'file_deletion', 'File help.html deleted.', '2025-02-17 01:49:29'),
(166, 43, 'file_deletion', 'File Userindex.html deleted.', '2025-02-17 01:49:33'),
(167, 43, 'file_deletion', 'File usermanagement.html deleted.', '2025-02-17 01:49:45'),
(168, 43, 'file_deletion', 'File users-profile.html deleted.', '2025-02-17 01:49:49'),
(169, 43, 'file_deletion', 'File files.zip deleted.', '2025-02-17 01:49:54'),
(170, 43, 'file_deletion', 'File files.zip deleted.', '2025-02-17 01:50:23'),
(171, 43, 'file_deletion', 'File userLogin.html deleted.', '2025-02-17 05:38:40'),
(172, 43, 'file_deletion', 'File addUser.html deleted.', '2025-02-17 05:38:44'),
(173, 43, 'file_deletion', 'File AdminDashboard.html deleted.', '2025-02-17 05:38:47'),
(174, 43, 'file_deletion', 'File adminLogin.html deleted.', '2025-02-17 05:38:51'),
(175, 43, 'file_deletion', 'File Fileshare.html deleted.', '2025-02-17 05:38:54'),
(176, 43, 'file_deletion', 'File help.html deleted.', '2025-02-17 05:38:57'),
(177, 43, 'file_deletion', 'File Userindex.html deleted.', '2025-02-17 05:39:01'),
(178, 43, 'file_deletion', 'File userLogin.html deleted.', '2025-02-17 05:39:04'),
(179, 43, 'file_deletion', 'File usermanagement.html deleted.', '2025-02-17 05:39:08'),
(180, 43, 'file_deletion', 'File users-profile.html deleted.', '2025-02-17 05:39:11'),
(181, 43, 'file_deletion', 'File Userindex.html deleted.', '2025-02-17 06:09:28'),
(182, 43, 'file_deletion', 'File files_20250217133802.zip deleted.', '2025-02-17 06:09:31'),
(183, 43, 'file_deletion', 'File help.html deleted.', '2025-02-17 06:09:35'),
(184, 43, 'file_deletion', 'File files_20250217140948.zip deleted.', '2025-02-17 06:12:49'),
(185, 43, 'file_deletion', 'File files_20250217142440.zip deleted.', '2025-02-17 06:31:57'),
(186, 43, 'file_deletion', 'File files_20250217142355.zip deleted.', '2025-02-17 06:32:00'),
(187, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-17 06:32:38'),
(188, 43, 'file_deletion', 'File files_20250217145133.zip deleted.', '2025-02-17 06:53:32'),
(189, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-17 12:49:28'),
(190, 43, 'file_deletion', 'File acc.txt deleted.', '2025-02-18 12:24:42'),
(191, 43, 'file_deletion', 'File acc.txt deleted.', '2025-02-18 12:25:21'),
(192, 43, 'file_deletion', 'File acc.txt deleted.', '2025-02-18 12:25:37'),
(193, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-18 12:52:03'),
(194, 43, 'file_deletion', 'File spark-md5.min.js deleted.', '2025-02-18 23:40:31'),
(195, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-19 23:12:49'),
(196, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-19 23:42:50'),
(197, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-19 23:50:57'),
(198, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-19 23:54:15'),
(199, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-21 03:29:30'),
(200, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-21 03:31:47'),
(201, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-21 03:35:02'),
(202, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-21 03:35:26'),
(203, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-23 13:58:42'),
(204, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-23 13:59:58'),
(205, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-24 06:39:03'),
(206, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-24 06:44:35'),
(207, 43, 'file_deletion', 'File files_20250221115849.zip deleted.', '2025-02-25 23:02:24'),
(208, 43, 'file_deletion', 'File VSCodeUserSetup-x64-1.97.2.exe deleted.', '2025-02-25 23:02:32'),
(209, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-27 03:48:05'),
(210, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-28 04:24:49'),
(211, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-28 04:25:54'),
(212, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-28 04:35:20'),
(213, NULL, 'admin_login', 'Admin admin logged in.', '2025-02-28 06:44:34'),
(214, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-04 05:03:13'),
(215, 43, 'file_deletion', 'File users-profile.html deleted.', '2025-03-05 00:36:54'),
(216, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-05 00:37:04'),
(217, 50, 'file_deletion', 'File webrtc-videochat-master.zip deleted.', '2025-03-05 04:41:08'),
(218, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-08 05:51:49'),
(219, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-09 09:35:53'),
(220, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-09 11:41:42'),
(221, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-09 12:56:18'),
(222, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-09 12:56:31'),
(223, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-09 12:57:00'),
(224, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-09 12:59:13'),
(225, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-09 12:59:29'),
(226, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-09 13:00:22'),
(227, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-09 13:00:56'),
(228, 43, 'file_deletion', 'File FilSha.zip deleted.', '2025-03-09 13:16:37'),
(229, 43, 'file_deletion', 'File files_20250226091848.zip deleted.', '2025-03-09 13:16:43'),
(230, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-09 17:22:51'),
(231, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-10 01:47:20'),
(232, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-10 02:34:02'),
(233, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-10 02:41:29'),
(234, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-10 06:58:18'),
(235, 43, 'file_deletion', 'File code_1.98.0-1741124782_amd64.deb deleted.', '2025-03-11 00:17:37'),
(236, 43, 'file_deletion', 'File xampp-linux-x64-8.2.12-0-installer.run deleted.', '2025-03-11 00:23:29'),
(237, 43, 'file_deletion', 'File burpsuite_community_linux_v2025_1_4.sh deleted.', '2025-03-11 02:31:35'),
(238, 50, 'file_deletion', 'File Module 11-12.zip deleted.', '2025-03-11 02:32:04'),
(239, 50, 'file_deletion', 'File FilSha.zip deleted.', '2025-03-11 02:32:07'),
(240, 43, 'file_deletion', 'File FilSha.zip deleted.', '2025-03-11 06:54:15'),
(241, 43, 'file_deletion', 'File burpsuite_community_linux_v2025_1_4(1).sh deleted.', '2025-03-11 06:55:38'),
(242, 43, 'file_deletion', 'File hanz.jpg deleted.', '2025-03-11 12:53:47'),
(243, 43, 'file_deletion', 'File hanz.jpg deleted.', '2025-03-11 12:54:20'),
(244, 43, 'file_deletion', 'File hanz.jpg deleted.', '2025-03-11 12:56:48'),
(245, 43, 'file_deletion', 'File hanz.jpg deleted.', '2025-03-11 12:56:51'),
(246, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-11 13:06:33'),
(247, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-11 13:27:10'),
(248, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-11 14:07:02'),
(249, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-11 14:36:25'),
(250, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-13 17:10:56'),
(251, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-15 08:04:05'),
(252, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-15 08:11:19'),
(253, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 07:38:24'),
(254, 50, 'file_deletion', 'File burpsuite_community_linux_v2025_1_4.sh deleted.', '2025-03-16 10:20:41'),
(255, 43, 'file_deletion', 'File barotac_nuevo.png deleted.', '2025-03-16 10:23:21'),
(256, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 12:13:32'),
(257, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 14:23:31'),
(258, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 14:24:35'),
(259, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 14:24:51'),
(260, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 14:25:11'),
(261, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 14:25:53'),
(262, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 14:26:28'),
(263, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 14:26:55'),
(264, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 14:28:18'),
(265, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 22:46:30'),
(266, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 22:49:02'),
(267, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 22:49:18'),
(268, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 22:50:29'),
(269, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 22:50:41'),
(270, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 23:04:21'),
(271, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 23:05:00'),
(272, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 23:19:50'),
(273, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 23:21:39'),
(274, NULL, 'admin_login', 'Admin admin logged in.', '2025-03-16 23:22:29'),
(275, 43, 'file_deletion', 'File zipped.zip deleted.', '2025-03-17 00:42:18');

-- --------------------------------------------------------

--
-- Table structure for table `brgycaptain`
--

CREATE TABLE `brgycaptain` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `age` int(11) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `position` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `barangay` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `brgycaptain`
--

INSERT INTO `brgycaptain` (`id`, `user_id`, `first_name`, `middle_name`, `last_name`, `gender`, `age`, `contact_number`, `position`, `email`, `barangay`) VALUES
(28, 43, 'florenz', 'mariano', 'olarte', 'Male', 21, '+639469463336', 'Barangay Captain', 'florenz.olarte@gmail.com', 'Agsirab'),
(34, 50, 'hanz', 'fronda', 'alido', 'Male', 21, '+639469463336', 'Barangay Captain', 'florenz.olarte@gmail.com', 'Agsirab');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `age` int(11) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `department` varchar(255) NOT NULL,
  `position` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE `files` (
  `id` int(11) NOT NULL,
  `filename` varchar(255) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `shared_with` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `expiration_time` datetime DEFAULT NULL,
  `size` bigint(20) DEFAULT NULL,
  `user_queries` text DEFAULT NULL,
  `virus_detected` tinyint(1) DEFAULT 0,
  `delete_after_download` tinyint(1) DEFAULT 0,
  `aes_key` varbinary(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `files`
--

INSERT INTO `files` (`id`, `filename`, `owner_id`, `shared_with`, `created_at`, `updated_at`, `expiration_time`, `size`, `user_queries`, `virus_detected`, `delete_after_download`, `aes_key`) VALUES
(105, 'Image.jpg', 43, 'hanz.alido', '2025-03-16 11:23:03', '2025-03-16 11:59:16', NULL, 160608, '', 0, 0, 0x27b25f55eb7826bae373f55cac835880c000ac1077f05e0e43b93f11e317ed1a),
(108, 'zipped.zip', 43, 'hanz.alido', '2025-03-17 00:46:13', '2025-03-17 00:46:28', '2025-03-24 08:46:13', 34777, '', 0, 1, 0x314bf79eed3dad3dc8a31d94042ba976a7e11394572802633177609d4cc641a6);

-- --------------------------------------------------------

--
-- Table structure for table `government_position`
--

CREATE TABLE `government_position` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `age` int(11) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `government_position` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `message` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `is_read` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`id`, `sender_id`, `receiver_id`, `message`, `created_at`, `is_read`) VALUES
(110, 50, 43, 'gAAAAABn1q-lspxzH4dGiIPJR_E8bHJXbNliS0bFODOxj9EFvx8fYXANxfZk-sdydnQsGSWRe-iCGeTxT_nBMoNAXuost8e7Mw==', '2025-03-16 11:01:57', 0),
(111, 43, 50, 'gAAAAABn1q_YQsHJd5LQxq00rvwnI1_HpRP1NLMOkugGMRCx5tMk8g2fVnvwHUzTsAe0Ien7K0d_9bm5Ctg8vCqaqHATxwYwnw==', '2025-03-16 11:02:48', 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('barangay-captain','government-position','municipal-employee') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `password_changed` tinyint(1) DEFAULT 0,
  `profile_picture` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`, `created_at`, `updated_at`, `password_changed`, `profile_picture`) VALUES
(43, 'florenz.olarte', '$2b$12$J0O.cuvplCgmDZXXe4UiuuWNM0WC0RGwxlA.aFYJuP..IgobcpD9K', 'barangay-captain', '2025-02-05 23:23:05', '2025-03-09 07:46:17', 1, 'profile_43.jpg'),
(50, 'hanz.alido', '$2b$12$HsKHsDG7ild09oiEb/JJ9uAlAv20hEGkl2r9P2KX5Nipw7bjcZp82', 'barangay-captain', '2025-03-04 05:03:48', '2025-03-09 08:10:05', 1, 'profile_50.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `user_inquiries`
--

CREATE TABLE `user_inquiries` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `status` enum('Pending','Resolved') DEFAULT 'Pending',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_inquiries`
--

INSERT INTO `user_inquiries` (`id`, `user_id`, `subject`, `description`, `status`, `created_at`) VALUES
(4, 43, 'hi', 'hello', 'Pending', '2025-03-11 14:05:28'),
(5, 43, 'HAAHA', 'HAHAH', 'Pending', '2025-03-11 14:37:58'),
(6, 50, 'hi', 'hello\r\n', 'Pending', '2025-03-11 14:51:09');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activity_log`
--
ALTER TABLE `activity_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `brgycaptain`
--
ALTER TABLE `brgycaptain`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`id`),
  ADD KEY `owner_id` (`owner_id`);

--
-- Indexes for table `government_position`
--
ALTER TABLE `government_position`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sender_id` (`sender_id`),
  ADD KEY `receiver_id` (`receiver_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `user_inquiries`
--
ALTER TABLE `user_inquiries`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity_log`
--
ALTER TABLE `activity_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=276;

--
-- AUTO_INCREMENT for table `brgycaptain`
--
ALTER TABLE `brgycaptain`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `files`
--
ALTER TABLE `files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;

--
-- AUTO_INCREMENT for table `government_position`
--
ALTER TABLE `government_position`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=112;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `user_inquiries`
--
ALTER TABLE `user_inquiries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `messages`
--
ALTER TABLE `messages`
  ADD CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`receiver_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `user_inquiries`
--
ALTER TABLE `user_inquiries`
  ADD CONSTRAINT `user_inquiries_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
