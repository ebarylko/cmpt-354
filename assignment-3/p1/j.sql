-- Write an INSERT statement that fails for violating (c)
INSERT into Trade Values (100, 0, 'buy', '2024-01-31 13:00:00', 'AAPL', 6.00, 143.68);
INSERT into Trade Values (100, 4, 'buy', '2021-01-31 13:00:00', 'AAPL', 6.00, 143.68);

