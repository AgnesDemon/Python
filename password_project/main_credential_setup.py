class CredentialSet:
    id: str = None
    title: str = None
    username: str = None
    password: str = None
    url: str = None
    notes: str = None

    def __init__(this, title: str, username: str, password: str, url: str = "", notes: str = ""):
        this.title = title
        this.username = username
        this.password = password
        this.url = url
        this.notes = notes