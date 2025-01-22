.PHONY: clean sdist upload pre-commit mkdocs

sdist: clean
	python3 setup.py sdist bdist_wheel --universa

upload: clean
	python3 setup.py upload

clean:
	rm -rf build dailycheckin.egg-info dist

pre-commit:
	pre-commit run --all-files
