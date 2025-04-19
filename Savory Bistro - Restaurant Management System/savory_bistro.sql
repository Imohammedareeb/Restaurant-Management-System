-- Reservations table
CREATE TABLE `reservations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `guests` int(11) NOT NULL,
  `special_requests` text,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Menu items table
CREATE TABLE `menu_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text,
  `price` decimal(10,2) NOT NULL,
  `is_special` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
);

-- Insert sample menu data
INSERT INTO `menu_items` (`category`, `name`, `description`, `price`, `is_special`) VALUES
('Starters', 'Bruschetta', 'Toasted bread topped with tomatoes, garlic, and fresh basil', 9.99, 0),
('Starters', 'French Onion Soup', 'Classic soup with caramelized onions and melted cheese', 11.99, 0),
('Main Courses', 'Filet Mignon', 'Premium cut beef with red wine reduction', 39.99, 0),
('Main Courses', 'Herb-Crusted Rack of Lamb', 'Tender lamb with herb crust and mint sauce', 36.99, 1),
('Desserts', 'Crème Brûlée', 'Classic vanilla custard with caramelized sugar top', 10.99, 0),
('Desserts', 'Tiramisu', 'Coffee-flavored Italian dessert with mascarpone', 11.99, 0);