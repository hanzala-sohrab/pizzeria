# pizzeria

## Steps to run a local server

1. Install the required modules
   ```shell
    pip install -r requirements.txt
    ```
2. Make migrations
    ```shell
    python manage.py makemigrations pizza
    ```
3. Apply migrations
    ```shell
    python manage.py migrate
    ```
4. Run server
    ```shell
    python manage.py runserver
    ```
5. Go to http://127.0.0.1:8000/docs for testing the APIs.


## API Info

1. **create**
    <details><summary><ins>pizza > create</ins></summary>
    
    - POST `/api/create/pizza/`
    
        | Parameter  | Description |
        | ------------- | ------------- |
        | `pizza_type` **(required)** | Type of pizza (*i.e.* regular or square)  |
        | `pizza_size` **(required)** | Size of pizza (*e.g.* small, medium, large, etc.)  |
        | `topping` **(required)**    | Topping on the pizza (*e.g.* tomato, onion, cheese, corn, etc.)|
    
    - **Example**
        ```shell
        # Load the schema document
        coreapi get http://127.0.0.1:8000/docs/
        
        # Interact with the API endpoint
        coreapi action create pizza create -p pizza_type="Regular" -p pizza_size="Large" -p topping='["Tomato","Cheese"]'
        ```
    
    - **Result**
        ```json
        {
            "id": 5,
            "pizza_type": "Regular",
            "pizza_size": "Large",
            "topping": [
            "Cheese",
            "Tomato"
            ]
        }
        ```
    </details>

    <details><summary><ins>topping > create</ins></summary>
    
    - POST `/api/create/topping/`
    
        | Parameter  | Description |
        | ------------- | ------------- |
        | `topping` **(required)**    | Topping on the pizza (*e.g.* tomato, onion, cheese, corn, etc.)|
        
    - **Example**
        ```shell
        # Load the schema document
        coreapi get http://127.0.0.1:8000/docs/
        
        # Interact with the API endpoint
        coreapi action create topping create -p topping="Mushroom"
        ```
    - **Result**
        ```json
        {
            "topping": "Mushroom"
        }
        ```
    
    </details>

2. **list**
    <details><summary><ins>show pizza with given id</ins></summary>
    
    - GET `/api/list/{id}/`
    
        | Parameter  | Description |
        | ------------- | ------------- |
        | `id` **(required)** | Pizza ID  |
    
    - **Example**
        ```json

        ```
    
    - **Result**
        ```json

        ```
    </details>

    <details><summary><ins>show all pizzas of given size</ins></summary>
    
    - GET `/api/list/{size}/`
    
        | Parameter  | Description |
        | ------------- | ------------- |
        | `size` **(required)**    | Size of pizza |
    
    - **Example**
    ```shell
    # Load the schema document
    coreapi get http://127.0.0.1:8000/docs/
    
    # Interact with the API endpoint
    coreapi action list read_0 -p type="Regular"
    ```
    - <details><summary>Result</summary>
      
        ```json
        [
            {
                "id": 2,
                "pizza_type": "Regular",
                "pizza_size": "Extra large",
                "topping": [
                    "Onion"
                ]
            },
            {
                "id": 3,
                "pizza_type": "Regular",
                "pizza_size": "Large",
                "topping": [
                    "Onion",
                    "Tomato"
                ]
            }
        ]
        ```
    </details>
    </details>

    <details><summary><ins>show all pizzas of given type</ins></summary>
    
    - GET `/api/list/{type}/`
    
        | Parameter  | Description |
        | ------------- | ------------- |
        | `type` **(required)**    | Size of pizza |
    
    - **Example**
        ```shell
        # Load the schema document
        coreapi get http://127.0.0.1:8000/docs/
        
        # Interact with the API endpoint
        coreapi action list read_0 -p type="Regular"
        ```
    - <details>
        <summary>Result</summary>
    
        ```json
        [
            {
                "id": 2,
                "pizza_type": "Regular",
                "pizza_size": "Extra large",
                "topping": [
                    "Onion"
                ]
            },
            {
                "id": 3,
                "pizza_type": "Regular",
                "pizza_size": "Large",
                "topping": [
                    "Onion",
                    "Tomato"
                ]
            }
        ]
        ```
    </details>
    </details>