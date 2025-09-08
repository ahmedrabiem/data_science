-- create schemas
CREATE SCHEMA production;
CREATE SCHEMA sales;

-- create tables for production
CREATE TABLE production.categories(
	category_id SERIAL PRIMARY KEY,
	category_name VARCHAR(255) not null
);

CREATE TABLE production.brands(
	brand_id SERIAL PRIMARY KEY,
	brand_name VARCHAR(255) not null
);

CREATE TABLE production.products(
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(255) NOT NULL UNIQUE,
	list_price DECIMAL NOT NULL,
	model_year SMALLINT NOT NULL,
	brand_id INT NOT NULL,
	category_id INT NOT NULL,
	FOREIGN KEY (brand_id) REFERENCES production.brands (brand_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (category_id) REFERENCES production.categories (category_id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- create tables for production sales
CREATE TABLE sales.customers(
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	phone VARCHAR(50),
	email VARCHAR(255) UNIQUE,
	street VARCHAR(255),
	city VARCHAR(100),
	zip_code VARCHAR(255) ,
	state VARCHAR(50)
);

CREATE TABLE sales.stores(
	store_id SERIAL PRIMARY KEY,
	store_name VARCHAR(255) NOT NULL,
	phone VARCHAR(50),
	email VARCHAR(60) UNIQUE,
	street VARCHAR(60),
	city VARCHAR(60),
	state VARCHAR(40),
	zip_code VARCHAR(10)
);

CREATE TABLE sales.staffs(
	staff_id SERIAL PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	phone VARCHAR(50)NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	active SMALLINT NOT NULL,
	store_id INT NOT NULL,
	maneger_id INT,
	FOREIGN KEY (store_id) REFERENCES sales.stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (maneger_id) REFERENCES sales.staffs (staff_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE sales.orders(
	order_id SERIAL PRIMARY KEY,
	customer_id INT NOT NULL,
	order_status VARCHAR(50) NOT NULL,
	order_date DATE NOT NULL,
	shipped_date DATE NOT NULL,
	required_date DATE NOT NULL,
	store_id INT NOT NULL,
	staff_id INT NOT NULL,
	FOREIGN KEY (store_id) REFERENCES sales.stores (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (customer_id) REFERENCES sales.customers (customer_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (staff_id) REFERENCES sales.staffs (staff_id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE sales.order_items(
	order_id INT,
	item_id INT,
	product_id INT NOT NULL,
	quantity INT NOT NULL,
	list_price DECIMAL (10,2) NOT NULL,
	discount DECIMAL (4,2) NOT NULL,
	PRIMARY KEY (order_id, item_id),
	FOREIGN KEY (order_id) REFERENCES sales.orders (order_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (product_id) REFERENCES production.products (product_id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE production.stocks(
	store_id INT,
	product_id INT,
	PRIMARY KEY (store_id, product_id),
	FOREIGN KEY (store_id) REFERENCES sales.stores(store_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (product_id) REFERENCES production.products (product_id) ON DELETE CASCADE ON UPDATE CASCADE
);






