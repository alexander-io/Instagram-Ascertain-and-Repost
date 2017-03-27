all:
	mkdir posts/
	touch post_map

clean:
	rm -rf posts/*
	rm -rf posts
	# echo "" > post_map.txt
	rm -rf post_map
	python3 drop_db.py

run:
	mkdir posts/
	touch post_map
	python3 x.py
