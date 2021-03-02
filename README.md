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

### 1. create

---

### - <ins>pizza > create</ins>

<span style="background-color: #337ab7; display: inline; padding: .2em .6em .3em; line-height: 1; color: #fff; text-align: center; white-space: nowrap; border-radius: .25em;">POST</span> `/api/create/pizza/`

| Parameter  | Description |
| ------------- | ------------- |
| `pizza_type` **(required)** | Type of pizza (*i.e.* regular or square)  |
| `pizza_size` **(required)** | Size of pizza (*e.g.* small, medium, large, etc.)  |
| `topping` **(required)**    | Topping on the pizza (*e.g.* tomato, onion, cheese, corn, etc.)|





### - <ins>topping > create</ins>

<span style="background-color: #337ab7; display: inline; padding: .2em .6em .3em; line-height: 1; color: #fff; text-align: center; white-space: nowrap; border-radius: .25em;">POST</span> `/api/create/topping/`

| Parameter  | Description |
| ------------- | ------------- |
| `topping` **(required)**    | Topping on the pizza (*e.g.* tomato, onion, cheese, corn, etc.)|

**Example**
```shell
curl -v -H "Content-Type: application/json" -X POST -d '{"topping":"Mushroom"}' http://127.0.0.1:8000/api/create/topping/
```