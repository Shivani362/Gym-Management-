-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 05, 2022 at 09:57 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gym_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_ad_memberlist`
--

CREATE TABLE `tbl_ad_memberlist` (
  `member_name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_no` int(10) NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_ad_payment`
--

CREATE TABLE `tbl_ad_payment` (
  `member_name` varchar(30) NOT NULL,
  `course` varchar(20) NOT NULL,
  `trainer_name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `total_amount` int(5) NOT NULL,
  `payment_ref_no` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_ad_subscription`
--

CREATE TABLE `tbl_ad_subscription` (
  `subs_name` text NOT NULL,
  `subs_duration` varchar(20) NOT NULL,
  `subs_description` text NOT NULL,
  `subs_trainer_type` varchar(20) NOT NULL,
  `subs_amount` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_ad_trainer`
--

CREATE TABLE `tbl_ad_trainer` (
  `trainer_name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_no` int(10) NOT NULL,
  `course_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_review`
--

CREATE TABLE `tbl_review` (
  `review_id` int(5) NOT NULL,
  `user_id` int(5) NOT NULL,
  `review_details` varchar(30) NOT NULL,
  `review_date_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_trainer_appointment`
--

CREATE TABLE `tbl_trainer_appointment` (
  `course` text NOT NULL,
  `requseted_appointment` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_trainer_esession`
--

CREATE TABLE `tbl_trainer_esession` (
  `course` varchar(20) NOT NULL,
  `trainer` varchar(30) NOT NULL,
  `online_links` varchar(50) NOT NULL,
  `from_time` time NOT NULL,
  `to_time` time NOT NULL,
  `day` text NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `user_id` int(5) NOT NULL,
  `user_type_id` int(5) NOT NULL,
  `full_name` varchar(40) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `dob` datetime NOT NULL,
  `address` varchar(150) NOT NULL,
  `email_id` varchar(25) NOT NULL,
  `password` varchar(10) NOT NULL,
  `mobile_no` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user_apppointment`
--

CREATE TABLE `tbl_user_apppointment` (
  `course` text NOT NULL,
  `trainer` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user_esession`
--

CREATE TABLE `tbl_user_esession` (
  `course` varchar(30) NOT NULL,
  `trainer` varchar(30) NOT NULL,
  `online links` varchar(50) NOT NULL,
  `from_time` time NOT NULL,
  `to_time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user_present_subs`
--

CREATE TABLE `tbl_user_present_subs` (
  `subs_name` varchar(30) NOT NULL,
  `subs_duration` varchar(20) NOT NULL,
  `subs_desc` text NOT NULL,
  `subs_trainer_type` varchar(15) NOT NULL,
  `amount` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user_type`
--

CREATE TABLE `tbl_user_type` (
  `user_type_id` int(5) NOT NULL,
  `user_type` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
