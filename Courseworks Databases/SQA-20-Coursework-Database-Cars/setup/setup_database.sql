
DROP TABLE IF EXISTS Car;
CREATE TABLE Car (
    regNo TEXT PRIMARY KEY,
    make TEXT,
    model TEXT,
    year INTEGER,
    customerID INTEGER
);

DROP TABLE IF EXISTS Garage;
CREATE TABLE Garage (
    garageID TEXT PRIMARY KEY,
    garageName TEXT,
    address TEXT,
    town TEXT,
    postCode TEXT,
    phoneNo TEXT
);

DROP TABLE IF EXISTS Customer;
CREATE TABLE Customer (
    customerID INTEGER PRIMARY KEY,
    forename TEXT,
    surname TEXT,
    address TEXT,
    postCode TEXT,
    phoneNo TEXT
);

DROP TABLE IF EXISTS Job;
CREATE TABLE Job (
    jobID TEXT PRIMARY KEY,
    garageID TEXT,
    dateIn TEXT,
    dateOut TEXT,
    regNo TEXT,
    cost REAL,
    FOREIGN KEY (garageID) REFERENCES Garage(garageID),
    FOREIGN KEY (regNo) REFERENCES Car(regNo)
);

INSERT INTO Car (regNo, make, model, year, customerID) VALUES
('50 J4C08', 'Subaru', 'Outback', 2011, 8291),
('83 5TU4RT', 'Mazda', '3', 2012, 1872),
('AF66 XFP', 'Ford', 'F-150', 2016, 4668),
('AR16 WJY', 'Mini', 'One', 2016, 6473),
('BD62 EWT', 'Kia', 'Rio', 2012, 6275),
('BM18 TWY', 'Mazda', 'CX-3', 2018, 4917),
('BP67 COO', 'Bentley', 'Continental', 2017, 1762),
('C4LI 23', 'Ferrari', 'California', 2015, 9579),
('CN61 XXH', 'Mitsubishi', 'Outlander', 2011, 8869),
('CR10 WQI', 'Kia', 'Sportage', 2010, 1872),
('DE17 ENG', 'Volvo', 'XC90', 2017, 6816),
('FN12 BXW', 'BMW', '1 Series', 2012, 1872),
('FO66 VMG', 'Ford', 'Fiesta', 2016, 2539),
('FS63 RXI', 'Volkswagen', 'Golf', 2013, 3345),
('GE15 KWE', 'Nissan', 'Qashqai', 2015, 8404),
('GZ68 VKP', 'Aston Martin', 'Vantage', 2018, 5475),
('HQ68 KOX', 'Toyota', 'Corolla', 2018, 4668),
('IM15 PMJ', 'Volvo', 'V40', 2015, 1566),
('J3NN 338', 'Citroen', 'C3', 2014, 8127),
('KG19 YBI', 'Nissan', 'Mokka', 2019, 7486),
('KP67 LRK', 'Nissan', 'Qashqai', 2017, 7563),
('LH65 MZX', 'Fiat', '500', 2015, 5441),
('M4S Q4TT', 'Maserati', 'Quattroporte', 2018, 4707),
('M4X PRR', 'Mitsubishi', 'Mirage', 2012, 1025),
('NJ11 DSF', 'Aston Martin', 'Virage', 2011, 2026),
('NR13 DIC', 'Peugeot', '308', 2013, 4730),
('P921 BCP', 'Toyota', 'Celica', 2015, 8127),
('QA16 NAX', 'Hyundai', 'ix35', 2016, 3345),
('QE66 GTT', 'Mini', 'Hatch', 2016, 1189),
('QI17 JUC', 'BMW', 'M2', 2017, 5475),
('QQ16 UKE', 'Bentley', 'Mulsanne', 2016, 1762),
('QR14 RGL', 'Suzuki', 'Swift', 2014, 8291),
('RS67 KPE', 'BMW', 'X1', 2017, 2026),
('SF11 HQS', 'Ford', 'Fiesta', 2011, 5786),
('SH63 MWG', 'Kia', 'Sorento', 2013, 1566),
('SO13 PWJ', 'Mitsubishi', 'Lancer', 2013, 1025),
('SR14 THK', 'Nissan', 'Juke', 2014, 4730),
('TA19 POK', 'Ford', 'Focus', 2019, 8723),
('TH67 CHK', 'Fiat', '500', 2017, 5786),
('THW 83', 'Audi', 'A4', 2018, 4707),
('TN62 XUS', 'Saab', '09-May', 2012, 7380),
('UY11 QPB', 'Nissan', 'Juke', 2011, 7416),
('V10 L3T', 'Mercedes', 'C Class', 2011, 2762),
('VX13 LIE', 'Nissan', 'Micra', 2013, 5475),
('W33 COL', 'Maserati', 'Ghibli', 2015, 4707),
('WC64 TJE', 'Vauxhall', 'Astra', 2014, 8869),
('WH10 OVH', 'Toyota', 'Yaris', 2010, 4668),
('WR13 QFR', 'Audi', 'A6', 2013, 6473),
('WZ19 EVI', 'Ferrari', '488', 2019, 4591),
('XV63 ZAS', 'Volkswagen', 'Passat', 2013, 3345),
('YE12 WUQ', 'Subaru', 'Forester', 2012, 2539),
('YU15 CQT', 'Peugeot', '208', 2015, 8869),
('ZC62 LCH', 'Toyota', 'Prius', 2012, 1189),
('ZN68 OXT', 'Citroen', 'C4', 2018, 5786);

