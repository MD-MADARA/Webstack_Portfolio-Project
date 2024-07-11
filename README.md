# Project: Api for fashion-alx store

## Description
fashion-alx api is an API for an online clothing store, providing comprehensive functionalities to manage products, users, carts, orders, and more.

## Installation Instructions
To set up and run the API locally, follow these steps:
1. Install dependencies:
   ```bash
   pip install flask sqlalchemy flask_sqlalchemy flask_swagger_ui faker mysqlclient

2. Clone the repository:
    ```bash
    git clone https://github.com/MD-MADARA/Webstack_Portfolio-Project.git
    cd Webstack_Portfolio-Project

3. Run the API using provided script:
    ```bash
    ./run

This script runs the API on port 5001.


## API Endpoints

### Products
- **GET /api/products**
  - **Description:** Retrieve a list of all products or filter based on specific criteria like category, price range, and sorting options.
  - **Parameters:**
    - `category_name` (optional): Filter products by category name.
    - `category_type` (optional): Filter products by category type.
    - `min_price` (optional): Minimum price threshold for products.
    - `max_price` (optional): Maximum price threshold for products.
    - `limit` (optional): Limit the number of products returned.
    - `asc_order_by` (optional): Sort products in ascending order by a specified attribute.
    - `desc_order_by` (optional): Sort products in descending order by a specified attribute.
    - `from` (optional): Start index for pagination.
    - `ignore` (optional): Ignore a product by its ID.

- **GET /api/products/{product_id}**
  - **Description:** Retrieve details of a specific product by its ID.

- **POST /api/products**
  - **Description:** Create a new product.
  - **Parameters:** 
    - `title`, `price`, `description`, `category_name`, `category_type` (required): Product details.

- **PUT /api/products/{product_id}**
  - **Description:** Update details of a specific product by its ID.
  - **Parameters:** 
    - `title`, `price`, `description`, `category_name`, `category_type`, `image_path` (optional): Updated product details.

- **DELETE /api/products/{product_id}**
  - **Description:** Delete a product by its ID.

### Users
- **GET /api/users**
  - **Description:** Retrieve a list of all users or filter by email and limit results.
  - **Parameters:**
    - `limit` (optional): Limit the number of users returned.
    - `email` (optional): Filter users by email.

- **GET /api/users/{user_id}**
  - **Description:** Retrieve details of a specific user by their ID.

- **POST /api/users**
  - **Description:** Create a new user.
  - **Parameters:** 
    - `email`, `password`, `first_name`, `last_name`, `address`, `phone` (required): User details.

- **PUT /api/users/{user_id}**
  - **Description:** Update details of a specific user by their ID.
  - **Parameters:** 
    - `first_name`, `last_name`, `address`, `phone`, `password` (optional): Updated user details.

- **DELETE /api/users/{user_id}**
  - **Description:** Delete a user by their ID.

### Carts
- **GET /api/carts/{user_id}**
  - **Description:** Retrieve the cart and its items for a specified user.

- **POST /api/carts/{user_id}**
  - **Description:** Add a product to the user's cart or update the quantity if it already exists.
  - **Parameters:** 
    - `product_id`, `quantity` (required): Product ID and quantity to add/update.

- **DELETE /api/carts/{user_id}**
  - **Description:** Remove a product from the user's cart.
  - **Parameters:** 
    - `product_id` (required): Product ID to remove.

- **PUT /api/carts/{user_id}/{product_id}**
  - **Description:** Update the quantity of a product in the user's cart or remove it if the quantity is zero.
  - **Parameters:** 
    - `product_id`, `quantity` (required): Product ID and quantity to update.

### Orders
- **GET /api/orders/{user_id}**
  - **Description:** Retrieve orders for a specified user or all orders if no user ID is provided.

- **POST /api/orders/{user_id}**
  - **Description:** Create a new order for a given user and transfer cart items to the order.
  - **Parameters:** 
    - `total_price` (required): Total price of the order.

### API Documentation
Explore and interact with the API using Swagger UI at http://fashion-alx.me/apidocs
or http://localhost:5001/api/docs after running the API.

### Contact Information
* Author: Mouad Khanouch
* Email: mouadmouadkhanouch@gmail.com
