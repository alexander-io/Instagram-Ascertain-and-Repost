all:
	python3 x.py
clean:

	rm -rf posts/*
	rm post_map
	touch post_map
	python3 drop_db.py
