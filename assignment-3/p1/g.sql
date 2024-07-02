-- Write a DELETE statement on Broker that fails because the broker
-- being deleted is managing somebody else.
DELETE from Broker where pid = 4004004000;