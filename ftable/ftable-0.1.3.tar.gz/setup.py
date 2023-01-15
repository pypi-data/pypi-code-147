
from setuptools import setup
# 公開用パッケージの作成 [ezpip]
import ezpip

# 公開用パッケージの作成 [ezpip]
with ezpip.packager(develop_dir = "./_develop_ftable/") as p:
	setup(
		name = "ftable",
		version = "0.1.3",
		description = "A table that has had its filter/search function optimized for speed.",
		author = "bib_inf",
		author_email = "contact.bibinf@gmail.com",
		url = "https://github.co.jp/",
		packages = p.packages,
		install_requires = ["ezpip", "sout>=1.2.1", "tqdm"],
		long_description = p.long_description,
		long_description_content_type = "text/markdown",
		license = "CC0 v1.0",
		classifiers = [
			"Programming Language :: Python :: 3",
			"License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
		],
	)
