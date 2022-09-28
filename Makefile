count-loc:
	@./pants count-loc ::

fmt:
	@./pants fmt ::

lint:
	@./pants lint ::

test:
	@./pants test ::

check:
	@./pants check ::
	@./tools/check_app_deps.py

package:
	@./pants package ::

clean:
	@rm -rf dist/*
