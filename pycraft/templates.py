from pycraft import expose, blocks
import os, csv

@expose.expose()
def from_template(template,*,mc=None):
    """Load a template file from disk and render as blocks"""
    # Your code here...

def convert_name(name, abbreviations=None):
    """Take a name, maybe a short-name, and turn it into a block object
    """
    # translate abbreviation to block-names...
    # Now convert block-names to block types
    # blocks.Block.as_instance(block_name)


def load_template(template, abbreviations=None):
    """Find template file, load it into memory as block-names

    Templates are in `CSV` format, which is a 
    plain-text format that looks like this:

        S,S,D,S,S
        S, , , ,S
        S,S,G,S,S
        -
        S,S,D,S,S
        S, , , ,S
        S,S,G,S,S

    where a bunch of abbreviations should be available
    for common types, but full block-names can
    be used as well.
    
    return should be [
        layer,
        layer,
        layer,
    ]
    layer being [
        [name,name,name],
        [name,name,name],
    ]
    """

    # Open your template in this editor (it's in the 
    # directory templates) and look at what the 
    # data looks like, can you see how it is the 
    # stuff you typed into google docs, but with
    # a set of rules for how to present it?


    # CSV is a common format, find pre-existing code
    # (a module) for reading the CSV information.

    # To read the template, you'll need to find the 
    # file on disk. Given a filename `filename`, the
    # final location would be:

    #     os.path.join(HERE,'templates',os.path.basename(filename))
    
    # You will need to pass the CSV module a `file` object
    # which you get by calling `open` on the filename
    # above.

    # The csv module will give you a sequence of rows from
    # your spreadsheet, like `['S','S','D','S','S']` which
    # you can iterate over with a `for` loop.

    # You will need to separate the rows into layers by
    # looking for the `-` value in the first column
    # of the row (`row[0]`). How will you gather the
    # rows into layers?

    # You will need to translate abbreviations into
    # full block-names to pass them to the server.
    # To do that, you'll need to setup a `mapping`
    # from each abbreviation to its full block-name.

    # Mappings in Python are generally written with
    # `{}` characters and are called `dicts`. So a 
    # mapping might look like:

    #     abbreviations = {
    #         'S': 'STONE',
    #         'G': 'WHITE_STAINED_GLASS',
    #     }

    # You can find `_blocknames.py` in this project
    # which includes all of the block names that are
    # currently known to work with the server.
