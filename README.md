# Hexagonal Architecture with Flask and Dependency Injection

## This project is based on the medium article:
[Nest JS -Clean code using Hexagonal Architecture](https://towardsdev.com/nest-js-clean-code-using-hexagonal-architecture-3442a37a6e8e)

But I have translated the **TypeScript** code to the **Python** - this should ease the pain of understanding Hexagonal Architecture, while reading this article.

### About the project from medium article

The project is a dummy Ticket system:

* You can create a Ticket with description and priority
* And you can retrieve all tickets

> We are not using real database and persistence. The Repository here is just plain InMemory.

![](https://miro.medium.com/max/720/1*F9D76gA1FJNH504TcEWG_A.png)

### About project dependencies

The project has 2 main dependencies:

[Dependency Injector](https://github.com/ets-labs/python-dependency-injector)

[Flask](https://github.com/pallets/flask)

### About Hexagonal Architecture

You can read it from original author:

[The Pattern: Ports and Adapters](https://alistair.cockburn.us/hexagonal-architecture/)

### How to run

* Create virtualenv:

```
virtualenv venv
source venv/bin/activate
```

* Install requirements:
```
pip install -r requirements.txt
```

* Run the application:

From the project directory:

```
export FLASK_APP=src.adapters.api.application
export FLASK_ENV=development
flask run
```

List the tickets:

`http://127.0.0.1:5000/tickets`

```json
[
  {
    "created_at": "Sun, 25 Sep 2022 20:00:38 GMT",
    "description": "awesome",
    "id_": "1722d89e-6146-4ca5-bd7f-33c25e14f2ec",
    "priority": 1,
    "status": "OPEN",
    "updated_at": "Sun, 25 Sep 2022 20:00:38 GMT"
  },
  {
    "created_at": "Sun, 25 Sep 2022 20:00:40 GMT",
    "description": "awesome",
    "id_": "db571e71-d976-4d57-81bb-40c953d4440c",
    "priority": 1,
    "status": "OPEN",
    "updated_at": "Sun, 25 Sep 2022 20:00:40 GMT"
  },
  {
    "created_at": "Sun, 25 Sep 2022 20:00:45 GMT",
    "description": "awesome",
    "id_": "427d46ca-2b7b-40b8-8390-56552a4d16f2",
    "priority": 1,
    "status": "OPEN",
    "updated_at": "Sun, 25 Sep 2022 20:00:45 GMT"
  }
]
```

Create the ticket:

cURL example:

```
curl -X POST --location "http://127.0.0.1:5000/tickets" \
    -H "Content-Type: application/json" \
    -d "{
          \"description\": \"awesome\",
          \"priority\": 1
        }"
```

Response:

```json
{
  "created_at": "Sun, 25 Sep 2022 20:00:45 GMT",
  "description": "awesome",
  "id_": "427d46ca-2b7b-40b8-8390-56552a4d16f2",
  "priority": 1,
  "status": "OPEN",
  "updated_at": "Sun, 25 Sep 2022 20:00:45 GMT"
}
```

### Running tests
Currently covered 100%

`pytest -svv tests --cov=src --cov-report=html`
