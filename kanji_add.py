# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

def find_notes_with_kanji(h):
    return mw.col.findNotes("deck:japonais -is:suspended " + h)

def myFunction():
    # get the number of cards in the current collection, which is stored in
    # the main window
    ids = mw.col.findNotes("deck:Kanji")
    count = 0
    for i in ids:
        kanjinote = mw.col.getNote(i)
        first = True
        for jap_note_id in find_notes_with_kanji(kanjinote['kanji']):
            jap_note = mw.col.getNote(jap_note_id)
            jap_word = jap_note['japanese'].strip()
            if " " not in jap_word:
                count += 1
                if first:
                    first = False
                    kanjinote['words'] = jap_word
                    kanjinote['words pro'] = jap_note['hiragana']
                else:
                    kanjinote['words'] += " <div>" + jap_word + "</div>"
                    kanjinote['words pro'] += " <div>" + jap_note['hiragana'] + "</div>"
        kanjinote.flush()
    showInfo("counted %d notes" % (count))

action = QAction("add missing Kanji words", mw)
action.triggered.connect(myFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
