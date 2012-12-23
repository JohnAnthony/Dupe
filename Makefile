install:
	cp dupe.py /usr/bin/dupe
	chmod +x /usr/bin/dupe
	cp dupe.1 /usr/share/man/man1/

uninstall:
	rm /usr/bin/dupe
	rm /usr/share/man/man1/dupe.1
