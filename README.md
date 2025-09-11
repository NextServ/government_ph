### Government PH

An ERPNext Localization for Philippine Government/LGU

## Getting Started (Development/Demo Setup)

### Docker

You need Docker, docker-compose and git setup on your machine. Refer [Docker documentation](https://docs.docker.com/).

#### ⚠️ Note for Windows Users

After installing or setting up Git, run the following command to prevent issues where script files get converted to **CRLF** instead of **LF** (which can break shell scripts):

```bash
git config --global core.autocrlf false
```

After that, run the following commands:

```bash
git clone https://github.com/NextServ/government_ph
```

```bash
cd government_ph/docker
```

```bash
docker-compose up
```

Wait for some time (usually around 10-20 mins. depending on your computer machine) until the setup script creates a site or you're seeing the Debugger PIN text. After that you can access `http://localhost:8000` in your browser and the login screen should show up.

Use the following credentials to log in:

- Username: `Administrator`
- Password: `admin`

## Updating the App

If you already have the app running and want to pull the latest changes, follow these steps.

In the same folder where your `docker-compose.yml` is located, open a terminal and run:

```bash
docker-compose exec frappe bash
```

```bash
cd frappe-bench
```

```bash
bench update
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/government_ph
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