INSERT INTO Garage (garageID, garageName, address, town, postCode, phoneNo) VALUES
('G59-G', 'Pit Stop Glasgow Shawlands', '42 Kingsgate', 'Glasgow', 'G41 3EU', '0141 632 9541'),
('G61-E', 'Pit Stop Edinburgh', '98 Glen Road', 'Edinburgh', 'EH11 1KJ', '0131 538 1297'),
('G72-S', 'Pit Stop Stirling', '6 Royal Stuart Way', 'Stirling', 'FK8 7DS', '0178 647 1946'),
('G82-G', 'Pit Stop Glasgow Govan', 'Unit 3 Eastlinks Industrial Estate', 'Glasgow', 'G51 9PD', '0141 649 6620'),
('G98-K', 'Pit Stop Kilmarnock', '112 Greenbank View', 'Kilmarnock', 'KA1 6AZ', '0156 352 3512');

INSERT INTO Customer (customerID, forename, surname, address, postCode, phoneNo) VALUES
(7486, 'Ian', 'Arthur', '330 West Street', 'G87 2VB', '07989 914299'),
(7563, 'David', 'Ballantyne', '87 King''s Place', 'G9 7WH', '07873 468849'),
(8869, 'Stuart', 'Barnes', '256 Hope Street', 'KA6 0KS', '07153 426507'),
(6816, 'John', 'Brown', '23 Bellflower Gardens', 'G58 6SL', '07771 458506'),
(1872, 'Stuart', 'Campbell', '2/8 Roberston Gait', 'EH11 1HJ', '07871 142681'),
(6473, 'Jack', 'Cook', '65 Castle Place', 'G5 6ME', '07006 672479'),
(9579, 'Laura', 'Forbes', '90 Church Street', 'KA7 2LG', '07487 256037'),
(1189, 'Jennifer', 'Hart', '9A Douglas Place', 'EH1 5LD', '07900 537290'),
(4668, 'Abdur', 'Imran', '98 Springfield Road', 'FK2 0HO', '07361 397435'),
(6275, 'Adil', 'Jabbar', '90 Market Street', 'G5 6CK', '07413 791995'),
(5786, 'Mark', 'Jones', '23 Queensway', 'G2 1LZ', '07174 763203'),
(7380, 'Mark', 'Jones', '8 Windsor Avenue', 'G6 9HA', '07868 666171'),
(7416, 'Stephanie', 'Jones', '87 Hampshire Gardens', 'G74 3VX', '07615 836502'),
(8291, 'Jacob', 'Joseph', '22 Deanston Street', 'KA0 0TP', '07945 061491'),
(1025, 'Max', 'Power', '189 Hunter Drive', 'G55 6TG', '07766 336835'),
(4730, 'Stewart', 'Regan', '134 Burton Lane', 'FK6 0XT', '07115 051817'),
(4917, 'Lawrence', 'Rose', '38 South Street', 'FK7 7BF', '07542 139739'),
  (2762, 'Violet', 'Rose', '42 Mallot Street', 'EH9 2AH', '07071 225929'),
  (8404, 'Rebecca', 'Shearer', '12 Hill Street', 'KA3 9WU', '07154 704172'),
  (8723, 'Alan', 'Simpson', '5B Church Lane', 'KA5 9RX', '07768 478897'),
  (1762, 'Laura', 'Skelly', '99 Queensway', 'EH7 4UZ', '07008 072455'),
  (2026, 'Mark', 'Slorance', '200 Edward Drive', 'EH71 3UM', '07194 413012'),
  (1566, 'Angela', 'Smith', '178 Mount Stuart Street', 'EH43 5UJ', '07110 577507'),
  (4707, 'Angela', 'Smith', '230 Bellwood Drive', 'FK3 7WP', '07233 894939'),
  (4591, 'Derek', 'Tsang', '243 Hill Street', 'FK1 1FM', '07160 225407'),
  (3345, 'Amy', 'Williams', '15 King Street', 'EH9 9UE', '07092 544935'),
  (2539, 'Colin', 'Wilson', '12 Hunter Drive', 'EH83 6NE', '07826 411735'),
  (5441, 'Colin', 'Wilson', '42 Mill Lane', 'FK9 2QY', '07529 702292'),
  (8127, 'Jennifer', 'Wilson', '2 West Street', 'G98 7FD', '07679 591563'),
  (5475, 'Lawrie', 'Young', '70 Drew Street', 'G1 9CJ', '07817 412513');

  INSERT INTO Job (jobID, garageID, dateIn, dateOut, regNo, cost) VALUES
  ('J002', 'G59-G', '02-Jan-20', '10-Jan-20', 'ZN68 OXT', '£393.60'),
  ('J011', 'G61-E', '02-Jan-20', '19-Jan-20', 'ZC62 LCH', '£507.64'),
  ('J028', 'G98-K', '05-Jan-20', '19-Jan-20', 'YU15 CQT', '£84.92'),
  ('J054', 'G61-E', '18-Jan-20', '20-Jan-20', 'YE12 WUQ', '£77.12'),
  ('J065', 'G61-E', '31-Jan-20', '31-Jan-20', 'XV63 ZAS', '£274.93'),
  ('J042', 'G72-S', '22-Jan-20', '23-Jan-20', 'WZ19 EVI', '£657.41'),
  ('J055', 'G59-G', '28-Jan-20', '31-Jan-20', 'WR13 QFR', '£87.71'),
  ('J034', 'G72-S', '11-Jan-20', '19-Jan-20', 'WH10 OVH', '£180.71'),
  ('J062', 'G98-K', '27-Jan-20', '30-Jan-20', 'WC64 TJE', '£121.77'),
  ('J037', 'G72-S', '19-Jan-20', '27-Jan-20', 'W33 COL', '£603.97'),
  ('J040', 'G59-G', '29-Jan-20', '30-Jan-20', 'VX13 LIE', '£24.50'),
  ('J033', 'G61-E', '10-Jan-20', '19-Jan-20', 'V10 L3T', '£108.64'),
  ('J021', 'G82-G', '14-Jan-20', '19-Jan-20', 'UY11 QPB', '£90.00'),
  ('J032', 'G82-G', '15-Jan-20', '23-Jan-20', 'UY11 QPB', '£65.98'),
  ('J030', 'G59-G', '08-Jan-20', '09-Jan-20', 'TN62 XUS', '£464.84'),
  ('J066', 'G72-S', '25-Jan-20', '26-Jan-20', 'THW 83', '£83.97'),
  ('J023', 'G59-G', '07-Jan-20', '14-Jan-20', 'TH67 CHK', '£74.20'),
  ('J039', 'G59-G', '22-Jan-20', '27-Jan-20', 'TH67 CHK', '£150.08'),
  ('J068', 'G98-K', '03-Jan-20', '08-Jan-20', 'TA19 POK', '£92.12'),
  ('J025', 'G72-S', '10-Jan-20', '18-Jan-20', 'SR14 THK', '£77.04'),
  ('J035', 'G82-G', '13-Jan-20', '28-Jan-20', 'SO13 PWJ', '£114.07'),
  ('J022', 'G61-E', '05-Jan-20', '06-Jan-20', 'SH63 MWG', '£704.80'),
  ('J027', 'G61-E', '10-Jan-20', '19-Jan-20', 'SH63 MWG', '£464.85'),
  ('J016', 'G59-G', '07-Jan-20', '09-Jan-20', 'SF11 HQS', '£345.00'),
  ('J041', 'G61-E', '25-Jan-20', '25-Jan-20', 'RS67 KPE', '£18.20'),
  ('J003', 'G82-G', '02-Jan-20', '04-Jan-20', 'QR14 RGL', '£55.96'),
  ('J015', 'G82-G', '08-Jan-20', '26-Jan-20', 'QR14 RGL', '£45.50'),
  ('J036', 'G82-G', '23-Jan-20', '28-Jan-20', 'QR14 RGL', '£112.00'),
  ('J013', 'G61-E', '03-Jan-20', '19-Jan-20', 'QQ16 UKE', '£130.88'),
  ('J060', 'G61-E', '21-Jan-20', '30-Jan-20', 'QQ16 UKE', '£95.70'),
  ('J006', 'G59-G', '06-Jan-20', '08-Jan-20', 'QI17 JUC', '£150.99'),
  ('J053', 'G61-E', '17-Jan-20', '19-Jan-20', 'QE66 GTT', '£320.98'),
  ('J017', 'G61-E', '03-Jan-20', '26-Jan-20', 'QA16 NAX', '£231.00'),
  ('J045', 'G82-G', '18-Jan-20', '20-Jan-20', 'P921 BCP', '£74.50'),
  ('J001', 'G72-S', '02-Jan-20', '10-Jan-20', 'NR13 DIC', '£117.12'),
  ('J050', 'G72-S', '20-Jan-20', '20-Jan-20', 'NR13 DIC', '£283.46'),
  ('J018', 'G61-E', '05-Jan-20', '23-Jan-20', 'NJ11 DSF', '£74.91'),
  ('J046', 'G82-G', '13-Jan-20', '28-Jan-20', 'M4X PRR', '£45.70'),
  ('J038', 'G72-S', '18-Jan-20', '24-Jan-20', 'M4S Q4TT', '£25.99'),
  ('J057', 'G72-S', '19-Jan-20', '20-Jan-20', 'M4S Q4TT', '£921.46'),
  ('J007', 'G72-S', '04-Jan-20', '19-Jan-20', 'LH65 MZX', '£701.10'),
  ('J020', 'G82-G', '14-Jan-20', '14-Jan-20', 'KP67 LRK', '£102.20'),
  ('J059', 'G82-G', '26-Jan-20', '31-Jan-20', 'KP67 LRK', '£313.74'),
  ('J005', 'G82-G', '17-Jan-20', '21-Jan-20', 'KG19 YBI', '£298.73'),
  ('J070', 'G82-G', '05-Jan-20', '07-Jan-20', 'KG19 YBI', '£71.90'),
  ('J067', 'G82-G', '14-Jan-20', '15-Jan-20', 'J3NN 338', '£121.29'),
  ('J019', 'G61-E', '07-Jan-20', '25-Jan-20', 'IM15 PMJ', '£133.81'),
  ('J063', 'G72-S', '23-Jan-20', '23-Jan-20', 'HQ68 KOX', '£23.00'),
  ('J004', 'G59-G', '04-Jan-20', '06-Jan-20', 'GZ68 VKP', '£484.42'),
  ('J049', 'G59-G', '16-Jan-20', '27-Jan-20', 'GZ68 VKP', '£88.29'),
  ('J044', 'G98-K', '19-Jan-20', '21-Jan-20', 'GE15 KWE', '£102.88'),
  ('J029', 'G61-E', '11-Jan-20', '19-Jan-20', 'FS63 RXI', '£94.82'),
  ('J024', 'G61-E', '07-Jan-20', '12-Jan-20', 'FO66 VMG', '£294.71'),
  ('J056', 'G61-E', '21-Jan-20', '23-Jan-20', 'FO66 VMG', '£378.13'),
  ('J061', 'G61-E', '27-Jan-20', '28-Jan-20', 'FN12 BXW', '£274.69'),
  ('J014', 'G59-G', '06-Jan-20', '12-Jan-20', 'DE17 ENG', '£162.60'),
  ('J031', 'G61-E', '13-Jan-20', '18-Jan-20', 'CR10 WQI', '£114.68'),
  ('J009', 'G98-K', '02-Jan-20', '11-Jan-20', 'CN61 XXH', '£50.10'),
  ('J012', 'G98-K', '09-Jan-20', '19-Jan-20', 'C4LI 23', 64.50),
  ('J064', 'G98-K', '27-Jan-20', '29-Jan-20', 'C4LI 23', 202.77),
  ('J026', 'G61-E', '08-Jan-20', '13-Jan-20', 'BP67 COO', 70.45),
  ('J058', 'G72-S', '22-Jan-20', '25-Jan-20', 'BM18 TWY', 127.80),
  ('J048', 'G59-G', '13-Jan-20', '19-Jan-20', 'BD62 EWT', 220.38),
  ('J069', 'G59-G', '12-Jan-20', '15-Jan-20', 'AR16 WJY', 23.20),
  ('J008', 'G72-S', '04-Jan-20', '21-Jan-20', 'AF66 XFP', 168.20),
  ('J051', 'G61-E', '21-Jan-20', '28-Jan-20', '83 5TU4RT', 250.32),
  ('J052', 'G61-E', '14-Jan-20', '16-Jan-20', '83 5TU4RT', 309.46),
  ('J010', 'G59-G', '02-Jan-20', '12-Jan-20', '50 J4C08', 77.14),
  ('J043', 'G59-G', '26-Jan-20', '29-Jan-20', '50 J4C08', 90.90),
  ('J047', 'G59-G', '14-Jan-20', '20-Jan-20', '50 J4C08', 60.00);
