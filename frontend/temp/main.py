
class Template:
    def __init__(self, css_dir, js_dir):
        self.css_dir = css_dir
        self.js_dir = js_dir

    def render_css(self, name: str) -> str:
        try:
            with open(f"frontend/{self.css_dir}/{name}", "r") as f:
                return f.read()
        except FileNotFoundError:
            raise f"{name} File not found: frontend/{self.css_dir}/{name}"

    def render_js(self, name: str) -> str:
        try:
            with open(f"frontend/{self.js_dir}/{name}", "r") as f:
                return f.read()
        except FileNotFoundError:
            raise f"{name} File not found: frontend/{self.js_dir}/{name}"