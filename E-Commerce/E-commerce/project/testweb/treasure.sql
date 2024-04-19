/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 80017 (8.0.17)
 Source Host           : localhost:3306
 Source Schema         : xm

 Target Server Type    : MySQL
 Target Server Version : 80017 (8.0.17)
 File Encoding         : 65001

 Date: 08/07/2023 15:32:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for treasure
-- ----------------------------
DROP TABLE IF EXISTS `treasure`;
CREATE TABLE `treasure`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `num` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of treasure
-- ----------------------------
INSERT INTO `treasure` VALUES (1, 'Gem', 4);
INSERT INTO `treasure` VALUES (2, 'Crown', 2);
INSERT INTO `treasure` VALUES (3, 'Talisman', 1);
INSERT INTO `treasure` VALUES (4, 'Blade', 6);
INSERT INTO `treasure` VALUES (5, 'Wand', 11);
INSERT INTO `treasure` VALUES (6, 'Flame', 5);
INSERT INTO `treasure` VALUES (7, 'Scale', 28);
INSERT INTO `treasure` VALUES (8, 'Clover', 22);

SET FOREIGN_KEY_CHECKS = 1;
