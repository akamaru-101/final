from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, filename, filesize, content):
        self.filename = filename
        self.filesize = filesize
        self.content = content

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def save(self):
        pass

class Word(Document):
    def open(self):
        print(f"Open Word document: {self.filename}")

    def read(self):
        print(f"Read Word document: {self.filename}")
        print(f"Content: {self.content}")

    def save(self):
        print(f"Save Word document: {self.filename}")

class PDF(Document):
    def open(self):
        print(f"Open PDF document: {self.filename}")

    def read(self):
        print(f"Read PDF document: {self.filename}")
        print(f"Content: {self.content}")

    def save(self):
        print(f"Save PDF document: {self.filename}")

class Excel(Document):
    def open(self):
        print(f"Open Excel document: {self.filename}")

    def read(self):
        print(f"Read Excel document: {self.filename}")
        print(f"Content: {self.content}")

    def save(self):
        print(f"Save Excel document: {self.filename}")

class Doc_Factory:
    @staticmethod
    def create_doc(doc_type, filename, filesize, content):
        if doc_type == "Word":
            return Word(filename, filesize, content)
        elif doc_type == "PDF":
            return PDF(filename, filesize, content)
        elif doc_type == "Excel":
            return Excel(filename, filesize, content)
        else:
            print("Invalid document type")


if __name__ == "__main__":
    word1 = Doc_Factory.create_doc("Word", "akmal.docx", 1024, "This is a Word document.")
    word1.open()
    word1.read()
    word1.save()

    pdf1 = Doc_Factory.create_doc("PDF", "kamel.pdf", 2048, "This is a PDF document.")
    pdf1.open()
    pdf1.read()
    pdf1.save()

    excel1 = Doc_Factory.create_doc("Excel", "grades.excel", 3072, "This is an Excel document.")
    excel1.open()
    excel1.read()
    excel1.save()
