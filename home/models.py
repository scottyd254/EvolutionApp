from django.db import models
from blog.models import BlogIndexPage, BlogPage
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import RichTextField

class HomePage(Page):
    # hero image section
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only, 16:9 ratio recommended at least 1024 x 768 px",)


    

    content_panels = Page.content_panels + [
        FieldPanel("image"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blog_index = BlogIndexPage.objects.first()
        if blog_index:
             context['blogpages'] = BlogPage.objects.live().descendant_of(blog_index).order_by('-first_published_at')[:3]  # Limit to 3 latest posts
        return context