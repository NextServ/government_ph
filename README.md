### Government PH

An ERPNext Localization for Philippine Government/LGU

### Installation

### Via Windows Docker

### Via Linux Docker

You need Docker, docker-compose and git setup on your machine. Refer [Docker documentation](https://docs.docker.com/). After that, follow below steps:

**Step 1**: Setup folder and download the required files

    mkdir government_ph
    cd government_ph

    # Download the docker-compose file
    wget -O docker-compose.yml https://raw.githubusercontent.com/NextServ/government_ph/main/docker/docker-compose.yml

    # Download the setup script
    wget -O init.sh https://raw.githubusercontent.com/NextServ/government_ph/main/docker/init.sh

**Step 2**: Run the container and daemonize it

    docker compose up -d

**Step 3**: The site [http://government_ph.localhost:8000/](http://localhost:8000) should now be available. The default credentials are:

-   Username: Administrator
-   Password: admin
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
