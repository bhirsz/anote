
def generate_release(version, unreleased_path):
    print(f"Generating release notes for {version}")

    # load # unreleased dir (default, or passed dir)
    # inside unreleased find template.jinja, or use --template path and load it
    # get all *.rst files and load them
    # pattern is <order_number>.<section>.rst
    # ie 1.fixes.rst, 10.features.rst
    # later in template we can refer to fixes, features as list of strings (simple as it is)
    # --clear-notes to remove *.rst