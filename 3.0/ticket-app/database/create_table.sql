-- 用户表
CREATE TABLE Users (
    UserID BIGINT PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(255),
    RealName VARCHAR(255),
    Gender VARCHAR(10),
    IDCard VARCHAR(20),
    Email VARCHAR(255),
    Address VARCHAR(255),
    Account VARCHAR(255),
    Password VARCHAR(255)
);

-- 管理员表
CREATE TABLE Administrators (
    AdminID BIGINT PRIMARY KEY AUTO_INCREMENT,
    AdminType VARCHAR(20), -- 剧院管理员或系统管理员
    Account VARCHAR(255),
    Password VARCHAR(255),
    Permissions VARCHAR(255)
);

-- 功能表
CREATE TABLE AdminFunctions (
    FunctionID BIGINT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255),
    Permissions VARCHAR(255)
);

-- 演出表
CREATE TABLE Shows (
    ShowID BIGINT PRIMARY KEY AUTO_INCREMENT,
    TheaterID BIGINT, -- 外键，关联剧院
    ShowName VARCHAR(255),
    Description TEXT,
    ShowDate DATE,
    Duration BIGINT,
    AdminID BIGINT, -- 外键，关联管理员
    Image VARCHAR(255),
    Category VARCHAR(255),
    City VARCHAR(255)
);

-- 剧院表
CREATE TABLE Theaters (
    TheaterID BIGINT PRIMARY KEY AUTO_INCREMENT,
    TheaterName VARCHAR(255),
    Address VARCHAR(255),
    Capacity BIGINT,
    AdminID BIGINT -- 外键，关联管理员
);

-- 票价管理表
CREATE TABLE TicketPrices (
    TicketID BIGINT PRIMARY KEY AUTO_INCREMENT,
    ShowID BIGINT, -- 外键，关联演出
    Price DECIMAL(10, 2),
    Category VARCHAR(255),
    TotalQuantity BIGINT,
    RemainingQuantity BIGINT
);

-- 订单表
CREATE TABLE Orders (
    OrderID BIGINT PRIMARY KEY AUTO_INCREMENT,
    UserID BIGINT, -- 外键，关联用户
    TicketID BIGINT, -- 外键，关联票价管理
    PurchaseTime TIMESTAMP,
    OrderStatus VARCHAR(20),
    Quantity BIGINT
);

-- 退票表
CREATE TABLE Refunds (
    RefundID BIGINT PRIMARY KEY AUTO_INCREMENT,
    UserID BIGINT, -- 外键，关联用户
    AdminID BIGINT, -- 外键，关联管理员
    RefundTime TIMESTAMP,
    RefundReason TEXT,
    TicketStatus VARCHAR(20),
    OrderID BIGINT -- 外键，关联订单
);
