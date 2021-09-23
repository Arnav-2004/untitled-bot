# untitled-bot

---

## Dev Installation

Using poetry

```
poetry install

poetry run task precommit

poetry run task lint

poetry run task bot
```

Using Docker (Recommended):

```
docker-compose up --build

# use -d flag for detached mode
docker-compose up

# Use ctrl+C if not in detached mode
docker-compose stop

# Use -v or --volumes flag to remove volumes
docker-compose down
```
