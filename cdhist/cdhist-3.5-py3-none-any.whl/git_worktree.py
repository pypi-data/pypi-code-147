#!/usr/bin/env python3
'Shell wrapper to conveniently cd between git worktrees.'
import os
import sys
import subprocess
from collections import deque
from dataclasses import dataclass
from pathlib import Path

from . import utils

HASH_LEN = 7

def get_level(path, cwd):
    'Get level at which cwd is within given paths parents'
    if path == cwd:
        level = 0
    else:
        try:
            level = len(path.parents) - path.parents.index(cwd)
        except Exception:
            level = sys.maxsize

    return level

@dataclass
class Tree:
    'Wrapper for individual worktree'
    path: Path
    path_u: Path
    head: str = None
    branch: str = None
    comment: str = None

class Trees:
    'Wrapper to manage the collection of worktrees'
    def fetch(self, args):
        'Run git and get list of worktrees'
        res = subprocess.run('git worktree list --porcelain'.split(),
                            stdout=subprocess.PIPE, text=True)
        if res.returncode != 0:
            return False

        trees = deque()
        tree = None
        level = level_index = None
        cwd = Path.cwd()
        for line in res.stdout.splitlines():
            line = line.strip()
            if not line:
                tree = None
                continue

            if ' ' in line:
                field, rest = line.split(maxsplit=1)
            else:
                field = line

            if field == 'worktree':
                path_u = path = Path(rest)

                if args.git_relative:
                    path_u = os.path.relpath(path)
                elif not args.no_user:
                    path_u = Path(utils.unexpanduser(str(path)))

                tlevel = get_level(path, cwd)
                if level is None or tlevel < level:
                    level = tlevel
                    level_index = len(trees)

                tree = Tree(path, path_u)
                trees.append(tree)

            elif field == 'HEAD':
                if tree:
                    tree.head = rest[:HASH_LEN]
            elif field == 'branch':
                if tree:
                    tree.branch = rest.split('/')[-1]
            else:
                if tree:
                    tree.comment = field

        # Move the worktree for the current working directory to the
        # front of the list
        if len(trees) > 0 and level_index >= 0:
            trees.rotate(-level_index)
            tree = trees.popleft()
            trees.rotate(level_index)
            trees.append(tree)

        self.paths = [t.path for t in trees]
        self.trees = trees
        return True

    def get_path_from_branch(self, text):
        'Return 1st branch (then hash) that starts with given text'
        for t in self.trees:
            if t.branch and t.branch.startswith(text):
                return t.path

        for t in self.trees:
            if t.head and t.head.startswith(text):
                return t.path

        return None

    def build_output(self):
        'Present list of worktrees to user and prompt for selection'
        # List the worktrees
        pw = max(len(str(t.path_u)) for t in self.trees)
        lines = []
        for t in self.trees:
            tlist = [f'{str(t.path_u):{pw}}']
            if t.head:
                tlist.append(t.head)
            if t.branch:
                tlist.append(f'[{t.branch}]')
            if t.comment:
                tlist.append(t.comment)

            lines.append(' '.join(tlist))

        return lines

def parse_args(args):
    'Parse command line for git worktree functionality'
    trees = Trees()

    if not trees.fetch(args):
        return None

    if args.directory and not args.list:
        path = None
        arg = args.directory
        if arg[0] == '-':
            path = utils.check_digit(arg[1:], trees.paths)
        else:
            path = trees.get_path_from_branch(arg)

    elif args.search:
        path = utils.check_search(args.search, trees.paths,
                                  list_is_paths=True)
    else:
        arg = utils.prompt(args, trees.build_output())
        if not arg:
            return None

        if len(arg) > 1 and arg[0] == '/':
            path = utils.check_search(arg[1:], trees.paths,
                                    list_is_paths=True)
        else:
            path = utils.check_digit(arg, trees.paths) or \
                    trees.get_path_from_branch(arg)

    if not path:
        sys.exit(f'fatal: no worktree for "{arg}".')

    return path

# vim: se et:
