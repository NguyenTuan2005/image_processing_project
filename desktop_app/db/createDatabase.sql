CREATE TABLE [cameras] (
  [id] int PRIMARY KEY IDENTITY(1, 1),
  [source_type] varchar(10),
  [rtsp_url] varchar(255),
  [file_path] varchar(255),
  [description] varchar(255),
  [created_at] datetime,
  [updated_at] datetime
)
GO

CREATE TABLE [vehicles] (
  [plate_number] varchar(20) PRIMARY KEY,
  [created_at] datetime,
  [updated_at] datetime
)
GO

CREATE TABLE [alpr_logs] (
  [id] int PRIMARY KEY IDENTITY(1, 1),
  [camera_id] int,
  [plate_number] varchar(20),
  [detected_at] datetime,
  [image_path] varchar(255)
)
GO

CREATE TABLE [monthly_cards] (
  [card_id] varchar(50) PRIMARY KEY,
  [customer_id] varchar(50),
  [price] int,
  [start_date] date,
  [end_date] date,
  [active] bit,
  [created_at] datetime,
  [updated_at] datetime
)
GO

CREATE TABLE [customers] (
  [customer_id] varchar(50) PRIMARY KEY,
  [plate_number] varchar(20),
  [card_id] varchar(20),
  [full_name] varchar(100),
  [phone_number] varchar(20),
  [email] varchar(50)
)
GO

CREATE TABLE [cards] (
  [card_id] varchar(50) PRIMARY KEY,
  [plate_number] varchar(20),
  [card_type] varchar(10),
  [entry_time] datetime,
  [exit_time] datetime,
  [fee] int,
  [created_at] datetime,
  [updated_at] datetime,
  [created_by] int,
  [closed_by] int
)
GO

CREATE TABLE [staffs] (
  [id] int PRIMARY KEY IDENTITY(1, 1),
  [username] varchar(50),
  [password] varchar(255),
  [fullname] varchar(100),
  [phone_number] varchar(20),
  [role] int,
  [created_at] datetime,
  [updated_at] datetime
)
GO

CREATE TABLE [payments] (
  [id] int PRIMARY KEY IDENTITY(1, 1),
  [card_id] varchar(50),
  [customer_id] varchar(50),
  [amount] int,
  [payment_date] datetime,
  [method] varchar(20),
  [processed_by] int
)
GO

ALTER TABLE [cards] ADD FOREIGN KEY ([created_by]) REFERENCES [staffs] ([id])
GO

ALTER TABLE [cards] ADD FOREIGN KEY ([closed_by]) REFERENCES [staffs] ([id])
GO

ALTER TABLE [payments] ADD FOREIGN KEY ([processed_by]) REFERENCES [staffs] ([id])
GO

ALTER TABLE [alpr_logs] ADD FOREIGN KEY ([camera_id]) REFERENCES [cameras] ([id])
GO

ALTER TABLE [alpr_logs] ADD FOREIGN KEY ([plate_number]) REFERENCES [vehicles] ([plate_number])
GO

ALTER TABLE [customers] ADD FOREIGN KEY ([plate_number]) REFERENCES [vehicles] ([plate_number])
GO

ALTER TABLE [monthly_cards] ADD FOREIGN KEY ([customer_id]) REFERENCES [customers] ([customer_id])
GO

ALTER TABLE [cards] ADD FOREIGN KEY ([plate_number]) REFERENCES [vehicles] ([plate_number])
GO

ALTER TABLE [payments] ADD FOREIGN KEY ([customer_id]) REFERENCES [customers] ([customer_id])
GO

ALTER TABLE [payments] ADD FOREIGN KEY ([card_id]) REFERENCES [cards] ([card_id])
GO


