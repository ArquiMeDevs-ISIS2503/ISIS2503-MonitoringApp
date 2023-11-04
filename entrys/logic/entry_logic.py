from ..models import Entry


def get_entrys():
    queryset = Entry.objects.all()
    return (queryset)


def create_entry(form):
    measurement = form.save() 
    measurement.save()
    return ()

def create_entry_object(startDate, entryDate, diagnostic, vitalSign):
    entry = Entry()
    entry.startDate = startDate
    entry.entryDate = entryDate
    entry.diagnostic = diagnostic
    entry.vitalSign = vitalSign
    entry.save()
    return (entry)


def get_entry_by_entryDate(entryDate):
    try:
        entry = Entry.objects.get(entryDate=entryDate)
        return (entry)
    except:
        entry = None
        return (entry)
