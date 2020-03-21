SRC_DIR := tmp/build

V := . .venv/bin/activate

clean:
	-rm -rf $(SRC_DIR)/

venv: clean
	virtualenv -p python3.6 .venv
	$(V); pip install -r requirements.txt

run:
	python3 src/derp_based_wars.py
