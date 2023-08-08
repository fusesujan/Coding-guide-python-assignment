"""
[Builder Design Pattern] Design a document generator using the Builder Design
Pattern. Create a DocumentBuilder that creates documents of various types (e.g., PDF,
HTML, Plain Text). Implement the builder methods to format the document content and
structure according to the chosen type. Demonstrate how the Builder Design Pattern
allows for the creation of different document formats without tightly coupling the
document generation logic.
"""
from abc import ABC, abstractmethod


class Document:
    """
    Represents a document of various types.
    """

    def __init__(self):
        self.content = ""

    def add_content(self, content: str) -> None:
        """
        adding content to existing content
        """
        self.content += content

    def get_content(self) -> str:
        """
        returning existing content
        """
        return self.content


class DocumentBuilder(ABC):
    """
    Abstract base class for document builders.
    """
    @abstractmethod
    def create_title(self, title: str) -> None:
        """
        nothing here just a pass
        """

    @abstractmethod
    def create_paragraph(self, paragraph: str) -> None:
        """
        nothing here just a pass
        """

    @abstractmethod
    def create_footer(self, footer: str) -> None:
        """
        nothing here just a pass
        """

    @abstractmethod
    def get_document(self) -> Document:
        """
        nothing here just a pass
        """


class PDFDocumentBuilder(DocumentBuilder):
    """
    Concrete PDF document builder.
    """

    def __init__(self):
        self.document = Document()

    def create_title(self, title: str) -> None:
        self.document.add_content(f"[PDF Title]: {title}\n")

    def create_paragraph(self, paragraph: str) -> None:
        self.document.add_content(f"[PDF Paragraph]: {paragraph}\n")

    def create_footer(self, footer: str) -> None:
        self.document.add_content(f"[PDF Footer]: {footer}\n")

    def get_document(self) -> Document:
        return self.document


class HTMLDocumentBuilder(DocumentBuilder):
    """
    Concrete HTML document builder.
    """

    def __init__(self):
        self.document = Document()

    def create_title(self, title: str) -> None:
        self.document.add_content(f"<h1>{title}</h1>\n")

    def create_paragraph(self, paragraph: str) -> None:
        self.document.add_content(f"<p>{paragraph}</p>\n")

    def create_footer(self, footer: str) -> None:
        self.document.add_content(f"<footer>{footer}</footer>\n")

    def get_document(self) -> Document:
        return self.document

# Similarly, you can define PlainTextDocumentBuilder class


class DocumentGenerator:
    """
    DocumentGenerator class to generate documents using a specified builder.
    """

    def __init__(self, builder: DocumentBuilder):
        self.builder = builder

    def generate_document(self) -> Document:
        """
        defining builder with static entries to each methods 
        in creation of title,
        paragraph, and footer.
        """
        self.builder.create_title("Sample Title")
        self.builder.create_paragraph("This is a paragraph.")
        self.builder.create_footer("Sample Footer")
        return self.builder.get_document()


def main():
    """
    Main function to demonstrate the Builder Design Pattern for generating different types of documents.
    """
    builder_type = input("Enter builder type (pdf/html/plain): ")
    if builder_type == "pdf":
        builder = PDFDocumentBuilder()
    elif builder_type == "html":
        builder = HTMLDocumentBuilder()
    elif builder_type == "plain":
        # builder = PlainTextDocumentBuilder()
        pass  # Uncomment and complete the PlainTextDocumentBuilder class
    else:
        raise ValueError("Invalid builder type!")

    generator = DocumentGenerator(builder)
    document = generator.generate_document()
    print(document.get_content())


if __name__ == "__main__":
    main()
