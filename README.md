# untitled-bot

---

## Dev Installation

1. Clone the repository:

- `git clone https://github.com/Arnav-2004/untitled-bot.git` or `git clone git@github.com:Arnav-2004/untitled-bot.git`

- Github CLI: `gh repo clone Arnav-2004/untitled-bot`

2. `cd untitled-bot/` and create a new branch: `git checkout -b <name of your new local branch> main` or `git switch -c <name of your new local branch> main`

3. Using poetry

Install poetry: `pip install -U poetry`

```sh
# Install the project and development dependencies
poetry install

# Install the pre-commit hooks
poetry run task precommit

poetry run task lint

# Run the source code
poetry run task bot
```

4. Using Docker (Recommended):

Install Docker: Follow the [official documentation](https://docs.docker.com/get-docker/)

Install docker-compose: `pip install -U docker-compose`

```sh
# Make sure docker service is running before executing the following command.
docker-compose up --build

# use -d flag for detached mode
docker-compose up

# Use Ctrl+C if not in detached mode
docker-compose stop

# Use -v or --volumes flag to remove volumes
docker-compose down
```

5. Lint and format your code using `poetry run task lint` and push the changes `git push -u origin <name of your remote branch>`
