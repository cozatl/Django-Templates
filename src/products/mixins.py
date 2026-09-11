
class TemplateTitleMixin:
    """
    Mixin to add a title to the context for template rendering.
    """

    title = None  # Default title, can be overridden in subclasses

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_title()
        return context

    def get_title(self):
        """
        Returns the title for the template context.
        If the title attribute is set, it will be used; otherwise,
        a default title is returned.
        """
        return self.title if self.title else "Default Title"
