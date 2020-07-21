from tkinter import StringVar, Label, Entry, Button
from functools import partial

class IHM:
    '''Class used to generate an Ihm
    which give parameter to a runner instance through user inputs'''

    def __init__(self):
        self._values = list()
        self._replay = True

    def _get_values(self):
        for c, v in enumerate(self._values):
            try:
                self._values[c] = int(v)
            except ValueError:
                print('No letter allowed', v)
                return False
            except TypeError:
                print('No letter allowed', v)
                return False
        return self._values

    def _get_replay(self):
        return self._replay

    def _set_replay(self, bool):
        self._replay = bool

    values = property(_get_values)
    replay = property(_get_replay, _set_replay)

    def data_treatment(self, elements, values, root):
        values.clear()
        for i in elements:
            values.append(i[1].get())
        root.destroy()

    def close(self, root):
        self._set_replay(False)
        root.destroy()

    def retry(self, root):
        root.destroy()

    def launch(self, root):
        root.title("Paramètres GOL")
        root.geometry("300x150")
        title = Label(root, text='PARAMETERS :')
        elements = [(Label(root, text='Dimension'), Entry(root, textvariable=(StringVar(root)))),
                    (Label(root, text='Round number'), Entry(root, textvariable=(StringVar(root)))),
                    (Label(root, text='Form amount'), Entry(root, textvariable=(StringVar(root))))]
        button = Button(root, text='lancer', command=partial(self.data_treatment, elements, self._values, root))

        title.grid(column=0, row=0)

        [(value[1][0].grid(column=0, row=value[0]+1), value[1][1].grid(column=1, row=value[0]+1)) for value in [(i,tupl) for i,tupl in enumerate(elements)]]

        button.grid(column=1, row=5)
        root.mainloop()

    def pop_up(self, root):
        root.title("Rejouer au GOL")
        root.geometry("250x100")
        title_retry = Label(root, text='Would you like to retry ?')
        buttonYes = Button(root, text='Yes', command=partial(self.retry, root))
        buttonNo = Button(root, text='No', command=partial(self.close, root))

        title_retry.grid(column=0, row=0)

        buttonYes.grid(column=0, row=1)
        buttonNo.grid(column=1, row=1)
        root.mainloop()
