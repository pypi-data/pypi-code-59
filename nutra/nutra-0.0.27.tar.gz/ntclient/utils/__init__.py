def git_sha():
    """ Gets the git revision, if it exists in cwd """
    try:
        from .__sha__ import __sha__
    except Exception as e1:
        from .settings import TESTING
        if not TESTING:
            print(repr(e1))
        import subprocess

        try:
            __sha__ = (
                subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
                .decode()
                .rstrip()
            )
        except Exception as e2:
            print(repr(e2))
            __sha__ = None

    return __sha__


# Export for package level
__sha__ = git_sha()
