-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 20, 2020 at 06:07 PM
-- Server version: 5.7.29-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ink`
--

-- --------------------------------------------------------

--
-- Table structure for table `Account`
--

CREATE TABLE `Account` (
  `AccountID` int(11) NOT NULL,
  `Type` enum('Member','Admin') DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Password` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Account`
--

INSERT INTO `Account` (`AccountID`, `Type`, `Name`, `Email`, `Password`) VALUES
(1, 'Admin', 'Admin1', 'Admin1@gmail.com', '12345678'),
(2, 'Member', 'test1', 'test1@gmail.com', '123456789123456789'),
(3, 'Member', 'test2', 'test2@gmail.com', '12345678');

-- --------------------------------------------------------

--
-- Table structure for table `Brand`
--

CREATE TABLE `Brand` (
  `BrandID` int(11) NOT NULL,
  `BrandName` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Brand`
--

INSERT INTO `Brand` (`BrandID`, `BrandName`) VALUES
(1, 'Castel'),
(2, 'General'),
(3, 'Blick'),
(4, 'Prismcolor'),
(5, 'Isabel'),
(6, 'Waacom');

-- --------------------------------------------------------

--
-- Table structure for table `Cart`
--

CREATE TABLE `Cart` (
  `CartID` int(11) NOT NULL,
  `ProductID` int(11) DEFAULT NULL,
  `AccountID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Category`
--

CREATE TABLE `Category` (
  `CategoryID` int(11) NOT NULL,
  `CategoryName` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Category`
--

INSERT INTO `Category` (`CategoryID`, `CategoryName`) VALUES
(1, 'Drawing Pencils'),
(2, 'Colored Pencils'),
(3, 'Brushes'),
(4, 'Tablets');

-- --------------------------------------------------------

--
-- Table structure for table `OrderDesc`
--

CREATE TABLE `OrderDesc` (
  `OrderID` int(11) NOT NULL,
  `ProductID` int(11) DEFAULT NULL,
  `AccountID` int(11) DEFAULT NULL,
  `OrderDate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `OrderDesc`
--

INSERT INTO `OrderDesc` (`OrderID`, `ProductID`, `AccountID`, `OrderDate`) VALUES
(10, 2, 2, '2020-04-20 17:02:29'),
(11, 21, 2, '2020-04-20 17:02:29'),
(12, 2, 3, '2020-04-20 17:16:39'),
(13, 13, 3, '2020-04-20 17:16:39');

-- --------------------------------------------------------

--
-- Table structure for table `Product`
--

CREATE TABLE `Product` (
  `ProductID` int(11) NOT NULL,
  `CategoryID` int(11) DEFAULT NULL,
  `BrandID` int(11) DEFAULT NULL,
  `ProductName` varchar(50) DEFAULT NULL,
  `ProductDesc` text,
  `Picture` varchar(255) DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Product`
--

INSERT INTO `Product` (`ProductID`, `CategoryID`, `BrandID`, `ProductName`, `ProductDesc`, `Picture`, `Quantity`, `Price`) VALUES
(1, 1, 1, 'Castel Goldfaber Sketching Pencils', 'Students and aspiring artists can enjoy the advantages of quality drawing pencils at an economical price with these versatile graphite pencils. Crafted for a smooth consistent laydown, the leads are made of finely ground graphite and clay. A special bonding process helps protect the lead from breakage. Pencils are pre-sharpened. They are available separately, in eight degrees of hardness, from 4H (hardest) to 6B (softest). Goldfaber is Faber-Castell\'s student brand, offering high quality yet affordable pencils and pastels for students and beginning artists.', 'Castel_Goldfaber_Sketching_Pencils.jpg', 1000, 130),
(2, 1, 2, 'General Kimber Drawing Pencils', 'Non-porous Ceylon graphite cores are dense and durable. The core is \"Carbo-Welded\" to withstand four times the normal point pressure. The specially treated cedar wood casings sharpen easily. Pencils are pre-sharpened.', 'General_Kimber_Drawing_Pencils.jpg', 1000, 80),
(3, 1, 2, 'General Semi-Hex Drawing Pencils', 'The perfect go-to pencil for shading, sketching, and illustrating, General\'s Semi-Hex Drawing Pencils are made with top-quality graphite and encased in sustained yield California incense cedar with a blue lacquer finish. Ideal for artists of all skill levels, these pencils are pre-sharpened and ready to use. The set includes four Semi-Hex pencils, one each of HB, 2B, 4B, and 6B, plus a General\'s All Art Pink Eraser and a General\'s All Art pencil sharpener.', 'General_Semi-Hex_Drawing_Pencils.jpg', 600, 40),
(4, 1, 2, 'General Layout Pencil', 'This versatile pencil is great for art, sketching, and layout work. It is a standard size, round pencil that has very soft (6B equivalent), heavy, black graphite. Pencil is pre-sharpened.', 'General_Layout_Pencil.jpg', 860, 86),
(5, 1, 1, 'Castel 9000 Pencils', 'The Castell 9000, a genuinely classic pencil, was launched by Count Alexander von Faber-Castell in 1905. Over the years, the 9000\'s quality and finely graduated range of hardness degrees have made it a favorite of artists and illustrators. The Castell 9000 is the ideal pencil for every technical or artistic application, with break-resistant leads that are fully bonded to their casings. Since 1905, this top quality pencil with superior black leads, made of very finely ground graphite and clay, has been a favorite among artists, as well as for precision, technical drafting.', 'Castel_9000_Pencils.jpg', 660, 65),
(6, 2, 1, 'Castel Classic Color Pencil Sets', 'These classic, hexagonal colored pencils feature vivid, pigment-rich, thick cores for superior coloring and blending. A special bonding process makes Faber-Castell Classic Color Pencil cores super break-resistant and easy to sharpen. The set of 36 pencils is housed in a sturdy metal box. The set of 48 also includes a PVC-free eraser, two Faber-Castell Grip graphite pencils, and a pencil sharpener, housed in a sturdy metal box with removable trays. The pencil barrels are FSC-certified, made from wood sourced from well-managed forests.', 'Castel_Classic_Color_Pencil_Sets.jpg', 500, 25),
(7, 2, 1, 'Castel GRIP Colored EcoPencils', 'GRIP Colored EcoPencils contain more pigment — for richer colors! Sporting Faber-Castell\'s unique \"grip dots,\" the EcoPencil\'s ergonomic triangular shape provides the comfort and ease of tireless drawing while preventing it from rolling off surfaces.', 'Castel_GRIP_Colored_EcoPencils.jpg', 1000, 15),
(8, 2, 1, 'Castel Polychromos Pencils and Sets', 'Part of a unique color-matching system that encompasses all Faber-Castell Art & Graphic Products, Polychromos Colored Pencils contain the highest-quality pigments for unsurpassed lightfastness.  The buttery smooth color laydown offered by Polychromos pencils can be easily blended for layered effects, highlights, and transitions. Their break-resistant, water-resistant, smudgeproof 3.8 mm leads are encased in premium California cedar with Secureall bonding to resist breakage while providing sharp, fine lines and permanent, rich color. Pencils are pre-sharpened.  Every pencil contains a lightfastness (light resistance) rating, as follows: III very good (100+ years), II good, or I reasonable.  All sets, except where noted, are housed in sturdy metal tins.', 'Castel_Polychromos_Pencils_and_Sets.jpg', 400, 325),
(9, 2, 3, 'Blick Essentials Colored Pencil Sets', 'An essential tool for any classroom or art class, Blick Essentials Colored Pencils are also an economical choice — with no compromise in quality! Their smooth, strong 3.3 mm cores provide great color laydown for drawing, coloring, and blending, with minimal breakage. Quality pigments result in bold colors that young artists love. Available in a variety of sets, Blick Essentials Colored Pencils are 7\" (18 cm) long and come presharpened. They sharpen easily. Non-toxic .', 'Blick_Essentials_Colored_Pencil_Sets.jpg', 800, 40),
(10, 2, 4, 'Prismcolor Premier Colored Pencils and Sets', 'Prismacolor Premier Colored Pencils are the most popular colored pencils we sell. Each colored pencil features a thick, soft core made from brilliant, light-resistant pigments to ensure smooth, rich laydown and color saturation.  The colors are easily blended, slow to wear, break-resistant, and waterproof. Each 3.8 mm core is enclosed in a round cedar casing that is lacquered to match the core.  Manual sharpening is recommended for these pencils. Clogging can be prevented in electric sharpeners by periodically sharpening a graphite pencil to keep the blades clean. ', 'Prismcolor_Premier_Colored_Pencils_and_Sets.jpg', 700, 100),
(11, 3, 3, 'Blick Economy Golden Nylon Brushes and Sets', 'Synthetics are a perfect match for oil and acrylic paints in a classroom setting because they\'re easier to clean than natural hair brushes. They are more durable, and they can withstand the harsh elements of acrylic paints, with less damage. This affordably priced synthetic brush is a logical choice that can handle everything from detail painting to bold, sweeping strokes. Best of all, it\'s available in classroom packs that offer an assortment of sizes at substantial discount. The natural wood handles have a green gloss finish, with seamless polished aluminum ferrules. Ferrules are double crimped.', 'Blick_Economy_Golden_Nylon_Brushes_and_Sets.jpg', 750, 310),
(13, 3, 3, 'Blick Bristle Brushes', 'Lots of great shapes and great looks! This is our most impressive range of shapes and sizes. The Blick Studio Bristle is a truly beautiful, yet affordable brush. Unbleached natural bristle from China sets strikingly on rich lacquered handles, individually sized to balance each size head. A mid-level of firmness makes these the most spontaneous and expressive of our bristles.', 'Blick_Bristle_Brushes.jpg', 900, 50),
(17, 3, 5, 'IsabeI Pure Squirrel Mop Pocket Brush', 'These travel-ready brushes are just like the traditional versions, with a brass cap that protects the delicate filaments. When removed, the cap fits on the end to form a full watercolor-length handle. The Series 6202 Pure Squirrel Mop Pocket Brush is available in Size 0 with a 3/16\" diameter.', 'Isabel_Pure_Squirrel_Mop_Pocket_Brush.jpg', 1000, 38),
(18, 3, 5, 'Isabel Red Sable Brushes', 'Isabey Red Sable Brushes are handmade using 100% Pure Red Sable. Available in a variety of shapes and sizes, each brush offers unique qualities for every type of watercolor paint and every technique.', 'Isabel_Red_Sable_Brushes.jpg', 900, 75),
(19, 3, 5, 'Isabel Kolinsky Retouch Brush', 'This Isabey Kolinsky brush is great for all your retouching and spotting needs. Featuring a very sharp point, this brush is perfect for detail and precision work. The lower belly and shorter hairs form a resilient tip and give you maximum control. This superior specialty brush also features a seamless nickel-plated brass ferrule and a sleek, black polished handle.', 'Isabel_Kolinsky_Retouch_Brush.jpg', 800, 40),
(20, 4, 6, 'Waacom MobileStudio Pro', 'Enjoy true independence to create anything, anywhere. Wacom MobileStudio Pro gives you a whole studio of creative tools in your hands – an awesome display, a precise pen and enhanced computing power to run leading creative software simultaneously. And with its long-lasting battery, you can bring your ideas to life without disrupting your flow. You’ll love how creative and productive you can be.', 'Waacom_MobileStudio_Pro.jpg', 1050, 2600),
(21, 4, 6, 'Waacom One Creative Pen Display', 'Whether you’re just starting in digital creation, want to add a twist to your visual thinking or looking to improve your digital expression, Wacom One delivers a great experience. It comes with all the essentials to spice up your digital life. There’s the natural pen feel on the 13.3” screen, the included creative software – even the ability to connect to certain Android devices. And it’s compatible with leading pen brands too. Open up new possibilities with Wacom One.', 'Waacom_One_Creative_Pen_Display.jpg', 600, 3000),
(22, 4, 6, 'Waacom Bamboo One', 'Sketch, doodle, create greeting cards, animation and much more, the One by Wacom opens up a whole new world of creative possibilities. Ideal for graphic designers and animators, the One lets you draw, write and edit photos digitally, with the ease of using a pen. It comes with a pressure-sensitive pen that along with the smooth tablet surface gives a pen-on-paper feel. Featuring a compact design, this sleek tablet is not only perfect for small desktop areas, but it is also portable. The wide-format active area of this tablet gives you more freedom of movement and allows for longer pen strokes. This tablet is designed for ambidextrous use. Product Description If you love drawing caricatures and cartooning, then you will definitely love the Wacom One Graphics tablet.', 'Wacom_Bamboo_One.jpeg', 860, 560),
(23, 4, 6, 'Waacom Intuos', 'Pursue your creative interests with this pen and touch tablet from WACOM which is designed to help you enhance your design process. It features a battery-free pen and a tablet with a bigger drawing area and four ExpressKeys to help you access your shortcuts easily. ', 'Waacom_Intuos.jpeg', 800, 1900),
(24, 4, 6, 'Waacom Cintiq Graphics Tablet', 'Wacom Cintiq 16 pen display, Wacom Pro Pen 2, detachable pen holder with 3 replacement nibs (standard) and nib removal tool, 3-in-1 cable (1.8 m), AC adapter (12 V, 3 A, 36 W), power cable (1.8 m), Quick Start Guide, warranty card', 'Waacom_Cintiq_Graphics_Tablet.jpeg', 900, 700);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Account`
--
ALTER TABLE `Account`
  ADD PRIMARY KEY (`AccountID`);

--
-- Indexes for table `Brand`
--
ALTER TABLE `Brand`
  ADD PRIMARY KEY (`BrandID`);

--
-- Indexes for table `Cart`
--
ALTER TABLE `Cart`
  ADD PRIMARY KEY (`CartID`),
  ADD KEY `AccountID` (`AccountID`),
  ADD KEY `ProductID` (`ProductID`);

--
-- Indexes for table `Category`
--
ALTER TABLE `Category`
  ADD PRIMARY KEY (`CategoryID`);

--
-- Indexes for table `OrderDesc`
--
ALTER TABLE `OrderDesc`
  ADD PRIMARY KEY (`OrderID`),
  ADD KEY `ProductID` (`ProductID`),
  ADD KEY `AccountID` (`AccountID`);

--
-- Indexes for table `Product`
--
ALTER TABLE `Product`
  ADD PRIMARY KEY (`ProductID`),
  ADD KEY `CategoryID` (`CategoryID`),
  ADD KEY `BrandID` (`BrandID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Account`
--
ALTER TABLE `Account`
  MODIFY `AccountID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `Brand`
--
ALTER TABLE `Brand`
  MODIFY `BrandID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `Cart`
--
ALTER TABLE `Cart`
  MODIFY `CartID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `Category`
--
ALTER TABLE `Category`
  MODIFY `CategoryID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `OrderDesc`
--
ALTER TABLE `OrderDesc`
  MODIFY `OrderID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `Product`
--
ALTER TABLE `Product`
  MODIFY `ProductID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `Cart`
--
ALTER TABLE `Cart`
  ADD CONSTRAINT `Cart_ibfk_1` FOREIGN KEY (`AccountID`) REFERENCES `Account` (`AccountID`),
  ADD CONSTRAINT `Cart_ibfk_2` FOREIGN KEY (`ProductID`) REFERENCES `Product` (`ProductID`);

--
-- Constraints for table `OrderDesc`
--
ALTER TABLE `OrderDesc`
  ADD CONSTRAINT `OrderDesc_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `Product` (`ProductID`),
  ADD CONSTRAINT `OrderDesc_ibfk_2` FOREIGN KEY (`AccountID`) REFERENCES `Account` (`AccountID`);

--
-- Constraints for table `Product`
--
ALTER TABLE `Product`
  ADD CONSTRAINT `Product_ibfk_1` FOREIGN KEY (`CategoryID`) REFERENCES `Category` (`CategoryID`),
  ADD CONSTRAINT `Product_ibfk_2` FOREIGN KEY (`BrandID`) REFERENCES `Brand` (`BrandID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
