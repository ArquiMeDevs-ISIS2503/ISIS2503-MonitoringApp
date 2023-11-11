from ..logic.entry_logic import get_entry_by_entryDate, create_entry, create_entry_object

# this function return entry id. If the entry does not exist, then it is created


def get_entry(entryDate):
    entry = get_entry_by_entryDate(entryDate)
    if entry != None:
        return (entry)
    else:
        entry = create_entry_object(entryDate)
        return (entry)
