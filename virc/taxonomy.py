"""The closet's vocabulary: every category and attribute an item can have.

This is the single source of truth. The classifier's labels, the database
columns and the UI filters all come from here, so a change starts here.
"""

# TODO(you): decide flat list vs hierarchy (decision 002), then fill this in.
#   Flat:       CATEGORIES = {"t-shirt", "jeans", ...}
#   Hierarchy:  CATEGORIES = {"tops": {"t-shirt", "hoodie"}, "bottoms": {...}}
#   Every item must fit exactly one category, so include an "other" bucket.
CATEGORIES = ...

# TODO(you): the named colors you'll filter by (~12 is typical). k-means will
# give exact hex values later; this is the list they get mapped onto.
COLORS = ...

# TODO(you): one constant per extra attribute you decide to track (season,
# formality, pattern...). Above each, note in a comment:
#   - one value or several?
#   - where the value comes from: the model, calculated, or entered by you?


def all_categories() -> set[str]:
    """Every category an item can be labeled with (the leaves, if you use a hierarchy)."""
    # TODO(you): flat: return the set as-is. Hierarchy: collect every child set
    # into one set. Look up set.union / the | operator.
    raise NotImplementedError


def is_valid(field: str, value: str) -> bool:
    """True if value is allowed for field, e.g. is_valid("category", "jeans")."""
    # TODO(you): find which allowed set belongs to `field`, then check membership.
    # An unknown field should raise ValueError rather than return False:
    # a typo in a column name should fail loudly, not quietly.
    raise NotImplementedError
