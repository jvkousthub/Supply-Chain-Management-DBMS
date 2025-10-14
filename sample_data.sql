-- Sample data for testing the supply chain management system

-- Insert suppliers
INSERT INTO suppliers VALUES (supplier_seq.NEXTVAL, 'TechParts Inc', 'John Smith', 'john@techparts.com', '555-0101', '123 Tech Street', 'New York', 'USA', 4.5, SYSDATE);
INSERT INTO suppliers VALUES (supplier_seq.NEXTVAL, 'Global Electronics', 'Sarah Chen', 'sarah@globalelec.com', '555-0102', '456 Innovation Blvd', 'San Francisco', 'USA', 4.2, SYSDATE);
INSERT INTO suppliers VALUES (supplier_seq.NEXTVAL, 'Quality Components', 'Mike Johnson', 'mike@qualitycomp.com', '555-0103', '789 Industrial Ave', 'Chicago', 'USA', 3.8, SYSDATE);
INSERT INTO suppliers VALUES (supplier_seq.NEXTVAL, 'Prime Supplies Co', 'Lisa Wang', 'lisa@primesupply.com', '555-0104', '321 Trade Center', 'Seattle', 'USA', 4.7, SYSDATE);

-- Insert warehouses
INSERT INTO warehouses VALUES (warehouse_seq.NEXTVAL, 'Central Warehouse', '100 Storage Lane', 'Dallas', 50000, 'Robert Brown', '555-0201');
INSERT INTO warehouses VALUES (warehouse_seq.NEXTVAL, 'East Coast Hub', '200 Logistics Dr', 'Boston', 35000, 'Emily Davis', '555-0202');
INSERT INTO warehouses VALUES (warehouse_seq.NEXTVAL, 'West Coast Hub', '300 Distribution Way', 'Los Angeles', 40000, 'David Lee', '555-0203');

-- Insert products
INSERT INTO products VALUES (product_seq.NEXTVAL, 'Laptop Computer', 'Electronics', 1, 899.99, 'High performance laptop');
INSERT INTO products VALUES (product_seq.NEXTVAL, 'Desktop Monitor', 'Electronics', 2, 249.99, '27 inch LED monitor');
INSERT INTO products VALUES (product_seq.NEXTVAL, 'Wireless Mouse', 'Accessories', 1, 29.99, 'Ergonomic wireless mouse');
INSERT INTO products VALUES (product_seq.NEXTVAL, 'Keyboard', 'Accessories', 3, 79.99, 'Mechanical keyboard');
INSERT INTO products VALUES (product_seq.NEXTVAL, 'USB Cable', 'Cables', 4, 9.99, 'USB-C cable 6ft');
INSERT INTO products VALUES (product_seq.NEXTVAL, 'HDMI Cable', 'Cables', 4, 14.99, 'HDMI 2.0 cable');
INSERT INTO products VALUES (product_seq.NEXTVAL, 'Webcam', 'Electronics', 2, 89.99, 'HD webcam with microphone');
INSERT INTO products VALUES (product_seq.NEXTVAL, 'Headphones', 'Accessories', 3, 149.99, 'Noise cancelling headphones');
INSERT INTO products VALUES (product_seq.NEXTVAL, 'Power Adapter', 'Accessories', 1, 39.99, 'Universal power adapter');
INSERT INTO products VALUES (product_seq.NEXTVAL, 'External SSD', 'Storage', 2, 129.99, '1TB external SSD');

-- Insert inventory
INSERT INTO inventory VALUES (inventory_seq.NEXTVAL, 1, 1, 45, 10, SYSDATE);
INSERT INTO inventory VALUES (inventory_seq.NEXTVAL, 2, 1, 78, 15, SYSDATE);
INSERT INTO inventory VALUES (inventory_seq.NEXTVAL, 3, 1, 150, 30, SYSDATE);
INSERT INTO inventory VALUES (inventory_seq.NEXTVAL, 4, 2, 92, 20, SYSDATE);
INSERT INTO inventory VALUES (inventory_seq.NEXTVAL, 5, 2, 8, 25, SYSDATE);
INSERT INTO inventory VALUES (inventory_seq.NEXTVAL, 6, 3, 120, 20, SYSDATE);
INSERT INTO inventory VALUES (inventory_seq.NEXTVAL, 7, 1, 34, 15, SYSDATE);
INSERT INTO inventory VALUES (inventory_seq.NEXTVAL, 8, 2, 56, 10, SYSDATE);
INSERT INTO inventory VALUES (inventory_seq.NEXTVAL, 9, 3, 88, 20, SYSDATE);
INSERT INTO inventory VALUES (inventory_seq.NEXTVAL, 10, 1, 6, 15, SYSDATE);

-- Insert orders
INSERT INTO orders VALUES (order_seq.NEXTVAL, 1, 1, TO_DATE('2025-10-01', 'YYYY-MM-DD'), 'DELIVERED', 5400.00, TO_DATE('2025-10-08', 'YYYY-MM-DD'));
INSERT INTO orders VALUES (order_seq.NEXTVAL, 2, 2, TO_DATE('2025-10-05', 'YYYY-MM-DD'), 'SHIPPED', 3200.00, TO_DATE('2025-10-15', 'YYYY-MM-DD'));
INSERT INTO orders VALUES (order_seq.NEXTVAL, 4, 1, TO_DATE('2025-10-10', 'YYYY-MM-DD'), 'CONFIRMED', 1500.00, TO_DATE('2025-10-20', 'YYYY-MM-DD'));
INSERT INTO orders VALUES (order_seq.NEXTVAL, 3, 3, TO_DATE('2025-10-12', 'YYYY-MM-DD'), 'PENDING', 2100.00, NULL);

-- Insert order details
INSERT INTO order_details VALUES (detail_seq.NEXTVAL, 1, 1, 6, 899.99, 5399.94);
INSERT INTO order_details VALUES (detail_seq.NEXTVAL, 2, 2, 10, 249.99, 2499.90);
INSERT INTO order_details VALUES (detail_seq.NEXTVAL, 2, 7, 8, 89.99, 719.92);
INSERT INTO order_details VALUES (detail_seq.NEXTVAL, 3, 5, 50, 9.99, 499.50);
INSERT INTO order_details VALUES (detail_seq.NEXTVAL, 3, 6, 40, 14.99, 599.60);
INSERT INTO order_details VALUES (detail_seq.NEXTVAL, 3, 9, 10, 39.99, 399.90);
INSERT INTO order_details VALUES (detail_seq.NEXTVAL, 4, 4, 15, 79.99, 1199.85);
INSERT INTO order_details VALUES (detail_seq.NEXTVAL, 4, 8, 6, 149.99, 899.94);

-- Insert shipments
INSERT INTO shipments VALUES (shipment_seq.NEXTVAL, 1, 'FedEx', 'FX123456789', TO_DATE('2025-10-02', 'YYYY-MM-DD'), TO_DATE('2025-10-08', 'YYYY-MM-DD'), 'DELIVERED');
INSERT INTO shipments VALUES (shipment_seq.NEXTVAL, 2, 'UPS', 'UP987654321', TO_DATE('2025-10-06', 'YYYY-MM-DD'), NULL, 'IN_TRANSIT');
INSERT INTO shipments VALUES (shipment_seq.NEXTVAL, 3, 'DHL', 'DH456789123', TO_DATE('2025-10-11', 'YYYY-MM-DD'), NULL, 'PREPARING');

COMMIT;
