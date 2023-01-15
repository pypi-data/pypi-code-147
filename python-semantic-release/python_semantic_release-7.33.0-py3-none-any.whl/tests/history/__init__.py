MAJOR = (
    "221",
    "feat(x): Add super-feature\n\n"
    "BREAKING CHANGE: Uses super-feature as default instead of dull-feature.",
)
MAJOR2 = (
    "222",
    "feat(x): Add super-feature\n\nSome explanation\n\n"
    "BREAKING CHANGE: Uses super-feature as default instead of dull-feature.",
)
MAJOR_MENTIONING_1_0_0 = (
    "223",
    "feat(x): Add super-feature\n\nSome explanation\n\n"
    "BREAKING CHANGE: Uses super-feature as default instead of dull-feature from v1.0.0.",
)
MAJOR_MULTIPLE_FOOTERS = (
    "244",
    "feat(x): Lots of breaking changes\n\n"
    "BREAKING CHANGE: Breaking change 1\n\n"
    "Not a BREAKING CHANGE\n\n"
    "BREAKING CHANGE: Breaking change 2",
)
MAJOR_EXCL_WITH_FOOTER = (
    "231",
    "feat(x)!: Add another feature\n\n"
    "BREAKING CHANGE: Another feature, another breaking change",
)
MAJOR_EXCL_NOT_FOOTER = (
    "232",
    "fix!: Fix a big bug that everyone exploited\n\nThis is the reason you should not exploit bugs",
)
MINOR = ("111", "feat(x): Add non-breaking super-feature")
PATCH = ("24", "fix(x): Fix bug in super-feature")
NO_TAG = ("191", "docs(x): Add documentation for super-feature")
UNKNOWN_STYLE = ("7", "random commits are the worst")

ALL_KINDS_OF_COMMIT_MESSAGES = [MINOR, MAJOR, MINOR, PATCH]
MINOR_AND_PATCH_COMMIT_MESSAGES = [MINOR, PATCH]
PATCH_COMMIT_MESSAGES = [PATCH, PATCH]
MAJOR_LAST_RELEASE_MINOR_AFTER = [
    MINOR,
    ("22", "1.1.0\n\nAutomatically generated by python-semantic-release\n"),
    MAJOR,
]
MAJOR_MENTIONING_LAST_VERSION = [
    MAJOR_MENTIONING_1_0_0,
    ("22", "1.0.0\n\nAutomatically generated by python-semantic-release\n"),
    MAJOR,
]
