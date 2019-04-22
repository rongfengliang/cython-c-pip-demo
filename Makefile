LIB_DIR = ext

CLI_DIR = cli

default: pyadd

pyadd: setup.py $(CLI_DIR)/app.pyx $(LIB_DIR)/libadd.a
	python3 setup.py build_ext --inplace && rm -f add_app.c && rm -Rf build && cp *.so  cli/  && rm *.so

$(LIB_DIR)/libadd.a:
	make -C $(LIB_DIR) libadd.a

clean:
	rm *.so