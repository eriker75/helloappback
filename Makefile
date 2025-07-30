# Archivos docker-compose
DOCKER_DIR=docker
COMPOSE_SERVICES_FILE=$(DOCKER_DIR)/docker-compose.services.yml
COMPOSE_DEV_FILE=$(DOCKER_DIR)/docker-compose.dev.yml
COMPOSE_PROD_FILE=$(DOCKER_DIR)/docker-compose.prod.yml

# Nombre del proyecto para docker-compose
PROJECT_NAME=helloback

# Comandos solo para servicios (db, redis, pgadmin)
up-services:
	@echo "Levantando solo los servicios (db, redis, pgadmin)..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -p $(PROJECT_NAME)_services up -d

down-services:
	@echo "Bajando solo los servicios (db, redis, pgadmin)..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -p $(PROJECT_NAME)_services down

logs-services:
	@echo "Mostrando logs de los servicios (db, redis, pgadmin)..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -p $(PROJECT_NAME)_services logs -f

restart-services:
	@echo "Reiniciando los servicios (db, redis, pgadmin)..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -p $(PROJECT_NAME)_services restart

clean-services:
	@echo "Limpiando los servicios y volúmenes..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -p $(PROJECT_NAME)_services down --volumes

destroy-services:
	@echo "Destruyendo los servicios, volúmenes e imágenes..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -p $(PROJECT_NAME)_services down --volumes --rmi all

# Comandos de desarrollo
up-dev:
	@echo "Levantando los contenedores en modo desarrollo..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_DEV_FILE) -p $(PROJECT_NAME)_dev up -d --build

down-dev:
	@echo "Bajando los contenedores en modo desarrollo..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_DEV_FILE) -p $(PROJECT_NAME)_dev down

logs-dev:
	@echo "Mostrando logs de los contenedores en modo desarrollo..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_DEV_FILE) -p $(PROJECT_NAME)_dev logs -f

restart-dev:
	@echo "Reiniciando los contenedores en modo desarrollo..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_DEV_FILE) -p $(PROJECT_NAME)_dev restart

build-dev:
	@echo "Construyendo las imágenes en modo desarrollo..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_DEV_FILE) -p $(PROJECT_NAME)_dev build

clean-dev:
	@echo "Limpiando los contenedores en modo desarrollo..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_DEV_FILE) -p $(PROJECT_NAME)_dev down --volumes

destroy-dev:
	@echo "Destruyendo los contenedores en modo desarrollo..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_DEV_FILE) -p $(PROJECT_NAME)_dev down --volumes --rmi all

# Comandos de producción
up:
	@echo "Levantando los contenedores en modo producción..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_PROD_FILE) -p $(PROJECT_NAME)_prod up -d --build

down:
	@echo "Bajando los contenedores en modo producción..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_PROD_FILE) -p $(PROJECT_NAME)_prod down

logs:
	@echo "Mostrando logs de los contenedores en modo producción..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_PROD_FILE) -p $(PROJECT_NAME)_prod logs -f

restart:
	@echo "Reiniciando los contenedores en modo producción..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_PROD_FILE) -p $(PROJECT_NAME)_prod restart

build:
	@echo "Construyendo las imágenes en modo producción..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_PROD_FILE) -p $(PROJECT_NAME)_prod build

clean:
	@echo "Limpiando los contenedores en modo producción..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_PROD_FILE) -p $(PROJECT_NAME)_prod down --volumes

destroy:
	@echo "Destruyendo los contenedores en modo producción..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_PROD_FILE) -p $(PROJECT_NAME)_prod down --volumes --rmi all

# Comandos útiles
migrate-dev:
	@echo "Aplicando migraciones Django (dev)..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_DEV_FILE) -p $(PROJECT_NAME)_dev exec web python manage.py migrate

createsuperuser-dev:
	@echo "Creando superusuario Django (dev)..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_DEV_FILE) -p $(PROJECT_NAME)_dev exec web python manage.py createsuperuser

shell-dev:
	@echo "Abriendo shell Django (dev)..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_DEV_FILE) -p $(PROJECT_NAME)_dev exec web python manage.py shell

migrate:
	@echo "Aplicando migraciones Django (prod)..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_PROD_FILE) -p $(PROJECT_NAME)_prod exec web python manage.py migrate

createsuperuser:
	@echo "Creando superusuario Django (prod)..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_PROD_FILE) -p $(PROJECT_NAME)_prod exec web python manage.py createsuperuser

shell:
	@echo "Abriendo shell Django (prod)..."
	docker-compose -f $(COMPOSE_SERVICES_FILE) -f $(COMPOSE_PROD_FILE) -p $(PROJECT_NAME)_prod exec web python manage.py shell

.PHONY: help
help:
	@echo "Uso del Makefile:"
	@echo "  up-services         - Levantar solo los servicios (db, redis, pgadmin)"
	@echo "  down-services       - Bajar solo los servicios"
	@echo "  logs-services       - Mostrar logs de los servicios"
	@echo "  restart-services    - Reiniciar los servicios"
	@echo "  clean-services      - Limpiar los servicios y volúmenes"
	@echo "  destroy-services    - Destruir los servicios, volúmenes e imágenes"
	@echo "  up-dev              - Levantar los contenedores en modo desarrollo"
	@echo "  down-dev            - Bajar los contenedores en modo desarrollo"
	@echo "  logs-dev            - Mostrar los logs en modo desarrollo"
	@echo "  restart-dev         - Reiniciar los contenedores en modo desarrollo"
	@echo "  build-dev           - Construir las imágenes en modo desarrollo"
	@echo "  clean-dev           - Limpiar los contenedores en modo desarrollo"
	@echo "  destroy-dev         - Destruye los contenedores en modo desarrollo"
	@echo "  migrate-dev         - Aplicar migraciones Django en desarrollo"
	@echo "  createsuperuser-dev - Crear superusuario Django en desarrollo"
	@echo "  shell-dev           - Abrir shell Django en desarrollo"
	@echo "  up                  - Levantar los contenedores en modo producción"
	@echo "  down                - Bajar los contenedores en modo producción"
	@echo "  logs                - Mostrar los logs en modo producción"
	@echo "  restart             - Reiniciar los contenedores en modo producción"
	@echo "  build               - Construir las imágenes en modo producción"
	@echo "  clean               - Limpiar los contenedores en modo producción"
	@echo "  destroy             - Destruye los contenedores en modo producción"
	@echo "  migrate             - Aplicar migraciones Django en producción"
	@echo "  createsuperuser     - Crear superusuario Django en producción"
	@echo "  shell               - Abrir shell Django en producción"