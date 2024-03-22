# Filesystem

    from udk import filesystem

Filesystem is a collection of file operations. For example `mov`:

    # Moves a file
    filesystem.mov("/path/to/file", "/path/to/destination", "Error message (optional)")
The `rem` function deletes a file:

    filesystem.rem("/path/to/file", "Error message (optional)")
The `see` function prints file contents:

    filesystem.see("/path/to/file", "Error message (optional)")

The `create` function creates an new text file:

    filesystem.create("/path/to/file", "Error message (optional)")