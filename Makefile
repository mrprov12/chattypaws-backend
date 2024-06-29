.PHONY: build_dev build_test build_prod build_image_processing update_requirements all test_image_processing test_app test_db

# SETUP
# Update the other requirements.txt files without the local package references, then update the root requirements.txt
update_requirements:
	@root_dir=$$(git rev-parse --show-toplevel); \
	for req_file in $$(find . -name 'requirements.txt' -not -path "$$root_dir/requirements.txt"); do \
		echo "Processing: $$req_file"; \
		dir=$$(dirname $$req_file); \
		echo "Activating virtual environment at: $$root_dir/env/bin/activate"; \
		source $$root_dir/env/bin/activate && \
		echo "Virtual environment activated"; \
		pip3 freeze | grep -v "$$dir" > $$req_file; \
		echo "Updated: $$req_file"; \
	done; \
	echo "Updating root requirements.txt"; \
	cd $$root_dir && \
	source $$root_dir/env/bin/activate && \
	pip3 freeze | grep -v "$$root_dir" > $$root_dir/requirements.txt; \
	echo "Updated: $$root_dir/requirements.txt";

# BUILD SCRIPTS
build_dev: update_requirements
	docker-compose -f docker-compose.yml -f docker-compose.override.dev.yml up --build

build_test: update_requirements
	docker-compose -f docker-compose.yml -f docker-compose.override.test.yml up --build

build_prod: update_requirements
	docker-compose -f docker-compose.yml -f docker-compose.override.prod.yml up --build


# TESTS
# Default target to run all tests
tests: test_image_processing test_app test_db

# Target to run image_processing tests
test_image_processing:
	@echo "Running image_processing tests..."
	@python -m unittest src/tests/test_image_processing.py

# Target to run app tests
test_app:
	@echo "Running app tests..."
	@python -m unittest src/tests/test_app.py

# Target to run db tests
test_db:
	@echo "Running db tests..."
	@python -m unittest src/tests/test_db.py


# DATABASE
# Initialize the database schema
init_db:
	psql -h $(DB_HOST) -p $(DB_PORT) -d $(DB_NAME) -U $(DB_USER) -f src/db/db_schema.sql

# Reset the database with current schema (drop, create, import)
reset_db:
	./scripts/reset_db.sh