import urwid
import time
import threading
import sys
import os

from .messages import teddy

class SimpleForm(urwid.Edit):
    def __init__(self, message, *args, response=None, align='center', **kwargs):
        message = '{} \n {}'.format(teddy, message)
        self.response = response
        super(SimpleForm, self).__init__(message, *args, align='center', **kwargs)

    def keypress(self, size, key):
        if key != 'enter':
            return super(SimpleForm, self).keypress(size, key)
        if self.edit_text != '':
            self.response(self.edit_text)

class TextButton(urwid.Button):
    def __init__(self, callback, caption, user_data=None, icon=u'  \N{BULLET} '):
        super(TextButton, self).__init__("")
        urwid.connect_signal(self, 'click', callback, user_data)
        self._w = urwid.AttrMap(urwid.SelectableIcon(
            [icon, caption], 2), None, 'selected')


class LineWalker(urwid.ListWalker):
    """ListWalker-compatible class for lazily reading file contents."""

    def __init__(self, name):
        if not os.path.exists(name):
            with open(name, 'w'): pass
            self.file = None

        self.file = open(name)
        self.lines = []
        self.focus = 0

    def get_focus(self):
        return self._get_at_pos(self.focus)

    def set_focus(self, focus):
        self.focus = focus
        self._modified()

    def get_next(self, start_from):
        return self._get_at_pos(start_from + 1)

    def get_prev(self, start_from):
        return self._get_at_pos(start_from - 1)

    def read_next_line(self):
        """Read another line from the file."""

        next_line = self.file.readline()

        if not next_line or next_line[-1:] != '\n':
            # no newline on last line of file
            self.file = None
        else:
            # trim newline characters
            next_line = next_line[:-1]

        expanded = next_line.expandtabs()

        edit = urwid.Edit("", expanded, allow_tab=True)
        edit.set_edit_pos(0)
        edit.original_text = next_line
        self.lines.append(edit)

        return next_line


    def _get_at_pos(self, pos):
        """Return a widget for the line number passed."""

        if pos < 0:
            # line 0 is the start of the file, no more above
            return None, None

        if len(self.lines) > pos:
            # we have that line so return it
            return self.lines[pos], pos

        if self.file is None:
            # file is closed, so there are no more lines
            return None, None

        assert pos == len(self.lines), "out of order request?"

        self.read_next_line()

        return self.lines[-1], pos

    def split_focus(self):
        """Divide the focus edit widget at the cursor location."""

        focus = self.lines[self.focus]
        pos = focus.edit_pos
        edit = urwid.Edit("",focus.edit_text[pos:], allow_tab=True)
        edit.original_text = ""
        focus.set_edit_text(focus.edit_text[:pos])
        edit.set_edit_pos(0)
        self.lines.insert(self.focus+1, edit)

    def combine_focus_with_prev(self):
        """Combine the focus edit widget with the one above."""

        above, ignore = self.get_prev(self.focus)
        if above is None:
            # already at the top
            return

        focus = self.lines[self.focus]
        above.set_edit_pos(len(above.edit_text))
        above.set_edit_text(above.edit_text + focus.edit_text)
        del self.lines[self.focus]
        self.focus -= 1

    def combine_focus_with_next(self):
        """Combine the focus edit widget with the one below."""

        below, ignore = self.get_next(self.focus)
        if below is None:
            # already at bottom
            return

        focus = self.lines[self.focus]
        focus.set_edit_text(focus.edit_text + below.edit_text)
        del self.lines[self.focus+1]


class EditDisplay:
    on_delete = None

    def __init__(self, name):
        self.footer = self.get_footer()
        self.listbox = urwid.Filler(urwid.Text("foo"))
        self.view = urwid.Frame(self.listbox,
            footer=self.footer)
        self.open(name)

    def open(self, name, on_delete=None):
        self.save_name = name
        self.walker = LineWalker(name)
        self.listbox = urwid.ListBox(self.walker)
        self.view.set_body(self.listbox)
        self.on_delete = on_delete
        self.view.set_footer(self.get_footer())

    def show_header_message(self, message):
        self.view.set_header(urwid.Text(message, align='center'))

        def blank():
            self.view.set_header(None)
        threading.Timer(3, blank, []).start()

    def get_footer(self):
        self.save_button = urwid.Button('save', self.handle_save_click)
        self.delete_button = urwid.Button('delete', self.handle_delete_click)
        return urwid.GridFlow(
            [self.delete_button, self.save_button],
            10, 1, 1, 'right')

    def handle_save_click(self, button, user_data=None):
        self.save_file()

    def handle_delete_click(self, button, user_data=None):
        os.remove(self.save_name)
        self.view.set_footer(None)
        self.view.set_body(urwid.Filler(urwid.Text('deleted', align='center')))
        if self.on_delete:
            self.on_delete()

    def unhandled_keypress(self, k, loop):
        """Last resort for keypresses."""
        if k == "f5" or k == 'ctrl w':
            self.save_file()
        elif k == "f8":
            raise urwid.ExitMainLoop()
        elif k == "delete":
            # delete at end of line
            self.walker.combine_focus_with_next()
        elif k == "backspace":
            # backspace at beginning of line
            self.walker.combine_focus_with_prev()
        elif k == "enter":
            # start new line
            self.walker.split_focus()
            # move the cursor to the new line and reset pref_col
            loop.process_input(["down", "home"])
        elif k == "right":
            w, pos = self.walker.get_focus()
            w, pos = self.walker.get_next(pos)
            if w:
                self.listbox.set_focus(pos, 'above')
                loop.process_input(["home"])
        elif k == "left":
            w, pos = self.walker.get_focus()
            w, pos = self.walker.get_prev(pos)
            if w:
                self.listbox.set_focus(pos, 'below')
                loop.process_input(["end"])
        elif k == "ctrl right":
            loop.process_input(['end', "right"])
        else:
            return
        return True


    def save_file(self):
        """Write the file out to disk."""
        l = []
        walk = self.walker
        for edit in walk.lines:
            # collect the text already stored in edit widgets
            if edit.original_text.expandtabs() == edit.edit_text:
                l.append(edit.original_text)
            else:
                l.append(re_tab(edit.edit_text))

        # then the rest
        while walk.file is not None:
            l.append(walk.read_next_line())

        # write back to disk
        outfile = open(self.save_name, "w")

        prefix = ""
        for line in l:
            outfile.write(prefix + line)
            prefix = "\n"

        self.show_header_message('saved')

def re_tab(s):
    """Return a tabbed string from an expanded one."""
    l = []
    p = 0
    for i in range(8, len(s), 8):
        if s[i-2:i] == "  ":
            # collapse two or more spaces into a tab
            l.append(s[p:i].rstrip() + "\t")
            p = i

    if p == 0:
        return s
    else:
        l.append(s[p:])
        return "".join(l)

