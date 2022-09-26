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
	@./pants dependencies --transitive apps/app1:app1_bin | grep app2

package:
	@./pants package ::
