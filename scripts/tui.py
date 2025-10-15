from textual.app import App, ComposeResult
from textual.widgets import TextArea, Header, Footer
from textual.containers import Vertical


class EditableTextApp(App):
    def __init__(self, llm_response: str):
        super().__init__()
        self.my_text = llm_response

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            # Create TextArea with initial text
            yield TextArea(self.my_text, id="text_area")
        yield Footer()

    def on_mount(self) -> None:
        text_area = self.query_one("#text_area", TextArea)

if __name__ == "__main__":
    app = EditableTextApp("default text")
    app.run()
