-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Окт 29 2024 г., 18:03
-- Версия сервера: 5.6.51
-- Версия PHP: 8.0.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `tree_view_db`
--

DELIMITER $$
--
-- Процедуры
--
CREATE DEFINER=`root`@`%` PROCEDURE `GetComponentHierarchy` ()   BEGIN
    SELECT c1.id AS parent_id, c1.name AS parent_name, c2.id AS child_id, c2.name AS child_name, s.amount
    FROM components c1
    LEFT JOIN structure s ON c1.id = s.id_pc
    LEFT JOIN components c2 ON s.id_component = c2.id
    ORDER BY c1.id, c2.id;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `components`
--

CREATE TABLE `components` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8mb4_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `components`
--

INSERT INTO `components` (`id`, `name`) VALUES
(1, 'Компьютер'),
(2, 'Монитор'),
(3, 'Системный блок'),
(4, 'Корпус'),
(5, 'Мат.плата'),
(6, 'Жесткий диск'),
(7, 'ОЗУ'),
(8, 'Процессор'),
(9, 'Клавиатура'),
(10, 'Мышьm');

-- --------------------------------------------------------

--
-- Структура таблицы `structure`
--

CREATE TABLE `structure` (
  `id_pc` int(11) DEFAULT NULL,
  `id_component` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `structure`
--

INSERT INTO `structure` (`id_pc`, `id_component`, `amount`) VALUES
(1, 2, 1),
(1, 3, 1),
(3, 4, 1),
(3, 5, 1),
(3, 6, 1),
(5, 7, 2),
(5, 8, 1),
(1, 9, 1),
(1, 10, 5);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `components`
--
ALTER TABLE `components`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `components`
--
ALTER TABLE `components`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
