import sys
from optparse import OptionParser
from typing import List

import editor
from gitlab import GitlabAuthenticationError, GitlabUpdateError

from mkmr.api import API
from mkmr.config import Config
from mkmr.utils import find_cache, init_repo, strtobool

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
        "-y",
        "--yes",
        dest="yes",
        action="store_true",
        default=False,
        help="Assume yes to all prompts",
    )

    (options, args) = parser.parse_args(sys.argv)

    if len(args) < 2:
        print("no merge request given")
        sys.exit(1)

    if options.token is None and options.overwrite is True:
        print("--overwrite was passed, but no --token was passed along with it")
        sys.exit(1)

    mrnum = args[1]

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

    gl = config.get_gitlab()

    name = mrnum
    if not mrnum.isdigit():
        try:
            cachepath = find_cache()
            # This path should be, taking alpine/aports from gitlab.alpinelinux.org as example:
            # $XDG_CACHE_HOME/mkmr/gitlab.alpinelinux.org/alpine/aports/branches/$source_branch
            cachepath = (
                cachepath
                / remote.host.replace("https://", "").replace("/", ".")
                / remote.user
                / remote.project
                / "branches"
                / name
            )
            mrnum = cachepath.read_text()
        except FileNotFoundError:
            print("branch name given, {}, has no corresponding cache file".format(name))
            sys.exit(1)
        else:
            # This is executed in a try-catch if there are no exceptions raised
            if mrnum == "":
                print("cache file for {} is empty".format(name))
                cachepath.unlink()  # Delete the file as it is empty
                sys.exit(1)

    project = gl.projects.get(
        remote.load_project_id(token=gl.private_token), retry_transient_errors=True, lazy=True
    )
    mr = project.mergerequests.get(mrnum, include_rebase_in_progress=True)

    # If discussion isn't locked then the value returned is a None instead of a false like it is
    # normally expected
    discussion = not mr.attributes["discussion_locked"]
    if discussion is None:
        discussion = True
    else:
        discussion = False

    state = mr.attributes["state"]
    if state == "opened" or state == "merged" or state == "repoened":
        state = "close"
    else:
        state = "reopen"

    if not mr.attributes["labels"]:
        labels = None

    # The input variable will hold all the values we allow the user to edit,
    # we show all of them to the user in a text editor (they decide it by
    # setting the EDITOR variable) and they modify as they wish, we send
    # them back to be parsed, if any errors are found we tell the userr
    # and change the valid changes.
    input: str = "# Set to 'close' to close the merge request\n"
    input += "# set to 'reopen' to open a closed merge request\n"
    input += "State: {}\n".format(mr.attributes["state"])

    input += "\n# Line must\n"
    input += "Title: {}\n".format(mr.attributes["title"])

    input += "\n# Any long multi-line string, will consider everything until the first line\n"
    input += "# that starts with a hashtag (#)\n"
    input += "Description: {}\n".format(mr.attributes["description"])

    input += "\n# Comma-separated list of labels, have it empty to remove all labels\n"
    input += "Labels: {}\n".format(labels)

    input += "\n# If this is true then the source branch of the Merge Request will de deleted\n"
    input += "# when this Merge Request is merged, takes 'true' or 'false'\n"
    input += "Remove source branch when merged: {}\n".format(
        mr.attributes["force_remove_source_branch"]
    )

    input += "\n# Name of the branch the branch the commit will be land on\n"
    input += "Target Branch: {}\n".format(mr.attributes["target_branch"])

    input += "\n# If 'true' no discussion can happen, 'false' otherwise\n"
    input += "Lock Discussion: {}\n".format(discussion)

    input += "\n# If 'true' then all commits will be squashed into a single one\n"
    input += "Squash on merge: {}\n".format(mr.attributes["squash"])

    input += "\n# If 'true' maintainers of the repository will be able to push commits\n"
    input += "# into your branch, this is required for people rebasing-and-merging\n"
    input += "Allow Maintainers to push: {}".format(mr.attributes["allow_maintainer_to_push"])

    # This is the result of the edits of the user, and what we will parse to get all the answers
    # we need from what the user edited. Use splitlines() to split it into a list we can walk at
    # the pace we require.
    output: List[str] = editor.edit(contents=input).decode("utf-8").splitlines()
    output_len = len(output)
    linenum: int = 0

    final_state = None
    final_title = None
    final_desc = None
    final_labels = None
    final_remove_branch = None
    final_target_branch = None
    final_lock_discussion = None
    final_squash = None
    final_collab = None

    while True:
        if linenum >= output_len:
            break  # We reached the end of the multi-line string, quit
        if output[linenum].startswith("State: "):
            final_state = ":".join(output[linenum].split(":")[1:]).strip()
            if (
                final_state == mr.attributes["state"]
                and final_state != "close"
                and final_state != "repoen"
            ):
                print("State given must be either close or reopen")
                final_state = None
            linenum += 1
            continue
        if output[linenum].startswith("Title: "):
            final_title = ":".join(output[linenum].split(":")[1:]).strip()
            if len(final_title) >= 255:
                print("The title must be at most 254 characters, keeping old title")
                final_title = None
            linenum += 1
            continue
        if output[linenum].startswith("Description: "):
            final_desc = "{}".format(":".join(output[linenum].split(":")[1:]).strip())
            linenum += 1
            while not output[linenum].startswith("#"):
                final_desc += "\n{}".format(output[linenum])
                linenum += 1
            # This value is given to us by the GitLab V4 API and is the hard limit for a description
            if len(final_desc) > 1048576:
                print("The description must be at most 1048576 characters, keeping old description")
                final_desc = None  # It means it won't be saved
            continue
        if output[linenum].startswith("Labels: "):
            final_labels = ":".join(output[linenum].split(":")[1:]).strip()
            linenum += 1
            continue
        if output[linenum].startswith("Remove source branch when merged: "):
            final_remove_branch = strtobool(":".join(output[linenum].split(":")[1:]).strip())
            linenum += 1
            continue
        if output[linenum].startswith("Target Branch: "):
            final_target_branch = ":".join(output[linenum].split(":")[1:]).strip()
            linenum += 1
            continue
        if output[linenum].startswith("Lock Discussion: "):
            final_lock_discussion = strtobool(":".join(output[linenum].split(":")[1:]).strip())
            linenum += 1
            continue
        if output[linenum].startswith("Squash on merge: "):
            final_squash = ":".join(output[linenum].split(":")[1:]).strip()
            linenum += 1
            continue
        if output[linenum].startswith("Allow Maintainers to push: "):
            final_collab = ":".join(output[linenum].split(":")[1:]).strip()
            linenum += 1
            continue
        linenum += 1

    # If final_state is None then it hasn't changed, also deny if it isn't either
    # 'close' or 'reopen' as those are the only valid values.
    if final_state is not None:
        if final_state != "close" and final_state != "repoen":
            setattr(mr, "state", final_state)

    if final_desc is not None:
        setattr(mr, "title", final_title)

    if final_desc is not None:
        setattr(mr, "description", final_desc)

    if final_labels is not None:
        setattr(mr, "labels", final_labels)

    if final_remove_branch is not None:
        setattr(mr, "force_remove_source_branch", final_remove_branch)

    if final_target_branch is not None:
        setattr(mr, "target_branch", final_target_branch)

    if final_lock_discussion is not None:
        setattr(mr, "discussion_locked", final_lock_discussion)

    if final_squash is not None:
        setattr(mr, "squash", final_squash)

    if final_collab is not None:
        setattr(mr, "allow_maintainer_to_push", final_collab)

    if options.dry_run is True:
        print("State:", final_state)
        print("Title:", final_title)
        print("Description:", final_desc)
        print("Labels:", final_labels)
        print("Remove source branch when merged:", final_remove_branch)
        print("Target Branch:", final_target_branch)
        print("Lock Discussion:", final_lock_discussion)
        print("Squash on merge:", final_squash)
        print("Allow Maintainers to push:", final_collab)
        sys.exit(0)

    try:
        mr.save()
    except GitlabAuthenticationError as e:
        print("Failed to update, authentication error\n\n{}".format(e))
    except GitlabUpdateError as e:
        print("Failed to update, update error\n\n{}".format(e))


if __name__ == "__main__":
    main()
