-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 2018-12-13 11:39:56
-- 服务器版本： 5.6.38
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wx_rkpass`
--

-- --------------------------------------------------------

--
-- 表的结构 `afternoon`
--

CREATE TABLE `afternoon` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optionA` text NOT NULL COMMENT '题目一问题',
  `optionAanswer` text NOT NULL COMMENT '题目一答案(答案中可能包含图片)',
  `optionAanswerImg` text NOT NULL COMMENT '题目一答案中的图片',
  `optionB` text NOT NULL COMMENT '题目二问题',
  `optionBanswer` text NOT NULL COMMENT '题目二答案(答案中可能包含图片)',
  `optionBanswerImg` text NOT NULL COMMENT '题目二答案中的图片',
  `optionC` text NOT NULL COMMENT '题目三问题',
  `optionCanswer` text NOT NULL COMMENT '题目三答案(答案中可能包含图片)',
  `optionCanswerImg` text NOT NULL COMMENT '题目三答案中的图片',
  `optionD` text NOT NULL COMMENT '题目四问题',
  `optionDanswer` text NOT NULL COMMENT '题目四答案(答案中可能包含图片)',
  `optionDanswerImg` text NOT NULL COMMENT '题目四答案中的图片',
  `optionE` text NOT NULL COMMENT '题目五问题',
  `optionEanswer` text NOT NULL COMMENT '题目五答案(答案中可能包含图片)',
  `optionEanswerImg` text NOT NULL COMMENT '题目五答案中的图片',
  `field` varchar(20) NOT NULL COMMENT '场次 20181即为2018年上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `dzsw_morning`
--

CREATE TABLE `dzsw_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20182即为2018下半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `media_morning`
--

CREATE TABLE `media_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `morning`
--

CREATE TABLE `morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `qrs_morning`
--

CREATE TABLE `qrs_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20182即为2018下半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `rjpcs_morning`
--

CREATE TABLE `rjpcs_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20182即为2018下半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `sjk_morning`
--

CREATE TABLE `sjk_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `wlgh_morning`
--

CREATE TABLE `wlgh_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `wl_morning`
--

CREATE TABLE `wl_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `xtfx_morning`
--

CREATE TABLE `xtfx_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `xtgh_morning`
--

CREATE TABLE `xtgh_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `xtjc_morning`
--

CREATE TABLE `xtjc_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `xtjg_morning`
--

CREATE TABLE `xtjg_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `xxaq_morning`
--

CREATE TABLE `xxaq_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `xxxtxm_morning`
--

CREATE TABLE `xxxtxm_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `xxxt_morning`
--

CREATE TABLE `xxxt_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `xx_morning`
--

CREATE TABLE `xx_morning` (
  `id` int(11) NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `afternoon`
--
ALTER TABLE `afternoon`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dzsw_morning`
--
ALTER TABLE `dzsw_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `media_morning`
--
ALTER TABLE `media_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `morning`
--
ALTER TABLE `morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `qrs_morning`
--
ALTER TABLE `qrs_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rjpcs_morning`
--
ALTER TABLE `rjpcs_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sjk_morning`
--
ALTER TABLE `sjk_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wlgh_morning`
--
ALTER TABLE `wlgh_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wl_morning`
--
ALTER TABLE `wl_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `xtfx_morning`
--
ALTER TABLE `xtfx_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `xtgh_morning`
--
ALTER TABLE `xtgh_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `xtjc_morning`
--
ALTER TABLE `xtjc_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `xtjg_morning`
--
ALTER TABLE `xtjg_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `xxaq_morning`
--
ALTER TABLE `xxaq_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `xxxtxm_morning`
--
ALTER TABLE `xxxtxm_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `xxxt_morning`
--
ALTER TABLE `xxxt_morning`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `xx_morning`
--
ALTER TABLE `xx_morning`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `afternoon`
--
ALTER TABLE `afternoon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `dzsw_morning`
--
ALTER TABLE `dzsw_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `media_morning`
--
ALTER TABLE `media_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `morning`
--
ALTER TABLE `morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `qrs_morning`
--
ALTER TABLE `qrs_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `rjpcs_morning`
--
ALTER TABLE `rjpcs_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `sjk_morning`
--
ALTER TABLE `sjk_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `wlgh_morning`
--
ALTER TABLE `wlgh_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `wl_morning`
--
ALTER TABLE `wl_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `xtfx_morning`
--
ALTER TABLE `xtfx_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `xtgh_morning`
--
ALTER TABLE `xtgh_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `xtjc_morning`
--
ALTER TABLE `xtjc_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `xtjg_morning`
--
ALTER TABLE `xtjg_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `xxaq_morning`
--
ALTER TABLE `xxaq_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `xxxtxm_morning`
--
ALTER TABLE `xxxtxm_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `xxxt_morning`
--
ALTER TABLE `xxxt_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `xx_morning`
--
ALTER TABLE `xx_morning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
