class Git:
    def __init__(self, con):
        self.con = con

    def save(self):
        self.con.exe("git config credential.helper store")

    def add(self):
        self.con.exe("git config credential.helper store")
        self.con.exe("git add .")

    def commit(self, msg="updated"):
        self.con.exe('git commit -m "{}"'.format(msg))

    def push(self):
        self.con.exe("git push origin master")

    def pull(self):
        self.con.exe("git pull")

    def put(self):
        self.add()
        self.commit()
        self.push()

    def get(self):
        self.pull()
