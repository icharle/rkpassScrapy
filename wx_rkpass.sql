/*
 Navicat Premium Data Transfer

 Source Server         : 本地数据库
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : localhost:3306
 Source Schema         : wx_rkpass

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : 65001

 Date: 14/07/2019 12:35:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cxy_morning
-- ----------------------------
DROP TABLE IF EXISTS `cxy_morning`;
CREATE TABLE `cxy_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) DEFAULT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) DEFAULT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1576 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for dzsw_morning
-- ----------------------------
DROP TABLE IF EXISTS `dzsw_morning`;
CREATE TABLE `dzsw_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) DEFAULT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) DEFAULT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=751 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for media_morning
-- ----------------------------
DROP TABLE IF EXISTS `media_morning`;
CREATE TABLE `media_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=601 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for morning
-- ----------------------------
DROP TABLE IF EXISTS `morning`;
CREATE TABLE `morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1576 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for qrs_morning
-- ----------------------------
DROP TABLE IF EXISTS `qrs_morning`;
CREATE TABLE `qrs_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) DEFAULT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) DEFAULT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=676 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for rjpcs_morning
-- ----------------------------
DROP TABLE IF EXISTS `rjpcs_morning`;
CREATE TABLE `rjpcs_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) DEFAULT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) DEFAULT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=751 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for sjk_morning
-- ----------------------------
DROP TABLE IF EXISTS `sjk_morning`;
CREATE TABLE `sjk_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=826 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for wl_morning
-- ----------------------------
DROP TABLE IF EXISTS `wl_morning`;
CREATE TABLE `wl_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1576 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for wlgh_morning
-- ----------------------------
DROP TABLE IF EXISTS `wlgh_morning`;
CREATE TABLE `wlgh_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=751 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for wlgl_morning
-- ----------------------------
DROP TABLE IF EXISTS `wlgl_morning`;
CREATE TABLE `wlgl_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) DEFAULT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) DEFAULT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1501 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xtfx_morning
-- ----------------------------
DROP TABLE IF EXISTS `xtfx_morning`;
CREATE TABLE `xtfx_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1651 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xtgh_morning
-- ----------------------------
DROP TABLE IF EXISTS `xtgh_morning`;
CREATE TABLE `xtgh_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=226 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xtjc_morning
-- ----------------------------
DROP TABLE IF EXISTS `xtjc_morning`;
CREATE TABLE `xtjc_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) DEFAULT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) DEFAULT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1576 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xtjg_morning
-- ----------------------------
DROP TABLE IF EXISTS `xtjg_morning`;
CREATE TABLE `xtjg_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=751 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xx_morning
-- ----------------------------
DROP TABLE IF EXISTS `xx_morning`;
CREATE TABLE `xx_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1501 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xxaq_morning
-- ----------------------------
DROP TABLE IF EXISTS `xxaq_morning`;
CREATE TABLE `xxaq_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xxcl_morning
-- ----------------------------
DROP TABLE IF EXISTS `xxcl_morning`;
CREATE TABLE `xxcl_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) DEFAULT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) DEFAULT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1501 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xxxt_morning
-- ----------------------------
DROP TABLE IF EXISTS `xxxt_morning`;
CREATE TABLE `xxxt_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) DEFAULT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) DEFAULT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=751 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for xxxtxm_morning
-- ----------------------------
DROP TABLE IF EXISTS `xxxtxm_morning`;
CREATE TABLE `xxxtxm_morning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL COMMENT '题目',
  `questionImg` text NOT NULL COMMENT '题目图片',
  `optiona` text NOT NULL COMMENT '选项A',
  `optionb` text NOT NULL COMMENT '选项B',
  `optionc` text NOT NULL COMMENT '选项C',
  `optiond` text NOT NULL COMMENT '选项D',
  `answer` text NOT NULL COMMENT '答案',
  `answeranalysis` text NOT NULL COMMENT '答案分析',
  `field` varchar(16) NOT NULL COMMENT '场次 20181即为2018上半年',
  `questionNum` varchar(8) NOT NULL COMMENT '题号',
  `knowledgeOne` varchar(32) NOT NULL COMMENT '题目一级分类',
  `knowledgeTwo` varchar(32) NOT NULL COMMENT '题目二级分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
