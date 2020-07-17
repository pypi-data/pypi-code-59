import sys
import os
from json import dumps
from optparse import OptionParser
from time import sleep
from pathlib import Path
from typing import Dict, List, Any

import inquirer
from git import GitCommandError
from gitlab import GitlabMRClosedError, GitlabMRRebaseError

from mkmr.api import API
from mkmr.config import Config
from mkmr.utils import find_cache, init_repo

from . import __version__


def main():
    parser = OptionParser(version=__version__)
    parser.add_option(
        "--token", dest="token", action="store", type="string", help="GitLab Personal Access Token"
    )
    parser.add_option(
        "-c",
        "--config",
        dest="config",
        action="store",
        type="string",
        default=None,
        help="Full path to configuration file",
    )
    parser.add_option(
        "-n",
        "--dry-run",
        dest="dry_run",
        action="store_true",
        default=False,
        help="show which merge requests mgmr would try to merge",
    )
    parser.add_option(
        "--timeout",
        dest="timeout",
        action="store",
        default=None,
        type="int",
        help="Set timeout for making calls to the gitlab API",
    )
    parser.add_option(
        "--overwrite",
        dest="overwrite",
        action="store_true",
        default=False,
        help="if --token is passed, overwrite private_token in configuration file",
    )
    parser.add_option(
        "--remote",
        dest="remote",
        action="store",
        type="string",
        default="upstream",
        help="which remote from which to operate on",
    )
    parser.add_option(
        "-q",
        "--quiet",
        dest="quiet",
        action="store_true",
        default=False,
        help="Print only the json with the results or in case of an unrecoverable error",
    )
    parser.add_option(
        "-y",
        "--yes",
        dest="yes",
        action="store_true",
        default=True,
        help="Assume yes to all prompts",
    )
    parser.add_option(
        "-w",
        "--wait",
        dest="wait",
        action="store",
        type="int",
        default=3,
        help="How long to wait every time a MR is rebased",
    )
    parser.add_option(
        "--clean-cached-branches",
        dest="clean_branch_cache",
        action="store_true",
        default=False,
        help="Remove branch files that are empty or don't match a local branch",
    )

    (options, args) = parser.parse_args(sys.argv)

    if len(args) < 2 and not options.clean_branch_cache:
        print("no merge requests given")
        sys.exit(1)

    if options.token is None and options.overwrite is True:
        print("--overwrite was passed, but no --token was passed along with it")
        sys.exit(1)

    # Initialize our repo object based on the local repo we have
    repo = init_repo()
    if repo is None:
        sys.exit(1)

    remote = API(repo, options.remote)

    try:
        config = Config(options, remote.host)
    except ValueError as e:
        print(e)
        sys.exit(1)

    # Annotate some variables
    cachedir: Path  # Path to directory where branch cache files reside

    cachedir = find_cache()
    cachedir = (
        cachedir
        / remote.host.replace("https://", "").replace("/", ".")
        / remote.user
        / remote.project
        / "branches"
    )

    if options.clean_branch_cache:
        # Annotate some variables
        filepath: Path  # Path to the branch cache file
        for branch in os.listdir(cachedir):
            filepath = cachedir / branch
            # If the files are empty they are of no use to us, just remove them
            if os.path.getsize(filepath) == 0:
                print("{} (empty file)".format(filepath))
                filepath.unlink()
                continue
            try:
                repo.git.rev_parse("--verify", branch)
            except GitCommandError:
                print("{} (no local branch)".format(filepath))
                filepath.unlink()
        sys.exit(0)

    gl = config.get_gitlab()

    project = gl.projects.get(
        remote.load_project_id(token=gl.private_token), retry_transient_errors=True, lazy=True
    )

    # Annotate some variables
    queue: Dict[str, str]  # A Dictionary of {merge request: its status}
    n: int  # Which member we are, this is checked against keys_len to not go out of index
    keys: List[str]  # List of strings that hold the 'merge request' from 'queue'
    keys_len: int  # How many keys we have

    """
    Create a dictionary that is our queue of merge requests to work on, they have the following
    scheme of {'MRNUM': 'STATE'}, the state can be one of the 3:
    - pending (this means the merge request needs to be processed)
    - merged (this means the merge request was merged, the best outcome)
    - any value other than the 2 above is an error and needs to be inspected by the user

    errors can happen for many reasons, not enough permissions to merge or to rebase, rebase failed
    because of conflicts, etc.

    also create a list of the keys we have, those are the ones we will iterate over in our workloop,
    and get the length of the list so we know when we have processed all the merge requests.
    """
    queue = dict()
    n = 0
    for arg in args[1:]:
        queue[arg] = "pending"

    keys = list(queue.keys())
    keys_len = len(keys)

    if options.dry_run is True:
        print("MRs to be merged:", keys)
        sys.exit(0)

    """
    This is a loop that iterates over all members of our queue dictionary using a needle that
    starts at 0 and will break the loop once the needle value gets higher than the length of
    our dictionary

    This is the logic of our loop:
    1. Get the merge request
    2. Check a few attributes of the merge request
       a. if the value of the 'state' key is 'merged', then set the merge request as
          'already merged' in the dictionary, increment the needle and restart the loop
       b. if the value of the 'state' key is 'closed', then set the merge request as 'closed' in
          the dictionary, increment the needle and restart the loop
       c. if the key 'work_in_progress' is True, then set the merge request as 'work in progress'
          in the dictionary, increment the needle and restart the loop
       d. if the key 'rebase_in_progress' is True, sleep for 2 seconds and restart the loop
       e. if the key 'rebase_in_progress' is False and 'merge_error' attribute is not null, then
          set the merge request in the dictionary as the value of the 'merge_error' key, increment
          the needle and restart the loop
    2. Try merging it
       a. if merging fails with error code 406, try starting a rebase request
          i. if asking for a rebase fails with error code 403, then set the merge request as
             'Rebase failed:' with the error message, increment the needle and restart the loop
          ii. if asking for a rebase returns 202, restart the loop
       b. if it fails with error code 401, then set the merge request as 'Merge failed:' with the
          error message, increment the needle and restart the loop
       c. if it works, then set the merge request as 'merged', increment the needle and restart the
          loop
    """
    # Annotate some variables
    name: str  # Number (or name) of the merge request we are merging
    cachepath: Path  # Path to the branch cache file is
    iid: int  # Number of the merge request
    present: str  # The string that represents the merge request, either number or branch(number)

    # Dictionary from GitLab, taken from the status of a merge request, we can't know the types
    # of what they give, and it can be anything ranging from 'str' to 'Dict[Dict[Any, Any], Any]
    attrs: Dict[Any, Any]

    while True:

        # This will be reached once we have worked on all members
        if n + 1 > keys_len:
            break

        # Set our needle in the list, k can be either the name of a branch of the internal id of a
        # merge request
        name = keys[n]
        cachepath = cachedir / name
        if cachepath.is_file():
            # If it is a file then try to read it and convert it to an integer at the same
            # time, there is the possibility of a FileNotFoundError but it is very unlikely
            try:
                iid = int(cachepath.read_text())
            except ValueError:
                # We reach here if the user has a cache file, we can read it, but the
                # value in it is not valid (not int), so check if the name of branch
                # given to us is *actually* an integer itself and try to use it, this deals
                # with the potential problem of someone having a branch literally called '123'
                # and they actually want to merge the MR with internal-id '123'
                if not options.quiet:
                    print(
                        "File has invalid value '{}', it must be an integer".format(
                            cachepath.read_text()
                        )
                    )
                    cachepath.unlink()  # Delete the file as it has an invalid value
                if name.isdigit():
                    iid = int(name)
                    present = name
                else:
                    queue[name] = "Invalid: branch name has an incorrect or empty cache file"
                    n += 1
                    continue
            else:
                # the way we represent the internal id for printing, in this case we do
                # branch_name(internal_id), if we reached here then we have a valid cache
                present = "{}({})".format(name, iid)
        else:
            if name.isdigit():
                iid = int(name)
                present = name
            else:
                queue[name] = "Invalid: string given for merge request is not integer"
                n += 1
                continue

        """
        Get the merge request, include_rebase_in_progress is required so
        we get information on whether we are rebasing
        """
        mr = project.mergerequests.get(iid, include_rebase_in_progress=True)

        attrs = mr.attributes
        if attrs["state"] == "merged":
            if not options.quiet:
                print(present, "is already merged")
            if present != name:  # This means we are using the branch cache file
                cachepath.unlink()
            queue[name] = "Merge: already merged"
            n += 1
            continue
        elif attrs["state"] == "closed":
            if not options.quiet:
                print(present, "is closed")
            if present != name:  # This means we are using the branch cache file
                cachepath.unlink()
            queue[name] = "Merge: closed"
            n += 1
            continue
        elif attrs["work_in_progress"] is True:
            if not options.quiet:
                print(present, "is a work in progress, can't merge")
            queue[name] = "Merge: work in progress"
            n += 1
            continue
        elif attrs["rebase_in_progress"] is True:
            if not options.quiet:
                print(
                    present,
                    "is currently rebasing, waiting",
                    options.wait,
                    "seconds to check if it still rebasing",
                )
            sleep(options.wait)
            continue
        elif attrs["rebase_in_progress"] is False and attrs["merge_error"] is not None:
            if not options.quiet:
                print(present, attrs["merge_error"])
            queue[name] = "Rebase: " + attrs["merge_error"]
            n += 1
            continue
        elif attrs["pipeline"]["status"] == "failed":
            if options.yes is False:
                choice = inquirer.confirm(
                    "Merge merge request even though the CI pipeline failed?", default=True
                )
            else:
                choice = options.yes
            if choice is False:
                if not options.quiet:
                    print(present, "skipped by the user because CI pipeline failed")
                queue[name] = "Merge: canceled by user prompt"
                n += 1
                continue

        try:
            mr.merge(should_remove_source_branch="true")
        except GitlabMRClosedError as e:
            if e.response_code == 406:
                if not options.quiet:
                    print(present, "cannot be merged, trying to rebase")
                try:
                    # Passing skip_ci actually doesn't work for some reason
                    # so a new CI Pipeline is always created unfortunately
                    #
                    # TODO: Find out why it doesn't work
                    mr.rebase(skip_ci=True)
                except GitlabMRRebaseError as err:
                    if err.response_code == 403:
                        if not options.quiet:
                            print("Rebase failed:", err.error_message)
                        queue[name] = "Rebase: " + err.error_message
                        n += 1
                        continue
                else:
                    continue
            elif e.response_code == 401:
                if not options.quiet:
                    print("Merge failed:", e.error_message)
                queue[name] = "Merge: " + e.error_message
                n += 1
                continue
            elif e.response_code == 405:
                if not options.quiet:
                    print("Merge failed:", e.error_message)
                queue[name] = "Merge: " + e.error_message
                n += 1
            else:
                print(e.error_message, "aborting completely")
                sys.exit(1)
        else:
            if not options.quiet:
                print("Merged", present)
            queue[name] = "merged"
            # Switch to master if our current branch is the active branch
            if name != str(iid):
                if name == repo.active_branch.name:
                    repo.git.checkout("master")
                repo.git.branch("-D", name)
            if present != name:  # This means we are using branch file
                cachepath.unlink()
            n += 1

    print(dumps(queue, indent=4))


if __name__ == "__main__":
    main()
